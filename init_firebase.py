# firebase_init.py
import firebase_admin
from firebase_admin import credentials, storage

def initialize_firebase():
    try:
        return firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate('/home/jhko2721/vridge/vridge-5f526-firebase-adminsdk-1vq62-7e7a7d4a58.json')
        return firebase_admin.initialize_app(cred, {
            'storageBucket': 'vridge-5f526.appspot.com'
        })

if __name__ == "__main__":
	initialize_firebase()