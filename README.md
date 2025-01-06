# yt_downloader

**yt_downloader** is a simple Python script that allows users to download YouTube videos. It uses the `yt-dlp` library to fetch and download videos from YouTube to a specified local directory.
## Features
- Downloads YouTube videos by providing a URL.
- Saves the downloaded video in your specified directory with the video title as the filename.

## Requirements

To run the `yt_downloader`, you need:
- Python 3.x installed on your system.
- The `yt-dlp` library to handle video downloading.

### Install Dependencies
To install the required dependencies, run the following command:

```bash
pip install yt-dlp

How to Use1. Clone the RepositoryFirst, clone the repository or download the code to your local machine:bashCopy codegit clone https://github.com/acube25/yt\_downloader.git2. Run the ScriptNavigate to the directory where the main.py file is located and run the script:bashCopy codepython main.py3. Enter Video URL and DirectoryThe script will prompt you to enter the following:YouTube video URL: Enter the URL of the YouTube video you want to download.Directory to save the video: Enter the path to the folder where the video will be saved.After entering this information, the video will be downloaded automatically.Example Output:mathematicaCopy codeEnter Youtube Video URL: https://www.youtube.com/watch?v=XXXXXXEnter the directory to save the video: /path/to/directoryVideo downloaded successfully to /path/to/directoryFile StructureThe project has the following structure:bashCopy codeyt\_downloader/├── main.py # Main script that handles user input and calls the download function├── yt\_dlp\_handler.py # Contains the logic to handle video downloading using yt-dlp├── README.md # This file└── \_\_init\_\_.py # Optional, marks the directory as a Python packageHow It Worksmain.py: Prompts the user for the YouTube video URL and the save directory, and calls the download function.yt\_dlp\_handler.py: Handles the actual downloading process using yt-dlp, saving the video with the title as the filename in the specified directory.please make it to markdown language

## How to Use
### 1. Clone the Repository
First, clone the repository or download the code to your local machine:
```bash
git clone https://github.com/acube25/yt_downloader.git
```
###  2. Run the Script
Navigate to the directory where the main.py file is located and run the script:

```bash
python main.py
```
###  3. Enter Video URL and Directory
The script will prompt you to enter the following:
- YouTube video URL: Enter the URL of the YouTube video you want to download.
- Directory to save the video: Enter the path to the folder where the video will be saved.
After entering this information, the video will be downloaded automatically.

### Example Output:
```mathmatica
Enter Youtube Video URL: https://www.youtube.com/watch?v=XXXXXX
Enter the directory to save the video: /path/to/directory
Video downloaded successfully to /path/to/directory
```
## File Structure
The project has the following structure:
```bash
yt_downloader/
├── main.py
├── yt_dlp_handler.py 
├── README.md  
└── __init__.py 
```

## How It Works
- `main.py`: Prompts the user for the YouTube video URL and the save directory, and calls the download function.
- `yt_dlp_handler.py`: Handles the actual downloading process using `yt-dlp`, saving the video with the title as the filename in the specified directory.

