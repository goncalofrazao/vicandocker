import cv2 as cv
import os
import sys
import numpy as np

# get argument 1
path = sys.argv[1]
contrast = -50
brightness = 100
# Define the Aruco dictionary
aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_ARUCO_ORIGINAL)

# Define the Aruco parameters
parameters = cv.aruco.DetectorParameters_create()
parameters.cornerRefinementMethod = cv.aruco.CORNER_REFINE_SUBPIX
parameters.cornerRefinementMinAccuracy = 0.05
parameters.adaptiveThreshConstant = 10
parameters.cornerRefinementMaxIterations = 50
parameters.adaptiveThreshWinSizeStep = 5
parameters.adaptiveThreshWinSizeMax = 35

total_ids = 0
all_ids = {}

for folder in os.listdir(path):
    if not os.path.isdir(f'{path}/{folder}'):
        continue
    for file in os.listdir(f'{path}/{folder}'):
        im = cv.imread(f'{path}/{folder}/{file}')
        im = np.int16(im)
        im = im * (contrast/127+1) - contrast
        im += brightness
        im = np.clip(im, 0, 255)
        im = np.uint8(im)

        gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        corners, ids, _ = cv.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        total_ids += len(ids)
        for i in ids:
            all_ids[i[0]] = all_ids.get(i[0], 0) + 1
        cv.aruco.drawDetectedMarkers(im, corners, ids)
        cv.imshow('Aruco', im)
        cv.waitKey(0)

cv.destroyAllWindows()

print(f'Total IDs: {total_ids}')
for i in all_ids:
    print(i, end=',')
print()

for i in all_ids:
    print(f'{i}: {all_ids[i]}')