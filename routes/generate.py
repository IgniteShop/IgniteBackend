from models.model import Generator
from flask import Blueprint, send_file
import torchvision.utils as vutils
import requests
import torch

generate = Blueprint('generate', __name__)

@generate.route("/generate_one", methods=["GET"])
def generateImage():
    model = Generator()
    model.load_state_dict(torch.load("./models/gen.pt", map_location=torch.device('cpu')))
    model.eval()

    device = torch.device("cpu")
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

    return send_file(open(f"./images/generate_one.jpg", 'rb'), mimetype='image/gif')