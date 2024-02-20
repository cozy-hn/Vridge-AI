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

def download_model_if_not_exists(model_path, index_path, uid, vid):
    if os.path.exists(model_path) and os.path.exists(index_path):
        print("Model already exists locally. Skipping download.")
        return

    model_dir = os.path.dirname(model_path)
    index_dir = os.path.dirname(index_path)
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
        
    print("Downloading model from Firebase Storage...")
    bucket = storage.bucket()
    blob_pth = bucket.blob(f"{uid}/{vid}/{vid}.pth")
    blob_index = bucket.blob(f"{uid}/{vid}/{vid}.index")
    blob_pth.download_to_filename(model_path)
    blob_index.download_to_filename(index_path)
    print("Model downloaded to local.")

if __name__ == "__main__":
	pass