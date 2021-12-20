from pytube import YouTube
from datetime import timedelta


def youtube_downloader(url):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    audio_stream = yt.streams.get_audio_only()

    data = {
        'title': yt.title,
        'length': str(timedelta(seconds=yt.length)),
        'video_url': video_stream.url,
        'resolution': video_stream.resolution,
        'audio_url': audio_stream.url,
        'abr': audio_stream.abr
    }

    return data


# print(youtube_downloader('https://www.youtube.com/watch?v=9qrE4i7b7zQ'))
