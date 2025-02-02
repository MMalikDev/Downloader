# Video Downloader

A simple video downloader using PyTube, designed for ease of use across multiple platforms.
This project provides three methods of execution: via Docker, locally with Python, or as an executable (exe).

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Docker Execution](#docker-execution)
  - [Local Python Execution](#local-python-execution)
  - [Executable Creation](#executable-creation)
- [Windows Shortcuts](#windows-shortcuts)
- [Additional Information](#additional-information)
- [Disclaimer](#disclaimer)

## Getting Started

### Prerequisites

To run this project, you need either of the following setups:

- Python 3 (recommended: dev version ≥ 3.6) and FFmpeg binary installed

  - [Download Python](https://docs.docker.com/engine/install/)

  - [Download FFmpeg](https://ffmpeg.org/)

OR

- Docker installed

  - [Install Docker](https://docs.docker.com/engine/install/)

### Docker Execution

1. Run the project inside a Docker container:

   ```bash
   bash run.sh -c
   ```

1. To download a video, replace 'URL' below with the desired url:

   ```bash
   bash run.sh -r URL
   ```

> **Note**: When using Windows, utilize WSL to prevent issues with the "cp_docker" command

### Local Python Execution

1. Initialize local environment & activate venv:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

1. Install dependencies:

   ```bash
   pip install -r src/requirements/core.txt  # Alternative if errors occur: versions.txt
   ```

1. Initiate the project with a provided link:

   ```bash
   bash run.sh -l URL
   ```

### Executable Creation

1. Ensure Python is accessible in your PATH.

   You may need to add its installation folder to the System Environment Variables.

1. Generate the executable by executing:

   ```bash
   bash run.sh -e
   ```

This process compiles the source code into standalone .exe file suitable for deployment without requiring external libraries.

### Windows Shortcuts

Two .bat files have been prepared for Windows users:

- **'Execute.bat'** will launch the exe file
- **'Download.bat'** will run the Python script

## Additional Information

To get additional help or information, you can use the following command:

```bash
bash run.sh -h
```

This will display a help message that provides more details on how to use the **'run.sh'** script.

## Disclaimer

This video downloader is for demonstration purposes only and is not meant for pirating content from the web. We do not condone or encourage illegal downloading of copyrighted material.

Any unauthorized downloading and sharing of copyrighted material is illegal and can result in civil and criminal penalties. Please use this downloader responsibly and respect copyright laws.

By using this tool, you agree that you will only use it for legal purposes and will not use it to infringe on anyone's intellectual property rights. If you choose to download copyrighted material using this tool, you do so at your own risk and we are not liable for any consequences that may arise.
