import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Audio Inference Script')
parser.add_argument('--transpose', type=int, default=-12, help='Pitch transpose value')
parser.add_argument('--input_path', type=str, default='audio/output_korean.wav', help='Input audio file path')
parser.add_argument('--index_path', type=str, default='logs/jiheun/added_IVF316_Flat_nprobe_1_jiheun_v2.index', help='Index file path')
parser.add_argument('--output_path', type=str, default='audio/cli_output.wav', help='Output audio file path')
parser.add_argument('--model_name', type=str, default='jiheun.pth', help='Model file name')
parser.add_argument('--index_rate', type=float, default=0.66, help='Index rate')
parser.add_argument('--volume_normalization', type=float, default=0, help='Volume normalization rate')
parser.add_argument('--consonant_protection', type=float, default=0, help='Consonant protection rate')
parser.add_argument('--f0_method', type=str, default='rmvpe', choices=['rmvpe', 'pm', 'harvest'], help='F0 estimation method')
args = parser.parse_args()



os.chdir("C:\\Users\\jhk27\\OneDrive\\바탕 화면\\Vridge\\KiwKiw")

if not os.path.exists(args.input_path):
    raise ValueError(f"{args.input_path} was not found in your RVC folder.")
if not os.path.exists(args.index_path):
    print(f"{args.index_path} was not found in your RVC folder.")

if os.path.exists(args.output_path):
    os.remove(args.output_path)

command = f"python tools\\infer_cli.py --f0up_key {args.transpose} " \
          f"--input_path {args.input_path} " \
          f"--index_path {args.index_path} " \
          f"--f0method {args.f0_method} " \
          f"--opt_path {args.output_path} " \
          f"--model_name {args.model_name} " \
          f"--index_rate {args.index_rate} " \
          f"--device cuda:0 " \
          f"--is_half True " \
          f"--filter_radius 3 " \
          f"--resample_sr 0 " \
          f"--rms_mix_rate {args.volume_normalization} " \
          f"--protect {args.consonant_protection}"

subprocess.run(command, shell=True, check=True)