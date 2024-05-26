import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageColor
df4 = pd.read_csv("final_pixels.csv")
df4.set_index("Unnamed: 0", inplace=True)
df4.pixel_color = df4.pixel_color.apply(lambda r: list(ImageColor.getcolor(r, "RGB")))
array_image = df4.groupby("y").pixel_color.apply(list).tolist()
def multiply_array(list, int):
    final = []
    for element in list:
        for loop in range(int):
            final.append(element)
    return final
cm = 25
final_temp = []
for line in array_image:
    line_cm = multiply_array(line, cm)
    final_temp.append(line_cm)
array_image_cm = multiply_array(final_temp, cm)
numpy_array = np.array(array_image_cm, dtype=np.uint8)
image_final = Image.fromarray(numpy_array)
image_final.save(f"final_x{cm}.jpg")
