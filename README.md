# Billboard_Song_Classification
This is a classification project with the goal of predicting if a song will be a Billboard Top 100 Hit.

# Technologies Used:
  - Spotify API
  - Spotipy
  - Pandas
  - Maplotlib
  - Seaborn
  - Scikit-learn
  
# Process:
A list of all Billboard Top 100 Hits was gathered going back to 1958. The analytical information of each song was compiled from Spotify. A function to generate random songs as well as their analytics was then created to pull a new collection of songs that did not make it on the Billboard chart. These two collections were then used to run the statistical tests.

# Models:
  - KNN
  - XGBoost
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Naive Bayes
  
  ![alt text](https://github.com/eharacz/Billboard_Song_Classification/blob/wip/Model_Results.png "Model Results")
  
  
# Final Model:
  - XGBoost
  ![alt text](https://github.com/eharacz/Billboard_Song_Classification/blob/wip/XGBoost_Confusion-Matrix.png "XGBoost Confusion Matrix")
  
# Future Improvements:
  - At the time of the intial model running there was a an uneven count of observations in the two classes. There was  approximately 23,000 Billboard Top 100 songs and approximately 7000 Non-Billboard songs. To deal with this, I used SMOTE to synthetically replicate more songs into the Non-Billboard category. More songs have been pulled and the tests can be re-run with more pure data.
  - There is a discrepancy in what was deemed by the tests as the most important feature, "Spotify Popularity Rating". Contrary to intuition, the Billboard category has a lower mean for this feature. After some exploration into the data I discovered this is due to the fact that my collection of Billboard songs date back to the late 1950s. Although these songs may have been big hits in their day they are generally not listened to much on Spotify currently. A cut off date on the Billboard songs can be used to deal with this issue. Below is a visual of their distributions:
![alt text](https://github.com/eharacz/Billboard_Song_Classification/blob/wip/Category_SpotPop_Distribution.png "Category Popularity Distributions")
