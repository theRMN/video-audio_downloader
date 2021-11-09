from pytube import YouTube
import datetime


def youtube_downloader(url):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    audio_stream = yt.streams.get_audio_only()

    data = {
        'title': yt.title,
        'length': str(datetime.timedelta(seconds=yt.length)),
        'url': video_stream.url,
        'video_type': video_stream.mime_type,
        'audio': audio_stream.url,
        'audio_type': audio_stream.mime_type
    }

    return data
