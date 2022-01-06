This repository is a modification of Google Brain AutoML found at https://github.com/google/automl/tree/master/efficientdet

# Purpose
The objective of this API is to provide the name of the objects that are recognized in an image which path is provided via http GET request as a parameter but it is stored in Firebase. This API that can help developers use this machine learning model for their web application projects without the hassle of figuring out how AutoML/EfficientDet works. 

This API was used in a dating app project, where given the profile pictures of the users the efficientdet network could identify their interests and match users with like minded individuals. 

# How it works?

# How to run?

cd automl
flask run
firebase

# Walkthrough
<img src="ObjectRecognition.gif"/>

Authors: Paulina Acosta, Usman Tariq

Note this project works with Firebase, hence https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/