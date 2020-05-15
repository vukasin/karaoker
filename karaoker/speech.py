import datetime
from pocketsphinx import AudioFile
from pocketsphinx import Pocketsphinx, get_model_path, get_data_path
import os
import sys
import tempfile
import fuzzy
from .phonetic import *
from pydub import AudioSegment
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

sound = AudioSegment.from_mp3(os.path.expanduser(
    "~/Music/karaoker/output/Bryan Ferry - These Foolish Things [Official]/vocals.mp3"))
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)
# sound.set_frame_rate()
sound.export("raw.raw",  format="raw")
sound.export("raw.wav",  format="wav")

# sound._data is a bytestring
raw_data = sound._data

model_path = get_model_path()

fps = 100
# Create a decoder with certain model
config = {
    'verbose': False,
    'audio_file': 'raw.wav',
    'buffer_size': 2048,
    'no_search': False,
    # "samprate": 16000,
    "sampling_rate": 16000,
    "frate": fps,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': "1790.lm",
    'dict': "1790.dic"
    # 'lm': os.path.join(model_path, 'en-us.lm.bin'),
    # 'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}
audio = AudioFile(**config)
print(os.path.join(model_path, 'en-us'))
model = make_model(open("lyrics.txt").read(), 8)
with open("test.lrc", "w") as out:
    for phrase in audio:  # frate (default=100)
        """
        print('-' * 28)
        print('| %5s |  %3s  |   %4s   |' % ('start', 'end', 'word'))
        print('-' * 28)
        """
        times = []
        line = []
        for s in phrase.seg():
            if s.word.startswith("<"):
                continue
            start = s.start_frame / fps
            end = s.end_frame / fps
            if not (line):
                line.append("[%02d:%02d.%02d]%s" % (
                    int(start) // 60, int(start) % 60, (100 * start) % 100, s.word))
            else:
                line.append("<%02d:%02d.%02d>%s" % (
                    int(start) // 60, int(start) % 60, (100 * start) % 100, s.word))

        #(score, corrected_phrase) = find_best_match(str(phrase), model)

        print(" ".join(line),
              file=out, end="\r\n")

    #print(start, corrected_phrase, end)

    # for s in phrase.seg():
    #    print(s.word)
    """
        print('| %4ss | %4ss | %8s |' %
              (s.start_frame / fps, s.end_frame / fps, s.word))
        """
    #print('-' * 28)
