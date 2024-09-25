# this program will blur photos - to change the photo change file name on line 5

from PIL import Image, ImageFilter #imports image filter from PIL

before = Image.open("daryldickson.webp") #open image file 
after = before.filter(ImageFilter.BoxBlur(10)) #apply blur filter at level 10
after.save("blurrydaryl.jpg") #save the blurre photo to a new file
