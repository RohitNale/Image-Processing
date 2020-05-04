# USAGE
# python extract_frames.py -i {file name} -o {folder name}
# python extract_frames.py -i vid.mp4 -o frames

# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True,
	help="path to input video")
ap.add_argument("-o", "--output", required=True,
	help="path to output folder")
args = vars(ap.parse_args())

if not os.path.exists(args["output"]):
        os.makedirs(args["output"])

path = args["output"]

vidcap = cv2.VideoCapture(args["input"])
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(os.path.join(path , f"{count}.jpg"), image) # save frame as JPEG file
  print(count)
  success,image = vidcap.read()
  # print ('Read a new frame: ', success)
  count += 1
