import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import time

def download_video():
    destination = destination_entry.get()
    url = url_entry.get()
    
    yt_dlp_path = os.path.join(os.path.dirname(__file__), 'yt-dlp.exe')
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')
    command = f'"{yt_dlp_path}" -f bestvideo+bestaudio --merge-output-format mp4 --postprocessor-args "-c:a aac" --ffmpeg-location "{ffmpeg_path}" -o "{destination}/%(title)s.%(ext)s" {url}'
    
    subprocess.run(command, shell=True)

    update_file_modification_time(destination)

def update_file_modification_time(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.utime(file_path, (time.time(), time.time()))

def browse_destination():
    folder_selected = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, folder_selected)

root = tk.Tk()
root.title("YouTube Video Downloader")

destination_label = tk.Label(root, text="Destination Folder:")
destination_label.grid(row=0, column=0, padx=10, pady=10)

destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_destination)
browse_button.grid(row=0, column=2, padx=10, pady=10)

url_label = tk.Label(root, text="YouTube Video URL:")
url_label.grid(row=1, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=2, column=1, padx=10, pady=20)
version_label = tk.Label(root, text="v1.1.0\nMade by hyphenangel", font=("Helvetica", 10, "italic"))
version_label.grid(row=3, column=2, sticky="sw", padx=10, pady=10)

root.mainloop()
