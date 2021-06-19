from fastapi import FastAPI
from utils import  clean_data
import json

app = FastAPI()


@app.get("/data")
def get_data():
    data = clean_data("test.json")
    return data