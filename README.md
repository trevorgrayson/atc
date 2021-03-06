ATC Transcription
=================

Setup
=====

```
    pip install -r requirements.txt
```

First make a dictionary by putting words into the lexicon file. 
These words will be broken into their phonetics.

```
    ./read_word_list.sh
```

You need a model around a language (english) and then the model
will try to match to words by the phonetics.  You can train
the dictionary to get improved results.  This process can be as
involved as you want for better results.

  * lots of parameters are available. depth, size, num_layers, decay rate.
  * can put in a valid dataset or a test dataset
  * can rewrite the model from scratch

```
    ./train_dictionary.sh
```

Next get a sound file you want to transcribe.  ffmpeg should be
able to figure out mp4, wav, etc. This is hardcoded to output 
a proper formatted bitrate file into `subject.wav.`

```
    ./convert_wav.sh your_file.wav
    # outputs subject.wav
```

Next, lets see what the hell this does.

```
    python decode_wav.py
```

This takes a long ass time.  I think the script has to load the whole file and 
THEN start spitting stuff out.  If you look at pocket-inter.py it has sample code.
It's not using the avaiation dict and I think that's connected to a microphone.
Probably should use something like this but take a file cat'ed into it.

Default model found in:
.venv/sphinx/lib/python2.7/site-packages/pocketsphinx/model/en-us
