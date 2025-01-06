from yt_dlp_handler import download_video

def main():
    video_url = input("Enter Youtube Video URL: ")
    save_directory = input("Enter the directory to save the video: ")
    download_video(video_url, save_directory)

if __name__ == "__main__":
    main()