import cv2 as cv
import os

# Define the Aruco dictionary
aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_ARUCO_ORIGINAL)

# Define the Aruco parameters
parameters = cv.aruco.DetectorParameters_create()
corner_refine = 'CORNER_REFINE_APRILTAG'
if corner_refine is not None:
        parameters.cornerRefinementMethod = eval('cv.aruco.' + corner_refine)
# parameters.cornerRefinementMinAccuracy = 0.05
# parameters.adaptiveThreshConstant = 10
# parameters.cornerRefinementMaxIterations = 50
# parameters.adaptiveThreshWinSizeStep = 5
# parameters.adaptiveThreshWinSizeMax = 35

total_ids = 0
all_ids = set()

for folder in os.listdir('./dataset/ob_calib2'):
    if not os.path.isdir(f'./dataset/ob_calib2/{folder}'):
        continue
    for file in os.listdir(f'./dataset/ob_calib2/{folder}'):
        image = cv.imread(f'./dataset/ob_calib2/{folder}/{file}')
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        corners, ids, rejected = cv.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        total_ids += len(ids)
        for i in ids:
            all_ids.add(i[0])
        # cv.aruco.drawDetectedMarkers(image, corners, ids)
        # cv.imshow('Aruco', image)
        # cv.waitKey(0)

cv.destroyAllWindows()

print(f'Total IDs: {total_ids}')
for i in all_ids:
    print(i, end=',')
print()