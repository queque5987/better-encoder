from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import numpy as np

import rtvc_main

app = FastAPI()

class EmbedInput(BaseModel):
    wav: list
    sr: int

@app.get('/')
def index():
    return {"Message": "This is Index"}

@app.get('/inference/')
async def inference(userinput: EmbedInput):
    userinput = userinput.dict()
    sample_rate = userinput["sr"]
    wav = userinput["wav"]
    wav = np.array(wav)
    embed = rtvc_main.inference(wav, sample_rate)
    embed = jsonable_encoder(embed.tolist())
    return JSONResponse(embed)

@app.get('/preprocess/')
async def inference(userinput: EmbedInput):
    userinput = userinput.dict()
    sample_rate = userinput["sr"]
    wav = userinput["wav"]
    wav = np.array(wav)
    wav = rtvc_main.preprocess(wav, sample_rate)
    wav = jsonable_encoder(wav.tolist())
    return JSONResponse(wav)
