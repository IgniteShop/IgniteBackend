from flask import Blueprint, send_file
import torchvision.utils as vutils
import torch
import numpy as np

preview = Blueprint('preview', __name__)

@preview.route("/preview", methods=["GET"])
def generatePreview():
    manualSeed = np.random.randint(1, 10000) # use if you want new results
    torch.manual_seed(manualSeed)
    print("Manual seed: ", manualSeed)

    device = torch.device("cpu")

    model = torch.load("./models/gen.pt", map_location=device)

    model.zero_grad()
    model.eval()

    noise = torch.randn(1, 100, 1, 1, device=device)
    fake = model(noise)

    vutils.save_image(fake[0], f"./images/preview.jpg")

    return send_file(open(f"./images/preview.jpg", 'rb'), mimetype='image/png')