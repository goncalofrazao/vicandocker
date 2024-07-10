import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
import glob

arucos_distance = []

# dataset_path = 'dataset/Dataset_Sensei/contlabs/aruco_images_samples/*/*.jpg'
dataset_path = 'small_dataset/aruco_images_samples/*/*.jpg'
for f in glob.glob(dataset_path):
    im = cv2.imread(f)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    camera_id = f.split('/')[-1].split('.')[0]
    camera_data = json.load(open('small_dataset/cameras_intrinsics.json'))[str(camera_id)]
    intrinsics, distortion = np.array(camera_data['intrinsics']), np.array(camera_data['distortion'])

    dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_1000)
    parameters = cv2.aruco.DetectorParameters_create()
    marker_corners, marker_ids, _ = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    if marker_ids is None:
        continue

    marker_corners = np.array(marker_corners).reshape(-1, 4, 2)
    marker_ids = np.array(marker_ids).flatten()

    marker_corners = marker_corners[marker_ids < 5]
    marker_ids = marker_ids[marker_ids < 5]

    marker_points = np.array([[-1, 1, 0],
                                [1, 1, 0],
                                [1, -1, 0],
                                [-1, -1, 0]], dtype=np.float32)
    marker_points *= 0.575 * 0.5
    points3d = np.zeros((len(marker_corners), 3))

    for i in range(len(marker_corners)):
        flag, r, t = cv2.solvePnP(marker_points,
                           imagePoints=marker_corners[i].squeeze(),
                           cameraMatrix=intrinsics,
                           distCoeffs=distortion)

        if not flag:
            continue

        r, t = cv2.solvePnPRefineLM(marker_points,
                                    imagePoints=marker_corners[i].squeeze(),
                                    cameraMatrix=intrinsics,
                                    distCoeffs=distortion,
                                    rvec=r,
                                    tvec=t)
        
        points3d[i] += t.reshape(-1)

    for corner in marker_corners:
        cv2.drawContours(im, [corner.astype(int)], -1, (0, 255, 0), 2)
    
    if len(points3d) < 2:
        continue

    for i in range(len(points3d)):
        for j in range(i+1, len(points3d)):
            arucos_distance.append(np.linalg.norm(points3d[i] - points3d[j]))
            # if arucos_distance[-1] > 1:
            #     plt.imshow(im)

            #     plt.title(f)
            #     plt.show()

arucos_distance = np.array(arucos_distance)
arucos_distance = arucos_distance[arucos_distance < 10]

plt.hist(arucos_distance, bins=100)
plt.show()
