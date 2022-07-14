from time import sleep
import re
from fastapi import FastAPI
import measurement

app = FastAPI()


@app.get("/")
async def root():
    return {"temperature": measurement.Measurement().measure()}
