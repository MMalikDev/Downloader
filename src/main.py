import sys

from lib.download import download_media
from lib.utilities import debug, load_variable, logger


@debug
def main() -> None:
    VIDEO = "v="
    DEFAULT = "@"

    ID = load_variable("ID")
    LOCATION = load_variable("LOCATION", "downloads")

    if not sys.argv[1:]:
        logger.info("Type %s to download: %s", DEFAULT, VIDEO + ID)
        logger.warning("No URL was provided\n")
        return

    URL = VIDEO + ID if sys.argv[1] == DEFAULT else sys.argv[1]
    download_media(location=LOCATION, url=URL)


if __name__ == "__main__":
    main()
