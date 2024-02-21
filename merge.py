from RVC.infer.lib.train.process_ckpt import merge
import argparse
from firebase_util import initialize_firebase, download_model_if_not_exists, upload_file_to_firebase
import os

# def merge(path1, path2, alpha1, sr, f0, info, path3, version):
def start_merge():
    defalut_path = "/home/jhko2721/vridge/Database/"
    path1 = f"{args.uid1}/{args.vid1}/{args.vid1}.pth"
    path2 = f"{args.uid1}/{args.vid2}/{args.vid2}.pth"
    path3 = f"{args.uid1}/{args.vid3}/{args.vid3}.pth"
    index3 = f"{args.uid1}/{args.vid3}/{args.vid3}.index"
    download_model_if_not_exists(f"{defalut_path}{path1}", f"{defalut_path}{path1}.index", args.uid1, args.vid1)
    download_model_if_not_exists(f"{defalut_path}{path2}", f"{defalut_path}{path2}.index", args.uid1, args.vid2)
    download_model_if_not_exists(f"{defalut_path}{path3}", f"{defalut_path}{path3}.index", args.uid1, args.vid3)
    merge(f"{defalut_path}{path1}", f"{defalut_path}{path2}", args.alpha1, args.sr, args.f0, args.info, f"{defalut_path}{path3}", args.version)
    os.copy(f"{defalut_path}{path1[:-4]}.index", f"{defalut_path}{index3}")
    upload_file_to_firebase(f"{defalut_path}{path3}", path3)
    upload_file_to_firebase(f"{defalut_path}{index3}", index3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge two models')
    parser.add_argument('uid1', type=str, help='UID1')
    parser.add_argument('vid1', type=str, help='VID1')
    parser.add_argument('vid2', type=str, help='VID2')
    parser.add_argument('vid3', type=str, help='VID3')
    parser.add_argument('--alpha1', type=float, help='Alpha1', default=0.5) #알파 0.5로 고정
    parser.add_argument('--sr', type=int, help='Sample rate', default="48K") #샘플링 레이트 "48K"로 고정
    parser.add_argument('--f0', type=int, help='F0', default=1) #F0 1로 고정
    parser.add_argument('--info', type=str, help='Info', default="")
    parser.add_argument('--version', type=int, help='Version', default="v2") #모델 버전
    args = parser.parse_args()
    initialize_firebase()
    start_merge()