import os
import torch
import numpy as np
from shapely.geometry import Polygon
import scipy.io

from vican.bipgo import bipartite_se3sync, object_bipartite_se3sync

DATASET_PATH = '/dataset'

MARKER_SIZE = 0.48 * 0.575
MARKER_IDS = list(map(str, range(24)))

cam_marker_edges = torch.load(os.path.join(DATASET_PATH, 'cam_marker_edges.pt'))
aux = torch.load(os.path.join(DATASET_PATH, 'cam_marker_edges-2.pt'))

obj_pose_est = object_bipartite_se3sync(aux,
                                        noise_model_r=lambda edge : 0.01 * Polygon(zip(edge['corners'][:,0], edge['corners'][:,1])).area**2,
                                        noise_model_t=lambda edge : 0.001 * Polygon(zip(edge['corners'][:,0], edge['corners'][:,1])).area**6,
                                        edge_filter=lambda edge : edge['reprojected_err'] < 0.1,
                                        maxiter=4,
                                        lsqr_solver="conjugate_gradient",
                                        dtype=np.float64)

tmax = 2000
edges = {k : v for k, v in cam_marker_edges.items() if int(k[1].split('_')[0]) < tmax}

pose_est = bipartite_se3sync(edges,
                             constraints=obj_pose_est,
                             noise_model_r=lambda edge : 0.001 * Polygon(zip(edge['corners'][:,0], edge['corners'][:,1])).area**1.0,
                             noise_model_t=lambda edge : 0.001 * Polygon(zip(edge['corners'][:,0], edge['corners'][:,1])).area**2.0,
                             edge_filter=lambda edge : edge['reprojected_err'] < 0.05,
                             maxiter=4,
                             lsqr_solver="conjugate_gradient",
                             dtype=np.float32)


scipy.io.savemat(os.path.join(DATASET_PATH, 'pose_est.mat'), pose_est)
