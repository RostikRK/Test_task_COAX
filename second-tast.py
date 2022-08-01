from TikTokApi import TikTokApi
import string
import random
import requests

def extract_video_id_from_url(url, headers={}):
    url = requests.head(url=url, allow_redirects=True, headers=headers).url
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )


#did=''.join(random.choice(string.digits) for num in range(19))
#verifyFp="verify_YOUR_VERIFYFP_HERE"
#api = TikTokApi.get_instance(custom_verifyFp=verifyFp, custom_did=did)

def download_video(url):
    video_bytes = TikTokApi().video(id=extract_video_id_from_url(url=url)).bytes()

    # Saving The Video
    with open('saved_video.mp4', 'wb') as output:
        output.write(video_bytes)


if __name__=="__main__":
    download_video("https://www.tiktok.com/@taniaveor/video/7116884739621014789?is_from_webapp=1&sender_device=pc")