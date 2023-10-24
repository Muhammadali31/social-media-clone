import pyrebase
from firebase_conf_ref import firebaseConf

# SET UP FIREBASE
firebase = pyrebase.initialize_app(firebaseConf)

# CONNECT TO DATA BASE
db = firebase.database()


# SENDING POST TO FB
def send_post(msg):
    post = {"message" : msg}
    try:
        db.child("rec_msg").update({"message" : msg})
        return 1
    except:
        return 0
