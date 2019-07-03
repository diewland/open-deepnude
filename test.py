import sys, os.path as path
from datetime import datetime as dt
t = dt.now()

import cv2
from PIL import Image
from run import paddingresize

img_path = sys.argv[1]
fname, ext = path.splitext(img_path)
out_path = "%s%s%s" % (fname, '_out', ext)

img = cv2.imread(img_path)
padded_img = paddingresize(img)
new_img = Image.fromarray(cv2.cvtColor(padded_img, cv2.COLOR_BGR2RGB))
new_img.save(out_path)

print(dt.now()-t)
