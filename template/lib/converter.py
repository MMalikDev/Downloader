from pathlib import Path
from typing import Any, Generator

from moviepy import editor


def files_in_directory(directory: Path) -> Generator[Path, Any, None]:
    for child in directory.rglob("*"):
        if child.is_file() and child.suffix == ".mp4":
            yield child


def convert_to_mp3(video: str, audio: str) -> None:
    with editor.VideoFileClip(video) as file:
        file.audio.write_audiofile(audio)


def main() -> None:
    folder = "data/src"
    for video in files_in_directory(Path(folder)):
        audio = str(video).replace("src", "dist").replace(".mp4", ".mp3")
        Path(audio).parent.mkdir(parents=True, exist_ok=True)
        convert_to_mp3(str(video), audio)


if __name__ == "__main__":
    main()

"""
pip install moviepy
"""
