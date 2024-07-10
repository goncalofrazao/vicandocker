import glob
import cv2
import numpy as np
import json

from get_all_cameras import get_all_cameras
from calibrate_camera import calibrate_camera

# Get all the cameras
cameras = get_all_cameras()

# Calibrate all the cameras
calibrations = {camera.split('.')[0]: calibrate_camera(camera) for camera in cameras if calibrate_camera(camera) is not None}

# Save the calibrations
json.dump(calibrations, open('camera_intrinsics.json', 'w'))
