ARG VERSION=3.12-slim-bookworm
FROM python:$VERSION AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LOCATION=downloads
WORKDIR /code

RUN mkdir -p $LOCATION

# Install FFmpeg
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update  \
    && apt-get -y install ffmpeg

# Install dependencies
ARG DEPENDENCIES=requirements/core.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=$DEPENDENCIES,target=$DEPENDENCIES  \
    python3 -m pip install -r $DEPENDENCIES 

# ------------------------------------------------------------ #

FROM builder AS testing
COPY . .

CMD ["python3", "main.py"]
