from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Shoe(BaseModel):
    id: int
    colour: str
    size: int

shoes = []

@app.post("/shoes/", response_model=Shoe)
def add_pair(pair: Shoe):
    shoes.append(pair)
    return pair

@app.get("/shoes/", response_model=List[Shoe])
def get_all_shoes():
    return shoes

@app.get("/shoes/{pair_id}", response_model=Shoe)
def get_pair(pair_id: int):
    for pair in shoes:
        if pair.id == pair_id:
            return pair
    return "Shoes not found"