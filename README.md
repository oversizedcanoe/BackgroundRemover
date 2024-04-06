# simple_background_remover
This library is meant to be a quick and dirty background remover for simple images with solid(ish) background colors. Basically, a green screen. It does not have any sort of 'foreground detection'; it simply transparent-ifies pixels which are similar to the provided (or determined) background color.

The processed files automatically get saved as PNGs.

#### Usage
```python
from simple_background_remover import remove_background

remove_background(input_filename='images/myPhoto.jpg',
                  output_filename='images/processed/myPhoto', 
                  wiggle_room=0.15, 
                  background_color=(0, 0, 0))
```

#### wiggle_room
`wiggle_room` is an optional parameter between 0 and 1. It determines how similar a pixels color can be to the background color and still be considered 'background'. For example, a value of 0.2 means that pixels can be +/- 20% similar to the background color and still be considered background pixels, and therefore made transparents. Note: This 20% range is applied to the R, G, and B value of the background color, so it's not perfect. Ideally it would use [redmean/Euclidean distance](https://en.wikipedia.org/wiki/Color_difference) like the auto-generated `wiggle_room` (more on that below) uses.

If wiggle_room is not passed/left as `None`, the wiggle room will be auto-determined by roughly calculating the contrast between the average foreground and background color. The larger the contrast (i.e. foreground black, background white), the higher `wiggle_room` can be. The smaller the constrast (i.e. foreground black, background dark gray), the lower `wiggle_room` must be, otherwise you risk accidentally transparent-ifying foreground pixels.

#### background_color
`background_color` is an optional parameter for the background color of the image (passed as an RGB color, as `tuple[int, int, int]` -- i.e. (0, 0, 0) for white). If not passed `background_color` will be estimated based on the average color of the top left 5% of the image. Ideally this could be flexible for the caller in the future. 

#### Examples

Demo examples can be seen in [images](https://github.com/oversizedcanoe/BackgroundRemover/tree/main/images). These were generated without specifying a `wiggle_room` or `background_color` value (so they were auto-determined).

Sample usage can be seen in [main.py](https://github.com/oversizedcanoe/BackgroundRemover/blob/main/main.py).

---
## Todo
Lots more can be done to improve this repo. 
 - General clean up -- I wrote this pretty quickly and many places could be cleaned up/refactored
   - Clean up `main.py`
 - Validation on user inputs
 - Improvements on the auto determination of background color and wiggle room
   - Could use the redmean to determine the closeness to background per pixel instead of doing +/- wiggle room -- although may be very slow
   - Allow user to pass in which corner to read background from