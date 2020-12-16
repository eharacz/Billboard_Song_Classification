def get_token():
    client_token = base64.b64encode("{}:{}".format(client_id, client_secret)
                                    .encode('UTF-8')).decode('ascii')

    headers = {"Authorization": "Basic {}".format(client_token)}
    payload = {
        "grant_type": "client_credentials"
    }
    token_request = requests.post(
        SPOTIFY_TOKEN_URL, data=payload, headers=headers)
    access_token = json.loads(token_request.text)["access_token"]
    return access_token

def request_valid_song(access_token, genre=None):
    # Wildcards for random search
    randomSongsArray = ['%25a%25', 'a%25', '%25a',
                        '%25e%25', 'e%25', '%25e',
                        '%25i%25', 'i%25', '%25i',
                        '%25o%25', 'o%25', '%25o',
                        '%25u%25', 'u%25', '%25u']
    randomSongs = random.choice(randomSongsArray)
    # Genre filter definition
    if genre:
        genreSearchString = " genre:'{}'".format(genre)
    else:
        genreSearchString = ""
    # Upper limit for random search
    maxLimit = 10000
    while True:
        try:
            randomOffset = random.randint(1, maxLimit)
            authorization_header = {
                "Authorization": "Bearer {}".format(access_token)
            }
            song_request = requests.get(
                "{}/search?query={}&offset={}&limit=1&type=track".format(
                    SPOTIFY_API_URL,
                    randomSongs + genreSearchString,
                    randomOffset
                ),
                headers=authorization_header
            )
            song_info = json.loads(song_request.text)['tracks']['items'][0]
            #print(song_info)
            artist = song_info['artists'][0]['name']
            song = song_info['name']
            song_id = song_info['id']
        except IndexError:
            if maxLimit > 1000:
                maxLimit = maxLimit - 1000
            elif maxLimit <= 1000 and maxLimit > 0:
                maxLimit = maxLimit - 10
            continue
        except KeyError:
            continue
        break
    return f"{artist},{song},{song_id}"#.format(artist, song, song_id)

raw_song_list = []
def get_random_songs(access_token):
    """Creating a list of random songs"""
    while len(raw_song_list) < 20000:
        s = request_valid_song(f'{access_token}', genre= None)
        s_info = s.split(",")
        raw_song_list.append(s_info)
        time.sleep(.5)
    return raw_song_list

random_song_list = []
def parse_list(list):
    """Collecting the data and parsing the random songs from a list containing the ids"""
    for s in tqdm(list):
        aud_feats = sp.audio_features(f'spotify:track:{s[2]}')
        aud_feats = aud_feats[0]
        track_info = sp.track(f'spotify:track:{s[2]}')
        art=track_info['artists'][0]['uri']
        art_info = sp.artist(art)
        sample_dict = {'SongID':f'{s[1]}{s[0]}', 
                       'Performer':s[0], 
                       'Song':s[1], 
                       'spotify_genre': art_info['genres'], 
                       'spotify_track_id':s[2],
                       'spotify_track_preview_url':track_info['preview_url'], 
                       'spotify_track_album':track_info['album']['name'],
                       'spotify_track_explicit':track_info['explicit'], 
                       'spotify_track_duration_ms':aud_feats['duration_ms'],
                       'spotify_track_popularity':track_info['popularity'], 
                       'danceability':aud_feats['danceability'], 
                       'energy':aud_feats['energy'], 
                       'key':aud_feats['key'], 
                       'loudness':aud_feats['loudness'],
                       'mode':aud_feats['mode'], 
                       'speechiness':aud_feats['speechiness'], 
                       'acousticness':aud_feats['acousticness'], 
                       'instrumentalness':aud_feats['instrumentalness'], 
                       'liveness':aud_feats['liveness'],
                       'valence':aud_feats['valence'], 
                       'tempo':aud_feats['tempo'], 
                       'time_signature':aud_feats['time_signature']}
        random_song_list.append(sample_dict)
        time.sleep(.300)
    return random_song_list