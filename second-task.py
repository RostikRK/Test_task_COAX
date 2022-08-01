from TikTokApi import TikTokApi
import requests
from moviepy.editor import VideoFileClip
import os

def extract_video_id_from_url(url, headers={}):
    url = requests.head(url=url, allow_redirects=True, headers=headers).url
    #gets an id
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )


def download_video(url):
    #reads video into bytes to have ability to write it
    video_bytes = TikTokApi().video(id=extract_video_id_from_url(url=url)).bytes()

    # Saving The Video
    with open('saved_video.mp4', 'wb') as output:
        output.write(video_bytes)

def video_to_gif(dir, name):
    videoClip = VideoFileClip(dir)
    videoClip.write_gif(name + ".gif")
    videoClip.close()
    filename = '\\' + name + ".gif"
    return "File was saved to: " + os.getcwd() + filename

def gif_from_url(url):
    print("Downloading started...")
    download_video(url)
    print("Downloading finished")
    while True:
        name = input("Please set the name of file:")
        if name == "":
            continue
        else:
            break
    print("Converting started...")
    final_dir = video_to_gif("saved_video.mp4", name)
    os.remove("saved_video.mp4")
    print("Congratulations! " + final_dir)


if __name__=="__main__":
    gif_from_url("https://www.tiktok.com/@y0ur.l0cal.ga1/video/7086578569471642886?is_from_webapp=1&sender_device=pc&web_id=7126970375594542598")
