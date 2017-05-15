ffmpeg -i $1 -ac 1 -ar 16000 -minrate 16 -maxrate 16 -bits_per_raw_sample 16 subject.wav
