from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import numpy as np
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates("/")

import rtvc_main

app = FastAPI()

class EmbedInput(BaseModel):
    wav: list
    sr: int

@app.get('/')
def index():
    """
    greetings
    """
    return templates.TemplateResponse("index.html")

@app.get('/inference/')
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
    embed = jsonable_encoder(embed.tolist())
    return JSONResponse(embed)

@app.get('/preprocess/')
async def inference(userinput: EmbedInput):
    """
    @request
        user voice sample {list}
            {array} wav, {int} sample_rate loaded by librosa
    @response
        user voice embedding {list}
            {ndarray} embedding converted into {list} so that it could be sent as a request;

    **This method preprocesses wav file - nomalizing, match the sampling rate**
    """
    userinput = userinput.dict()
    sample_rate = userinput["sr"]
    wav = userinput["wav"]
    wav = np.array(wav)
    wav = rtvc_main.preprocess(wav, sample_rate)
    wav = jsonable_encoder(wav.tolist())
    return JSONResponse(wav)
