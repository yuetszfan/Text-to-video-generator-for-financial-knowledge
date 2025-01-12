from questionnaire import start_questionnaire
from video_generator import generate_video

def main():
    def on_complete(script):
        print(f"Generated script: {script}")
        audio_file_path = "background_audio.mp3"  # Replace with actual audio file path
        output_path = "personalized_financial_advice.mp4"
        video_status = generate_video(script, audio_file_path, output_path)
        print(video_status)

    # Start the questionnaire and generate video based on responses
    start_questionnaire(on_complete)

if __name__ == "__main__":
    main()
