from pytube import YouTube
from pytube.exceptions import LiveStreamError, RegexMatchError, VideoUnavailable

from datetime import timedelta

from video_audio.models import VideoInfo


def get_video_data(url):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    audio_stream = yt.streams.get_audio_only()

    data = {
        'title': yt.title,
        'length': str(timedelta(seconds=yt.length)),
        'video_url': video_stream.url,
        'resolution': video_stream.resolution,
        'audio_url': audio_stream.url,
        'abr': audio_stream.abr,
        'image': yt.thumbnail_url
    }

    return data


def check_exceptions(url):
    try:
        data = get_video_data(url)
    except LiveStreamError:
        return {'exception': ['Вы ввели ссылку на трансляцию']}
    except RegexMatchError:
        return {'exception': ['Ошибка соответствия регулярного выражения']}
    except VideoUnavailable:
        return {'exception': ['Видео недоступно']}

    return data


def check_user_id(data, user):

    if user.id:
        data['user'] = user
        VideoInfo.objects.create(**data)
