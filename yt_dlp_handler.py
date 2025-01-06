import yt_dlp

def download_video(url, save_path):
    try:
        ydl_opts = {
            "outtmpl": save_path + "/%(title)s.%(ext)s" #save the video with the title as the filename
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Title: {info_dict.get("title", "Unknown title")}")
            print(f"Video downloaded successfully to {save_path}")
        
    except Exception as e:
        print(f"Error: {e}")