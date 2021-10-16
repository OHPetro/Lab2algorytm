from PIL import Image,ImageDraw
import re

canvas = Image.new('RGBA',(540,960),"black")
idraw = ImageDraw.Draw(canvas)


file = open ('DS3.txt')
strfile = file.readlines()
strfilesplit = []


for i in range(len(strfile)):
    strfilesplit.append(re.findall(r'\d+',strfile[i]))

for a in range(len(strfilesplit)):
    idraw.point((int(strfilesplit[a][0]), int(strfilesplit[a][1])), fill="white")

canvas.show()












