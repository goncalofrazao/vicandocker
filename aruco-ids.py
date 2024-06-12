import json
import os

all_ids = set()
# for all json files inside a dir
for directory in os.listdir('dataset/aruco_images'):
    # get json file inside the directory
    for filename in os.listdir(f'dataset/aruco_images/{directory}'):
        if filename.endswith('.json'):
            with open(f'dataset/aruco_images/{directory}/{filename}', 'r') as f:
                data = json.load(f)
                ids = data['ids']
                for id_list in ids:
                    for i in id_list:
                        all_ids.add(i)

print(all_ids)