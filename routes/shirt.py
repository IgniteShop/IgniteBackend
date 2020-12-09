from flask import Blueprint, send_file
from flask_cors import cross_origin
from PIL import Image 

shirt = Blueprint('shirt', __name__)

@shirt.route('/shirt', methods=["GET"])
@cross_origin()
def getShirtImage():
    shirtImage = Image.open('./media/shirt.png') 
    
    # Hacer una copia para que la imagen original no cambie
    shirtImageCopy = shirtImage.copy() 
    iaImage = Image.open('./images/generate_one.jpg')

    iaImagecopy = iaImage.copy()
    iaImagecopy = iaImagecopy.resize([380, 380])
    
    # Pegar iaImagecopy en la playera 
    shirtImageCopy.paste(iaImagecopy, (300, 270)) 
    
    # Guardar la imagen 
    shirtImageCopy.save('./images/shirt.png')
    return send_file(open(f'./images/shirt.png', 'rb'), mimetype='image/png', cache_timeout=-1)