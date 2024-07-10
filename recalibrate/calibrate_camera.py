import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calibrate_camera(camera_id):
    print(f'Calibrating camera {camera_id}')
    # Get all the images
    images_paths = glob.glob(f'dataset/Dataset_Sensei/contlabs/aruco_images_samples/*/{camera_id}')

    # Load the images
    images = [cv2.imread(image_path) for image_path in images_paths]

    # Get the aruco corners
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_1000)
    parameters = cv2.aruco.DetectorParameters_create()
    arucos = [[ids, corners] for corners, ids, _ in [cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters) for image in images]]

    aruco_size = 0.575
    undistorted_points = np.array([
        [0, 0, 0],          # top-left
        [aruco_size, 0, 0], # top-right
        [aruco_size, aruco_size, 0], # bottom-right
        [0, aruco_size, 0] # bottom-left
    ], dtype="float32")

    object_points = []
    image_points = []
    for ids, corners in arucos:
        if ids is not None:
            ids = ids.flatten()
            for i, corner in zip(ids, corners):
                if i == 0:
                    object_points.append(undistorted_points)
                    image_points.append(corner)

    object_points = np.array(object_points)
    image_points = np.array(image_points)

    image_size = (1280, 720)

    ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, image_size, None, None)

    if ret:
        return {'intrinsics': camera_matrix.tolist(), 'distortion': dist_coeffs.flatten().tolist()}
    else:
        print(f'Failed to calibrate camera {camera_id}')
        return None
    
