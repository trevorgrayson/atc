import os
import sys
from pocketsphinx import DefaultConfig, Decoder, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

# Create a decoder with a certain model
config = DefaultConfig()
config.set_string('-hmm', os.path.join(model_path, 'en-us'))
config.set_string('-lm', os.path.join(model_path, 'en-us.lm.bin'))
config.set_string('-dict', 'aviation.dict')
# set log level
#config.set_string("-logfn", "null")
decoder = Decoder(config)

# Decode streaming data
buf = bytearray(1024)

with open('subject.wav', 'rb') as f: #should be raw format with right timing
    decoder.start_utt()
    while f.readinto(buf):
        decoder.process_raw(buf, False, False)
    decoder.end_utt()
print('Best hypothesis segments:') 

for seg in decoder.seg():
    if not seg.word == '<sil>':
        sys.stdout.write(seg.word)
        sys.stdout.write(' ')
