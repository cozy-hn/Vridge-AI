import firebase_admin
import os
import subprocess
from firebase_admin import credentials, storage
import shutil

def initialize_firebase():
    try:
        return firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate('/home/jhko2721/vridge/vridge-5f526-firebase-adminsdk-1vq62-7e7a7d4a58.json')
        return firebase_admin.initialize_app(cred, {
            'storageBucket': 'vridge-5f526.appspot.com'
        })
        
def download_files_from_firebase(uid, vid, local_directory):
    app = firebase_admin.get_app()  # Firebase 앱 인스턴스 가져오기
    bucket = storage.bucket(app=app)
    
    # 버킷 내의 특정 경로 설정
    directory = f'{uid}/{vid}/train'
    blobs = bucket.list_blobs(prefix=directory)  # 해당 경로에 있는 모든 객체 목록 가져오기
    
    for blob in blobs:
        # 로컬 저장 경로에 사용자 지정 경로 추가
        file_path = os.path.join(local_directory, blob.name)
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))  # 필요한 디렉토리 생성
        blob.download_to_filename(file_path)  # 파일을 로컬 경로에 다운로드
        print(f'Downloaded {file_path}')
        

def convert_m4a_to_wav(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.m4a'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename.replace('.m4a', '.wav'))

            command = [
                'ffmpeg',
                '-i', input_file,        # 입력 파일
                '-acodec', 'pcm_s16le',  # WAV 오디오 코덱
                '-ar', '44100',          # 오디오 샘플 레이트
                output_file,              # 출력 파일
                '-y'
            ]
            # 표준 출력 및 에러 억제
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f'Converted {input_file} to {output_file}')

            # 원본 파일 삭제
            os.remove(input_file)
            print(f'Removed original file: {input_file}')

    shutil.rmtree(input_directory)
    print(f'Deleted directory: {input_directory}')

initialize_firebase()
download_files_from_firebase('oQi6Gm6sHfYyOOZsnBDCSbbPmUz1', '467cb22b4e274498962e6e72392cb411', '/home/jhko2721/vridge/Database')
input_dir = '/home/jhko2721/vridge/Database/oQi6Gm6sHfYyOOZsnBDCSbbPmUz1/467cb22b4e274498962e6e72392cb411/train'
output_dir = '/home/jhko2721/vridge/Database/oQi6Gm6sHfYyOOZsnBDCSbbPmUz1/467cb22b4e274498962e6e72392cb411'
convert_m4a_to_wav(input_dir, output_dir)
