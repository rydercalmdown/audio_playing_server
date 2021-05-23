# Audio Playing Server
A simple raspberry-pi, python-based server that listens for requests and plays corresponding audio files.

## Install
To install, clone this repository on your pi, and run the install command:

```
# From a fresh raspbian-lite installation
sudo apt-get update && sudo apt-get install -y git
cd ~/
git clone https://github.com/rydercalmdown/audio_playing_server.git
cd audio_playing_server
make install
```

## Running
To run, use the run command:
```
make run
```

## Adding Audio Files
Add mp3 files to the audio directory and they'll show up as available options on the index route.
