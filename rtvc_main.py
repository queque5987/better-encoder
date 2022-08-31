from pathlib import Path
from encoder import inference as encoder

def inference(wav, sampling_rate):
    if not encoder.is_loaded():
        print("loading model . . . ")
        encoder.load_model("/")
    preprocessed_wav = encoder.preprocess_wav(wav, sampling_rate)
    embed = encoder.embed_utterance(preprocessed_wav)
    return embed
    
def preprocess(wav, sampling_rate):
    preprocessed_wav = encoder.preprocess_wav(wav, sampling_rate)
    return preprocessed_wav