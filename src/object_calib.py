import os
import torch

from vican.cam import estimate_pose_mp
from vican.dataset import Dataset

DATASET_PATH = '/dataset'

MARKER_SIZE = 0.48 * 0.575

MARKER_IDS = list(map(str, range(24)))

def main():
    print("Loading dataset...")

    obj_dataset = Dataset(root=os.path.join(DATASET_PATH, 'cube_calib'))

    aux = estimate_pose_mp(cams=obj_dataset.im_data['cam'],
                        im_filenames=obj_dataset.im_data['filename'],
                        aruco='DICT_4X4_1000',
                        marker_size=MARKER_SIZE,
                        corner_refine='CORNER_REFINE_APRILTAG',
                        marker_ids=MARKER_IDS,
                        flags='SOLVEPNP_IPPE_SQUARE',
                        brightness=-150,
                        contrast=120)

    torch.save(aux, os.path.join(DATASET_PATH, 'cube_calib_pose.pt'))

if __name__ == "__main__":
    main()
    