import os

for folder in os.listdir('dataset/ob_calib'):
    if not os.path.isdir(f'dataset/ob_calib/{folder}'):
        continue

    for filename in os.listdir(f'dataset/ob_calib/{folder}'):
        os.rename(f'dataset/ob_calib/{folder}/{filename}', f'dataset/ob_calib/{folder}/{folder}.png')