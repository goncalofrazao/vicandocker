import os
import cv2 as cv

directory = './dataset/ob_calib'

for folder in os.listdir(directory):
    if not os.path.isdir(f'{directory}/{folder}'):
        continue

    for file in os.listdir(f'{directory}/{folder}'):
        image = cv.imread(f'{directory}/{folder}/{file}')
        image_flip = cv.flip(image, 1)
        cv.imwrite(f'{directory}/{folder}/{file}', image_flip)
        