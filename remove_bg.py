from PIL import Image
import sys

try:
    img = Image.open('images/cactus.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    # Using a threshold to catch off-white as well
    for item in datas:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save('images/cactus.png', "PNG")
    print("Success")
except Exception as e:
    print(f"Error: {e}")
