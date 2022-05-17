import soundfile as sf
import numpy as np
import os

# Setup hyper parameters
import hparams

# Inject frontend text processor
import synthesis
import train
from deepvoice3_pytorch import frontend

# Load Model Checkpoint
from train import build_model
from train import restore_parts, load_checkpoint

# Preprocess Text
from g2p_cw_rules import g2p_cw_rules
import re

# change the checkpoint path to change the model
preset = "deepvoice3_ljspeech.json"
checkpoint_path = "checkpoint_step000750000_Exp13.pth"

# Load parameters from preset
with open(preset) as f:
    hparams.hparams.parse_json(f.read())

synthesis._frontend = getattr(frontend, "en")
train._frontend = getattr(frontend, "en")

# aliases
fs = hparams.hparams.sample_rate
hop_length = hparams.hparams.hop_size

# Define Utility Functions
def tts(model, text, p=0, speaker_id=None, fast=True, figures=True):
    from synthesis import tts as _tts
    waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)
    waveform /= np.max(np.abs(waveform), axis=0)
    sf.write('flaskfiles/static/output.wav', waveform, fs, 'PCM_24')


model = build_model()
model = load_checkpoint(checkpoint_path, model, None, True)


# Enter the Sentence/word in Maltese into the string 'texts'
# text = "Jien jisimni Lijża, l-assistenta diġitali tiegħakk, u mil-lumm, għandi vuċi ġdida."
# text = "Dik il-ħabta l-uġigħ ta' rasijiet kienu fl-aqwa tagħhom"
# text = "Nistgħu ngħidu li diġà nafu niktbu sentenzi bil-Malti iżda f’din il-lezzjoni se nitgħallmu!"
# text = "Jekk wara l-qari ta’ kitba deskrittiva l-qarrejja jħossu li saru jafu"

# # convert text to phonemes
# text = g2p_cw_rules(text)
#
# # fix kh instances from g2p tool
# text = (re.sub('kh', '', re.sub('kh ', 'h ', text)))
#
# # make sure the sentence has sufficient length for attention mechanism
# text.ljust(30, '.')
#
# # make sure a sentence ends in full stop
# if (text[-1:] != '.'):
#     text = text + '.'
#
# # padd 'x' sounds with spaces. Tend to produce better pronunciations more often than not.
# text = re.sub('ʃ', ' ʃ ', text)


# Generate Speech
def text_manipulation(text):
    text = g2p_cw_rules(text)

    # fix kh instances from g2p tool
    text = (re.sub('kh', '', re.sub('kh ', 'h ', text)))

    # make sure the sentence has sufficient length for attention mechanism
    text.ljust(30, '.')

    # make sure a sentence ends in full stop
    if (text[-1:] != '.'):
        text = text + '.'

    # padd 'x' sounds with spaces. Tend to produce better pronounciations more often than not.
    text = re.sub('ʃ', ' ʃ ', text)

    return tts(model, text, figures=False)

# text_manipulation(text)
