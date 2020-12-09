from flask import Blueprint, send_file
from flask_cors import cross_origin
from PIL import Image 

mug = Blueprint('mug', __name__)

@mug.route('/mug', methods=["GET"])
@cross_origin()
def getMugImage():
    mugImage = Image.open('./media/mug.png') 
    
    # Hacer una copia para que la imagen original no cambie
    mugImageCopy = mugImage.copy() 
    iaImage = Image.open('./images/generate_one.jpg')

    iaImagecopy = iaImage.copy()
    # iaImagecopy = iaImagecopy.resize([380, 380])
    
    # Pegar iaImagecopy en la playera 
    mugImageCopy.paste(iaImagecopy, (80, 220)) 
    
    # Guardar la imagen 
    mugImageCopy.save('./images/mug.png')
    return send_file(open(f'./images/mug.png', 'rb'), mimetype='image/png', cache_timeout=-1)