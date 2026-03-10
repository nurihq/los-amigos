from PIL import Image, ImageDraw

# Open new correct image
img = Image.open('images/mexican-mascot.png').convert("RGBA")
w, h = img.size

# The image they provided in the second screenshot looks round, but let's check its background
# Assuming it has a black background to remove like before, let's just make the black background transparent using threshold

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
