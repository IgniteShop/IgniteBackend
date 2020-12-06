from flask import Blueprint, send_file
from flask_cors import cross_origin
import torchvision.utils as vutils
import requests
import torch
# import torch.nn as nn
# import torch.optim as optim
import numpy as np


generate = Blueprint('generate', __name__)

@generate.route("/generate_one", methods=["GET"])
@cross_origin()
def generateImage():
    manualSeed = np.random.randint(1, 10000) # use if you want new results
    torch.manual_seed(manualSeed)
    print("Manual seed: ", manualSeed)

    device = torch.device("cpu")

    model = torch.load("./models/gen.pt", map_location=device)

    model.zero_grad()
    model.eval()

    noise = torch.randn(1, 100, 1, 1, device=device)
    fake = model(noise)

    vutils.save_image(fake[0], f"./images/generate_one.jpg")

    r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={
            'image': open(f"./images/generate_one.jpg", 'rb'),
        },
        headers={'api-key': 'b8ab374d-d187-4260-88e3-5c6206a253ac'}
    )
    
    res = requests.get( r.json()["output_url"] )
    with open(f"./images/generate_one.jpg", "wb") as f:
        f.write(res.content)

    encoded_image = open(f"./images/generate_one.jpg", "rb")

    return send_file(encoded_image, mimetype='image/gif')