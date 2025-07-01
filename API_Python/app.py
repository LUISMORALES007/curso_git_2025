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


@app.get("/superheroesVarios")
def get_superheroes():
    rows = ["BarbillaRoja", "Antman", "Cirenoman y chico percebe"]
    return rows

@app.get("/superheroesMarvel")
def get_superheroes():
    rows = ["Spiderman", "Thor", "Ironman", "Hulk", "Wolverine"]
    return rows    


@app.get("/superheroesInventados")
def get_superheroes():
    rows = ["Spidercat", "Thorado", "Ironmaiden", "Hulking", "Wolverineheim"]
    return rows  



@app.get("/superheroesInventados2")
def get_superheroes():
    rows = ["Capman", "AuThor", "Ironwoman", "Hilk", "Wolverinerbi"]
    return rows       


 @app.get("/superheroesInventados3")
def get_superheroes():
    rows =[
  "Capman",
  "AuThor",
  "Ironwoman",
  "Hilk",
  "Wolverinerbi",
  "Shadow Vortex",
  "Voltaris",
  "Solaris Flame",
  "Nebula X",
  "Echo Fist",
  "Crimson Drift",
  "Mystblade",
  "Phantom Pulse",
  "Spectro",
  "Glacier Hawk"
]
    return rows    