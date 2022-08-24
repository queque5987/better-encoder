from pathlib import Path
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
def preprocess(wav, sampling_rate):
    preprocessed_wav = encoder.preprocess_wav(wav, sampling_rate)
    return preprocessed_wav