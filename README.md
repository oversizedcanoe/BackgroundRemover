# BackgroundRemover
This library is meant to be a quick and dirty background remover for simple images with solid(ish) background colors. Basically, a green screen. It does not have any sort of 'foreground detection'; it simply transparent-ifies pixels which are similar to the provided (or determined) background color.

Sample usage can be seen in [main.py](https://github.com/oversizedcanoe/BackgroundRemover/blob/main/main.py). The gist is:

```python
from BackgroundRemover import remove_background

remove_background(input_filename, output_filename, wiggle_room, background_color)

# wiggle_room: Optional parameter between 0 and 1. A wiggle room of 0.1 means that
# pixel colors can be within +/-10% of the background and not be made transparent.
# If not passed, an optimal wiggle room will be calculated based on the contrast
# between the background color and the average non-background color.
# Larger contrast = larger wiggle room.

# background_color: Optional parameter for the RGB color of the background (i.e.
# (0,0,0) for white). If not passed, the background color will be estimated based
# on the average color of the top left 5% of the image. 
```

Demo examples can be seen in [images](https://github.com/oversizedcanoe/BackgroundRemover/tree/main/images). These were generated without specifying a `wiggle_room` or `background_color` value (so they were auto-determined).

---
## Todo
Lots more can be done to improve this repo. 
 - General clean up -- I wrote this pretty quickly and many places could be cleaned up/refactored
   - Improve `remove_background` method, it's pretty big -- also it returns nothing so fix call in `main.py`
   - Clean up `main.py`
 - Add typing
 - Method comments
 - Validation on user inputs
 - Improvements on the auto determination of background color and wiggle room
   - Could use the redmean to determine the closeness to background per pixel instead of doing +/- wiggle room -- although may be very slow
   - Allow user to pass in which corner to read background from
 - Improves docs to specify `venv`; figure out how to pip install this package?
   - Make requirements.txt
