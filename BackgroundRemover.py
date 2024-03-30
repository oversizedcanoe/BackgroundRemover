from PIL import Image
from ColorHelper import ColorHelper
import time

transparent_color = (255,255,255,0)

def remove_background(input_filename, output_filename, wiggle_room = None, background_color = None):
    start = time.time()
    image = Image.open(input_filename).convert("RGBA")
    image_data = image.getdata()
    new_data = []

    if background_color is None:
        background_color = get_determined_background_color(image)

    helper = ColorHelper(background_color)
    # Determine the optimal wiggle room. Start with something very small, 3%.
    # Loop through the pixels, skipping those within background color range.
    # For the non-skipped pixels, add up their average RGB value.
    # If this average is close to background, keep wiggle room low. The farther
    # this average is from the background, the higher we can go.
    if wiggle_room is None:
        total_r = 0
        total_g = 0
        total_b = 0
        non_background_pixels_counted = 0
        helper.set_wiggle_room(0.03)
        for pixel_data in image_data:
            red = pixel_data[0]
            green = pixel_data[1]
            blue = pixel_data[2]
            if helper.is_close_to_background((red, green, blue), background_color) == False:
                total_r += red
                total_g += green
                total_b += blue
                non_background_pixels_counted += 1

        if non_background_pixels_counted != 0:
            average_r = round(total_r / non_background_pixels_counted)
            average_g = round(total_g / non_background_pixels_counted)
            average_b = round(total_b / non_background_pixels_counted)

            color_difference = helper.get_color_difference((average_r, average_g, average_b), background_color)
            helper.update_ideal_wiggle_room(color_difference)
    else:
        helper.set_wiggle_room(wiggle_room)
        
    for pixel_data in image_data:
        if helper.is_close_to_background((pixel_data[0], pixel_data[1], pixel_data[2]), background_color):
            new_data.append(transparent_color)
        else:
            new_data.append(pixel_data)

    image.putdata(new_data)
    file_name = f'{output_filename}-{round(helper.get_wiggle_room(), 3)}.png'
    image.save(file_name, "PNG")
    end = time.time()
    print(f'Image saved: \'{file_name}\' in {end-start} seconds')
            

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
