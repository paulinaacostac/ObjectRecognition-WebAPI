from flask import Flask
import urllib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import datetime
import os
from flask import request
app = Flask(__name__)
global appF
appF = None

def detectObjects():
    objects = []
    os.system('python .\\tutorial.py')
    f = open(".\\classesToWords.txt","r")
    strClasses = f.read()
    strClasses = strClasses[1:-1]
    objects = strClasses.split(', ')
    for i in range(len(objects)):
        objects[i] = objects[i].strip('\'')
    f.close()
    return ','.join(objects)


@app.route('/', methods=['GET', 'POST'])
def retrieveImage():
    global appF
    profilePic = request.args.get('profilePic')
    # Fetch the service account key JSON file contents
    if appF is None:
        cred = credentials.Certificate("credentials.json")

        # Initialize the app with a service account, granting admin privileges
        appF = firebase_admin.initialize_app(cred, {
            'storageBucket': 'aisparkdev-tinder.appspot.com',
        }, name='storage')


    bucket = storage.bucket(app=appF)
    #profilePic = "7gRyAHFRtKOks3BgFOn051SU6dE2/blackwidow1"
    blob = bucket.blob("profileImages/"+profilePic+".jpg")
    urllib.request.urlretrieve(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'), ".\\img.png")
    objects = detectObjects()
    return objects

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=105)
    