from questionnaire import start_questionnaire
from video_generator import generate_video

def main():
    def on_complete(script):
        print(f"Generated script: {script}")
        audio_file_path = "background_audio.mp3"
        output_path = "personalized_financial_advice.mp4"
        print(generate_video(script, audio_file_path, output_path))

    start_questionnaire(on_complete)

if __name__ == "__main__":
    main()
