from PIL import Image

path = "./images/pants.jpg"
image = Image.open(path)

width, height = image.size

for x in range(0, width - 1):
    for y in range(0, height - 1):
        pixel_color = image.getpixel((x,y))

        # print(pixel_color)

        # pixel color is (r,g,b) as (int, int int)
        # todo: get average color of top corner of image (or some way to figure out background)
        # overwrite this with transparent

# save as png 
#image.save(...)
        
# open in paint
# image.show()
