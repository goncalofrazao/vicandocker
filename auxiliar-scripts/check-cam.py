cam_file = './dataset/pose_est.json'

import json
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('src')
from vican.geometry import SE3

orientations = []
positions = []
with open(cam_file) as f:
    data = json.load(f)

    for i in data:
        if '_' not in i:
            orientations.append(np.array(data[i]['R']))
            positions.append(SE3(R=np.array(data[i]['R']), t=np.array(data[i]['t'])).inv().t())

# Plot camera positions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#set axes limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

ax.scatter([pos[0] for pos in positions], [pos[1] for pos in positions], [pos[2] for pos in positions], c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plot camera orientations
for pos, rot in zip(positions, orientations):
    r = rot @ np.array([0.1, 0, 0])
    ax.plot([pos[0], pos[0] + r[0]], [pos[1], pos[1] + r[1]], [pos[2], pos[2] + r[2]], c='b')

    r = rot @ np.array([0, 0.1, 0])
    ax.plot([pos[0], pos[0] + r[0]], [pos[1], pos[1] + r[1]], [pos[2], pos[2] + r[2]], c='g')

    r = rot @ np.array([0, 0, 0.1])
    ax.plot([pos[0], pos[0] + r[0]], [pos[1], pos[1] + r[1]], [pos[2], pos[2] + r[2]], c='r')

plt.show()
