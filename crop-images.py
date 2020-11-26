from PIL import Image
img = Image.open("ON Pan card/Marvee-Pan.jpg")
newsize = (715, 475) 
img = img.resize(newsize)
img.save("Test.jpg")
w, h = img.size
img2 = img.crop((300, 340, 535, 465))
#img3 = img.crop((0, 340, 310, 465))

img2.save("img2.jpg")
#img3.save("img3.jpg")

