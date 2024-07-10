import os
import numpy as np
from get_all_cameras import get_all_cameras
from scipy.sparse import csgraph

dataset_path = 'small_dataset'
all_cameras = [int(camera.split('.')[0]) for camera in get_all_cameras(dataset_path)]
num_cameras = max(all_cameras) + 1
print(f"Number of cameras: {num_cameras}")
print(f"Number of individual graphs: {num_cameras - len(all_cameras)}")
adjacency_matrix = np.zeros((num_cameras, num_cameras), dtype=int)


for timestep in os.listdir(dataset_path):
    if not os.path.isdir(os.path.join(dataset_path, timestep)):
        continue

    cameras = os.listdir(os.path.join(dataset_path, timestep))
    cameras = [int(camera.split('.')[0]) for camera in cameras if camera.endswith('.jpg')]

    for i in range(len(cameras)):
        for j in range(i+1, len(cameras)):
            adjacency_matrix[cameras[i], cameras[j]] += 1
            adjacency_matrix[cameras[j], cameras[i]] += 1

# Check if the graph is fully connected
is_fully_connected = csgraph.connected_components(adjacency_matrix, directed=False)
print(f"The graph is fully connected: {is_fully_connected}")


    