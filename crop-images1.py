from PIL import Image
from PIL import ExifTags
#import ExifTags
#import Image

img = Image.open("nitin_new.jpg")
#img.save("Test123.jpg")
newsize = (715, 475) 
img = img.resize(newsize)
img.save("Test.jpg")
w, h = img.size
new = img.crop((250, 360, 520, 455))
all1 = img.crop((10, 340, 510, 465))

new.save("new.jpg")
all1.save("all1.jpg")



#new = img.crop((300, 380, 535, 465))
#img3 = img.crop((0, 340, 510, 465))


'''img = Image.open("ON Pan card/1Naresh.jpg")
print(img._getexif().items())
exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
if not exif['Orientation']:
    img=img.rotate(0, expand=True)
img.thumbnail((1000,1000), Image.ANTIALIAS)
img.save("Test123456.jpg", "JPEG")'''
