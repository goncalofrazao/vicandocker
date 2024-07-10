import glob

def get_all_cameras(dataset_path='dataset/Dataset_Sensei/contlabs/aruco_images_samples'):
    images_paths = glob.glob(f'{dataset_path}/*/*.jpg')

    images_paths = [image_path.split('/')[-1] for image_path in images_paths]
    images_paths = set(images_paths)

    return images_paths

print(len(get_all_cameras()))