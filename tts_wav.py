from google.cloud import texttospeech
from pydub import AudioSegment
import os
import argparse

def make_tts_wav(tts="안녕하세요, 여러분 반가워요!",path="output_korean"):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=tts)

    # 음성 설정
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        name="ko-KR-Neural2-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # 오디오 설정
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16  # WAV 파일 형식
    )

    # TTS 요청 및 응답
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # 음성 파일로 임시 저장
    temp_filename = "temp_"+path+".wav"
    with open(temp_filename, "wb") as out:
        out.write(response.audio_content)

    # 무음 구간 추가
    sound = AudioSegment.from_wav(temp_filename)
    silence = AudioSegment.silent(duration=300)  # ms
    final_sound = silence + sound + silence 

    # 최종 음성 파일로 저장
    final_sound.export(path+".wav", format="wav")
    os.remove(temp_filename)
    print("TTS 완료 : "+path+".wav")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text to speech")
    parser.add_argument("--tts", type=str, help="text to be converted to speech")
    args = parser.parse_args()
    if args.tts:
        make_tts_wav(args.tts)
    else:
        print("text : 안녕하세요, 여러분 반가워요!")
        make_tts_wav()
