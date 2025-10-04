import os
import warnings
import sounddevice as sd
from scipy.io.wavfile import write
from speechbrain.pretrained import SpeakerRecognition
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

REFERENCE_FILE = "speech.wav"   
USER_FILE = "user_input.wav"
def record_audio(filename=USER_FILE, duration=5, fs=16000):
    try:
        print(f"Recording for {duration} seconds Speak now!")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        write(filename, fs, recording)
        print(f"Recording saved as {filename}")
    except Exception as e:
        print(f"Error recording audio: {e}")
        return False
    return True
def main():
    print("Voice Comparison Script\n")
    if not os.path.exists(REFERENCE_FILE):
        print(f"Reference file '{REFERENCE_FILE}' not found in the current folder.")
        return
    if not record_audio():
        print(" Recording failed. Exiting.")
        return
    try:
        print("\nLoading speaker recognition model")
        verify = SpeakerRecognition.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb",
            savedir="pretrained_models",
            run_opts={"local_strategy": "copy"}  
        )
    except Exception as e:
        print(f"Failed to load model: {e}")
        return
    try:
        score, prediction = verify.verify_files(REFERENCE_FILE, USER_FILE)
        if score is not None:
            print(f"\nSimilarity score: {float(score):.4f}")
        else:
            print("\nSimilarity score: N/A")
        if prediction:
            print(" Voices are the SAME.")
        else:
            print("Voices are DIFFERENT.")
    except Exception as e:
        print(f"Voice comparison failed: {e}")
if __name__ == "__main__":
    main()
