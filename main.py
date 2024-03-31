from datetime import datetime
from BackgroundRemover import remove_background
import sys

wiggle_room = None
pic_name = 'shirt'

# testing purposes only. This just updates wiggle_room and pic_name if
# passed by user on cmd line
def is_float(string):
    try:
        float(string)
        return True
    except:
        return False

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print(arg1)
    # not perfect, if image name is numeric this doesn't work
    if is_float(arg1):
        wiggle_room = float(arg1)
    else:
        pic_name = arg1

    if len(sys.argv) > 2:
        arg2 = sys.argv[2]
        print(arg2)
        if is_float(arg2):
            wiggle_room = float(arg2)
        else:
            pic_name = arg2

input_filename = f"./images/{pic_name}.jpg"
# Turn 12:59:59.123456 into 125959
date_string = str(datetime.now().time()).split('.')[0].replace(':','')
output_filename = f"./images/test-{date_string}"

remove_background(input_filename, output_filename, wiggle_room=wiggle_room)