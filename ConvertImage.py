import uuid 
from PIL import ImageTk, Image

def convertImage(): 
    filename = str(uuid.uuid4())
    img = Image.open("./Image/figure.png") 
    img = img.convert("RGBA") 
  
    data = img.getdata() 
  
    newData = [] 
  
    for item in data: 
        if item[0] == 255 and item[1] == 255 and item[2] == 255: 
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item) 
  
    img.putdata(newData) 
    img.save("Image/figure.png", "PNG") 
    print("Successful")