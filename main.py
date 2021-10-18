from PIL import Image,ImageDraw
import re


class pixel_to_art():

    def __init__(self, file):       #конструктор який приймає ім*я файлу
        self.file=file

    def do_art(self):

        canvas = Image.new('RGBA', (540, 960), "black")      #створення нового малюнку
        idraw = ImageDraw.Draw(canvas)             #зманюємо малюнок

        file = open(self.file)
        strfile = file.readlines()        #записуемо рядки у масив
        strfilesplit = []

        for i in range(len(strfile)): #перебираемо масив ,а саме рядки окремо
            strfilesplit.append(re.findall(r'\d+', strfile[i]))     #відєднуемо числа від інших символів і вписуемо у новий масив

        for a in range(len(strfilesplit)):     #перебираемо масив
            idraw.point((int(strfilesplit[a][0]), int(strfilesplit[a][1])), fill="white")      #підставляемо елементи масиву,як координти і ставимо пікселі на малюнку

        #canvas.save("alglab2.png", "PNG") зберігаемо у форматі PNG
        canvas.show()     #виводимо малюнок


my_art = pixel_to_art('DS0.txt')     #створюемо обєкт
my_art.do_art()     #"запускаемо програму"\викликаемо метод обекту












