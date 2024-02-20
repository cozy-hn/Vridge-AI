from KiwKiw.infer.lib.train.process_ckpt import merge
import argparse

# def merge(path1, path2, alpha1, sr, f0, info, name, version):
def main():
    parser = argparse.ArgumentParser(description='Merge two models')
    parser.add_argument('path1', type=str, help='Path to the first model')
    parser.add_argument('path2', type=str, help='Path to the second model')
    # parser.add_argument('alpha1', type=float, help='Alpha1') #모델 a,b의 가중치 0.5고정
    # parser.add_argument('sr', type=int, help='Sample rate') #샘플링 레이트 48K 고정
    # parser.add_argument('f0', type=int, help='F0') #음높이 1 고정
    # parser.add_argument('info', type=str, help='Info') #""
    parser.add_argument('name', type=str, help='Name') #저장할 모델 이름 
    # parser.add_argument('version', type=int, help='Version') #모델 버전 v2 고정
    args = parser.parse_args()
    merge(args.path1, args.path2, 0.5, "48K", 1, "", args.name, "v2")

if __name__ == '__main__':
    main()