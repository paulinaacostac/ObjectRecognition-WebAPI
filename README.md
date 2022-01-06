This repository is a modification of Google Brain AutoML found at https://github.com/google/automl/tree/master/efficientdet

# Purpose
The objective of this API is to provide the name of the objects that are recognized in an image which path is provided via http GET request as a parameter but it is stored in Firebase. This API that can help developers use this machine learning model for their web application projects without the hassle of figuring out how AutoML/EfficientDet works. 

This API was used in a dating app project, where given the profile pictures of the users the efficientdet network could identify their interests and match users with like minded individuals. 

# How it works?
This web API manages inputs and outputs with HTTP GET requests. The developer should wrap the users image path in an URL in the following way:

```
http://localhost:5000/?profilePic=[url to image stored in firebase]

```
Example:

```
http://localhost:5000/?profilePic=test1/surfboarding
```

# How to run?

1. First open the project in your favorite IDE

2. You will need to download the data model for efficientdet d4, which can be found in Google original repo: https://github.com/google/automl/tree/master/efficientdet

3. You will need to install the Firebase APIs and download your own account credentials https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/

3. Change directory to the automl folder using: 
```
cd automl
```

4. Execute the python script where the flask API runs (app.py) using this command
```
flask run
```
You can use other parameters as --port or --host to modify the default deployed port which is 5000

3. Wait until the API is running and test URL by executing an HTTP GET request with Postman or your favorite browser.

```
http://localhost:5000/?profilePic=[url to image stored in firebase]

```


# Walkthrough
<img src="ObjectRecognition.gif"/>

Authors: Paulina Acosta, Usman Tariq

