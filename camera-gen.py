import json

# Load the data from the JSON file
with open('camera_params.json', 'r') as f:
    data = json.load(f)

# Get the data for object 55
object_55_data = data['11']

# Replicate object 55 data for objects 56 to 88
for i in range(12, 89):
    data[str(i)] = object_55_data

# Write the updated data back to the JSON file
with open('camera_params.json', 'w') as f:
    json.dump(data, f, indent=4)