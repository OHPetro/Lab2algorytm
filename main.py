from PIL import Image,ImageDraw
import re


class pixel_to_art():

    def __init__(self, file):
        self.file=file

    def do_art(self):

        canvas = Image.new('RGBA', (540, 960), "black")
        idraw = ImageDraw.Draw(canvas)

        file = open(self.file)
        strfile = file.readlines()
        strfilesplit = []

        for i in range(len(strfile)):
            strfilesplit.append(re.findall(r'\d+', strfile[i]))

        for a in range(len(strfilesplit)):
            idraw.point((int(strfilesplit[a][0]), int(strfilesplit[a][1])), fill="white")

        canvas.show()


my_art = pixel_to_art('DS3.txt')
my_art.do_art()












