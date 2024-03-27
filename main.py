from datetime import datetime
from BackgroundRemover import remove_background

# TODO This value depends on whether the average contents of the photo is similar to the background of the photo 
# or not. For example with the light blue shirt on white background, I have to use ~0.05 otherwise the shirt
# gets transparent-y. Whereas with the dark blue jeans I can set it to 0.4 with no issue. I should try to get
# a "similar-ness" value which figures out how close to the background each pixel is -- the sharper the difference,
# the larger this value can be.
wiggle_room = 0.33
input_filename = "./images/shirt.jpg"
# Turn 12:59:59.123456 into 125959
date_string = str(datetime.now().time()).split('.')[0].replace(':','')
output_filename = f"./images/test-{date_string}-{wiggle_room}"

# Can pass as background if needed
white = (255,255,255)

background_remover = remove_background(input_filename, output_filename, wiggle_room)