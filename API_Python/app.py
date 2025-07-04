import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows


@app.get("/superheroescambiosotrodev")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

    
@app.get("/superheroesfull")
def get_superheroes():
    rows = ["Superman", "Aquaman"]
    return rows

@app.get("/superheroesok")
def get_superheroes():
    rows = ["Superman", "Aquaman","sssdsdsd"]
    return rows


@app.get("/superheroesok2")
def get_superheroes():
    rows = ["Supermen", "Aquamen"]
    return rows

