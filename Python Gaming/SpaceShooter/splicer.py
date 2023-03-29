from PIL import Image
from os import mkdir

#mkdir("Assets/Background/BigStar2")
sheet = Image.open("Assets/Background/BigStar2.png")
count = 0

width, height = sheet.size

## Height: 360 Width = 5760
print(f'Height: {height}, Width: {width}')

strideLength = width/9

left = 475
right = strideLength
top = 175
bottom = height - 20

for x in range(9):
    icon = sheet.crop((left, top, right, bottom))
    icon.save("Assets/Background/BigStar2/{}.png".format(count))
    count += 1
    left += strideLength
    right = right + strideLength