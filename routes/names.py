from typing import List
from flask import Blueprint
from flask_cors import cross_origin
import requests
import random
import os

image_name = Blueprint('name', __name__)

@image_name.route("/name", methods=["GET"])
@cross_origin()
def generateName():
    adjectives = open("names\\adjectives.txt", 'r')
    adjectiveList = adjectives.readlines()

    nouns = open("names\\words.txt", 'r')
    nounList = nouns.readlines()

    adjective = random.choice(adjectiveList)
    nouns =  random.sample(nounList, 3)

    name = removeWhitespace([adjective, *nouns])

    return name

def removeWhitespace(strings: List[str]) -> str:
    name = ""

    for string in strings:
        name += string.strip().capitalize()
    
    return name
