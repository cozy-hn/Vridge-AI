# firebase_init.py
import firebase_admin
import os
from firebase_admin import credentials, storage

def initialize_firebase():
    try:
        return firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate('/home/jhko2721/vridge/vridge-5f526-firebase-adminsdk-1vq62-7e7a7d4a58.json')
        return firebase_admin.initialize_app(cred, {
            'storageBucket': 'vridge-5f526.appspot.com'
        })

def download_model_if_not_exists(path):
    if os.path.exists(path):
        print("Model already exists locally. Skipping download.")
        return

    print("Downloading model from Firebase Storage...")
    bucket = storage.bucket()
    blob = bucket.blob(path)
    blob.download_to_filename(path)
    print(f"Model downloaded to local {path}.")

if __name__ == "__main__":
	pass