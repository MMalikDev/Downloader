import re

import yt_dlp

from lib.utilities import logger


def download_media(location: str, url: str) -> None:
    VIDEO = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    PLAYLIST = r"(list=).*"
    URLS = [url]

    options = {}
    validVideo = re.compile(VIDEO).search(url)
    isPlaylist = re.compile(PLAYLIST).search(url)

    if not validVideo and not isPlaylist:
        logger.warning("Invalid URL was provided")
        return



    options = {
        "quiet": True,
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "".join([location + "/%(title)s.%(ext)s"]),
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(URLS)

    logger.info("Download Complete - %s\n", location)
