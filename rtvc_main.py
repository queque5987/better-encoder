# import os
# import torch
from pathlib import Path

# import librosa
# import numpy as np
# import sounddevice as sd
# import soundfile as sf

from encoder import inference as encoder

class rtvc_args():
    def __init__(self):
        self.enc_model_fpath = Path("saved_models/encoder")
        self.cpu = True
        self.seed = None

def inference(wav, sampling_rate):
    args = rtvc_args()
    encoder.load_model(args.enc_model_fpath)
    preprocessed_wav = encoder.preprocess_wav(wav, sampling_rate)
    embed = encoder.embed_utterance(preprocessed_wav)
    return embed

# if __name__ == "__main__":
#     args = rtvc_args()
#     encoder.load_model(args.enc_model_fpath)
#     in_fpath = Path("testing.wav")
#     original_wav, sampling_rate = librosa.load(str(in_fpath))
#     preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
#     print("Loaded file succesfully")
#     embed = encoder.embed_utterance(preprocessed_wav)
#     print(type(embed))