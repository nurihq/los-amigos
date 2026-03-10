from PIL import Image
import sys

try:
    img = Image.open('images/mexican-mascot.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    # Using a threshold to catch almost-black background
    for item in datas:
        # Check if color is very dark
        if item[0] < 30 and item[1] < 30 and item[2] < 30:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save('images/mexican-mascot.png', "PNG")
    print("Success")
except Exception as e:
    print(f"Error: {e}")
