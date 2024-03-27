from PIL import Image
from ColorHelper import ColorHelper
import time

transparent_color = (255,255,255,0)

def remove_background(input_filename, output_filename, wiggle_room = 0.33, background_color = None):
    start = time.time()
    image = Image.open(input_filename).convert("RGBA")
    image_data = image.getdata()
    helper = ColorHelper(wiggle_room)
    new_data = []

    if background_color is None:
        background_color = get_determined_background_color(image)

    for pixel_data in image_data:
        if helper.is_close_to_background((pixel_data[0], pixel_data[1], pixel_data[2]), background_color):
            new_data.append(transparent_color)
        else:
            new_data.append(pixel_data)

    image.putdata(new_data)
    image.save(f'{output_filename}.png', "PNG")
    end = time.time()
    print(f'Image saved: \'{output_filename}.png\' in {end-start} seconds')
            

def get_determined_background_color(image: Image.Image):
    width, height = image.size
    
    # top 5%
    width_limit = round(width * 0.05)
    height_limit = round(height * 0.05)

    total_pixels = 0
    total_red = 0
    total_green = 0
    total_blue = 0

    for x in range(0, width_limit):
        for y in range(0, height_limit):
            pixel_color = image.getpixel((x,y))
            total_red += pixel_color[0]
            total_green += pixel_color[1]
            total_blue += pixel_color[2]
            total_pixels += 1

    return (round(total_red/total_pixels), round(total_green/total_pixels), round(total_blue/total_pixels))
