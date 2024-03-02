import re

from pytube import Playlist, YouTube
from pytube.cli import on_progress

from lib.utilities import logger


# ---------------------------------------------------------------------- #
# Utility Functions
# ---------------------------------------------------------------------- #
def get_resolution(itag: int) -> str:
    resolutions = {
        18: "low ~360p",
        22: "medium ~720p",
        137: "high ~1080p",
        313: "very high ~2160p",
    }
    return resolutions.get(itag, "Undefined")


def download_playlist(location: str, url: str) -> None:
    p = Playlist(url)

    for video in p.videos:
        yd = video.streams.get_highest_resolution()
        logger.info("%s | Resolution: %s", video.title, get_resolution(yd.itag))
        yd.download(location)


def download_video(location: str, url: str) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    yd = yt.streams.get_highest_resolution()

    logger.info("%s | Resolution: %s", yt.title, get_resolution(yd.itag))
    yd.download(location)


# ---------------------------------------------------------------------- #
# Core Functions
# ---------------------------------------------------------------------- #
def download_media(location: str, url: str) -> None:
    VIDEO = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    PLAYLIST = r"(list=).*"

    validVideo = re.compile(VIDEO).search(url)
    isPlaylist = re.compile(PLAYLIST).search(url)

    if not validVideo and not isPlaylist:
        logger.warning("Invalid URL was provided")
        return
    if isPlaylist:
        logger.info("Downloading Playlist item(s)...")
        download_playlist(url=url, location=location)
    else:
        logger.info("Downloading Video...")
        download_video(url=url, location=location)

    logger.info("Download Complete - %s\n", location)
