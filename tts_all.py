import os
from contextlib import contextmanager
from tts_wav import make_tts_wav
from wraped_infer_cli import wapred_infer_cil
import argparse
from dotenv import load_dotenv

@contextmanager
def temporary_env_var(key, value):
    original_value = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if original_value is None:
            raise ValueError(f"환경 변수 '{key}'가 원래 설정되어 있지 않습니다.")
        else:
            os.environ[key] = original_value

def tts_all(tts, uid, vid, ttsid, pitch):
    load_dotenv()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Vridge\\vridge-5f526-146273e2ebf7.json"
    defalut_path = "C:/Vridge/test_db"
    tts_wav_path = defalut_path + "/" + uid + "/" + vid + "/" + ttsid + "_tts"
    converted_wav_path = defalut_path + "/" + uid + "/" + vid + "/" + ttsid + ".wav"
    model_name = vid + ".pth"
    model_path = defalut_path + "/" + uid + "/" + vid
    index_path = defalut_path + "/" + uid + "/" + vid + "/" + vid + ".index"
    make_tts_wav(tts, tts_wav_path)
    tts_wav_path+=".wav"
    with temporary_env_var("weight_root", model_path):
        with temporary_env_var("index_root", model_path):
            wapred_infer_cil(f0up_key=pitch, input_path=tts_wav_path, index_path=index_path, opt_path=converted_wav_path, model_name=model_name)
    os.remove(tts_wav_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text to speech")
    parser.add_argument("--tts", type=str, help="text to be converted to speech", required=True)
    parser.add_argument("--uid", type=str, help="name of the user model to be used", required=True)
    parser.add_argument("--vid", type=str, help="name of the voice model to be used", required=True)
    parser.add_argument("--ttsid", type=str, help="model to be used for the tts", required=True)
    parser.add_argument("--pitch", type=int, help="pitch of the voice", default=0)
    args = parser.parse_args()
    tts_all(args.tts, args.uid, args.vid, args.ttsid, args.pitch)