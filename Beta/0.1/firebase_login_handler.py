import pyrebase

# SETTING UP FIREBASE
firebaseConf={'apiKey': "YOUR API KEY",
    'authDomain': "YOUR FIREBASE DOMAIN",
    'databaseURL': "YOUR FIREBASE URL",
    'projectId': "YOUR FIREBASE PROJECT ID",
    'storageBucket': "YOUR FIREBASE PROJECT BUCKET",
    'messagingSenderId': "YOUR SENDER ID",
    'appId': "YOUR FIREBASE APP ID"}

# CONNECTING TO FIREBASE
firebase = pyrebase.initialize_app(firebaseConf)
auth = firebase.auth()

# Sign Up Function
def sign_up(email, password):
    # SENDING DATA OF TO FB
    try: # CHECKING IF THE EMAIL IS ALREADY THERE
        create_user = auth.create_user_with_email_and_password(email,password)
        return 1
    except: # IF EMAIL IS ALREADY THERE THEN
        return 0

# LOGIN FUNCTION
def login(email, password):
    # SENDING EMAIL&PASSWORD TO FB
    try: # CHECKING IF IT IS CORRECT
        check_user = auth.sign_in_with_email_and_password(email,password)
        return 1
    except: # IF THE EMAIL OR PASSWORD IS WRONG
        return 0
