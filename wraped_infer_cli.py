import os
import sys

now_dir = os.getcwd()
sys.path.append(now_dir)


# from dotenv import load_dotenv
from scipy.io import wavfile

sys.path.append("./RVC")
from configs.config import Config
from infer.modules.vc.modules import VC


def wraped_infer_cil(f0up_key, input_path, index_path, opt_path, model_name, index_rate=0.66, f0method="rmvpe", device="cuda:0", is_half=True, filter_radius=3, resample_sr=0, rms_mix_rate=0, protect=0):
    # load_dotenv()
    if os.path.exists(opt_path):
        os.remove(opt_path)
    config = Config()
    config.device = device if device else config.device
    config.is_half = is_half if is_half else config.is_half
    vc = VC(config)
    vc.get_vc(model_name)
    _, wav_opt = vc.vc_single(
        0,
        input_path,
        f0up_key,
        None,
        f0method,
        index_path,
        None,
        index_rate,
        filter_radius,
        resample_sr,
        rms_mix_rate,
        protect,
    )
    wavfile.write(opt_path, wav_opt[0], wav_opt[1])


if __name__ == "__main__":
    wraped_infer_cil(f0up_key=0, input_path="audio/test.wav", index_path="logs/test.index", opt_path="audio/test.wav", model_name="test.pth")
