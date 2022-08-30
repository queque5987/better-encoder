"""
    ***************************************************
    author: Park Young-woong
    e-mail: pyw5987@gmail.com
    github: https://github.com/queque5987/better-encoder
    ***************************************************
"""
from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import json

import rtvc_main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmbedInput(BaseModel):
    wav: list
    sr: int

@app.get('/')
def index():
    return FileResponse('index.html')
    # return templates.TemplateResponse("index.html")

@app.post('/inference/')
async def inference(userinput: EmbedInput):
    """
    @request
        user voice sample {list}
            {array} wav, {int} sample_rate loaded by librosa
    @response
        user voice embedding {list}
            {ndarray} embedding converted into {list} so that it could be sent as a request;

    **This method returns user utterance embedding inferenced by Speaker Encoder**
    """
    userinput = userinput.dict()
    sample_rate = userinput["sr"]
    wav = userinput["wav"]
    wav = np.array(wav)
    embed = rtvc_main.inference(wav, sample_rate)
    # embed = jsonable_encoder(embed.tolist())
    # return JSONResponse(embed)
    embed = embed.tolist()
    embed_json = json.dumps({
        "embed": embed
    })
    return JSONResponse(embed_json)

@app.post('/preprocess/')
async def inference(userinput: EmbedInput):
    """
    @request
        user generated voice {list}
            {array} wav, {int} sample_rate loaded by librosa
    @response
        user generated voice trimed {list}
            wav {list} use librosa or other library to generate wav file with it.

    **This method preprocesses wav file - nomalizing, match the sampling rate**
    """
    userinput = userinput.dict()
    sample_rate = userinput["sr"]
    wav = userinput["wav"]
    wav = np.array(wav)
    wav = rtvc_main.preprocess(wav, sample_rate)
    # wav = jsonable_encoder(wav.tolist())
    wav = wav.tolist()
    wav_json = json.dumps({
        "wav": wav
    })
    return JSONResponse(wav_json)
