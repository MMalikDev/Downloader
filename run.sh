#!/bin/bash

# set -e

source ./scripts/run.sh
# ---------------------------------------------------------------------- #
# Define Docker Variables
# ---------------------------------------------------------------------- #
declare -a reloads=(
    python
)

declare -a logs=(
    python
)

# ---------------------------------------------------------------------- #
# Options
# ---------------------------------------------------------------------- #
remote_download(){
    local url=${1:-@}
    local source=$(get_env MEDIA)
    docker exec -it python python3 main.py $url
    cp_docker python $source .
    exit 0
}
run_devcontainer(){
    local url=${1:-@}
    run_python_dev $url
    exit 0
}
run_locally(){
    local url=${1:-@}
    run_python $url
    exit 0
}
run_docker(){
    reload_services ${reloads[*]}
    handle_errors $?
    
    docker image prune -f
    # follow_logs ${logs[*]}
    
    remote_download
    exit 0
}
create_exe() {
    printf "\n$icon_start Creating executable file for main.py\n\n"
    source .venv/Scripts/activate
    cd src/
    pyinstaller -F main.py -n Downloader --distpath ../dist --specpath ../dist
    exit 0
}

use_env_file(){
    [[ $(get_bool DEVCONTAINER) == "true" ]] && run_devcontainer
    [[ $(get_bool RUN_LOCAL) == "true" ]] && run_locally
    run_docker
}

# ---------------------------------------------------------------------- #
# Main Function
# ---------------------------------------------------------------------- #
main(){
    while getopts "d:l:cr:eh" OPTION; do
        case $OPTION in
            d) run_devcontainer $OPTARG ;;
            l) run_locally $OPTARG      ;;
            c) run_docker               ;;
            r) remote_download $OPTARG  ;;
            e) create_exe               ;;
            h) display_usage            ;;
            ?) display_usage            ;;
        esac
    done
    shift $((OPTIND -1))
    
    use_env_file
}

main $@
