# vican
Very efficient algorithm for camera calibration dockerized

## How to use

### Step 1 - build the docker image

```
docker build -t <image-name> .
```

### Step 2 - setup dataset

Create a directory with the following disposal

The folders structure of ```<object-images>``` and ```<cameras-images>``` is ```<dataset>/<timestep>/<camera_id>.jpg```

```
<volume-directory>
├── config.txt
├── <object-images>
│   ├── 0
│   │   └── 0.jpg
│   ├── 1
│   │   └── 1.jpg
    ...
│   └── cameras.json
└── <cameras-images>
    ├── 0
    │   ├── 1.jpg
    │   ├── 10.jpg
    │   ├── 11.jpg
    │   ├── 12.jpg
    │   ...
    ├── 1
    │   ├── 1.jpg
    │   ├── 10.jpg
    │   ├── 11.jpg
    │   ├── 15.jpg
    │   ...
    ...
    └── cameras.json
```

### Step 3 - calibrate an object

```
docker run -v ./<volume-dir>:/dataset <image-name> python src/object_calib.py
```

### Step 4 - estimate poses of a camera network

```
docker run -v ./<volume-dir>:/dataset <image-name> python src/pose_est.py
```

#### Example of config file - [config.txt](./config.txt)

```
object_path:<object-images>
object_calib:cube-calib.pt
cameras_path:<cameras-images>
cameras_pose_est:pose_est.mat
aruco:DICT_4X4_1000
marker_size:0.276
marker_ids:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
brightness:-150
contrast:120
```

#### Example of ```<object-images>/cameras.json```

```
{
    "0": {
        "fx": 711.1111111111111,
        "fy": 711.1111111111111,
        "cx": 640,
        "cy": 360,
        "resolution_x": 1280,
        "resolution_y": 720,
        "clip_start": 0.10000000149011612,
        "clip_end": 1000,
        "t": [
            5.816105365753174,
            21.875133514404297,
            2.772583246231079
        ],
        "R": [
            [
                0.03479209542274475,
                -0.9984201192855835,
                0.044123295694589615
            ],
            [
                -0.9954691529273987,
                -0.038530927151441574,
                -0.08692909777164459
            ],
            [
                0.08849187195301056,
                -0.04089892655611038,
                -0.995236873626709
            ]
        ],
        "distortion": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    },
    "1": {
        "fx": 711.1111111111111,
        "fy": 711.1111111111111,
        "cx": 640,
        "cy": 360,
        "resolution_x": 1280,
        "resolution_y": 720,
        "clip_start": 0.10000000149011612,
        "clip_end": 1000,
        "t": [
            5.816105365753174,
            21.875133514404297,
            2.772583246231079
        ],
        "R": [
            [
                0.03479209542274475,
                -0.9984201192855835,
                0.044123295694589615
            ],
            [
                -0.9954691529273987,
                -0.038530927151441574,
                -0.08692909777164459
            ],
            [
                0.08849187195301056,
                -0.04089892655611038,
                -0.995236873626709
            ]
        ],
        "distortion": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    },
    "2": {
        "fx": 711.1111111111111,
        "fy": 711.1111111111111,
        "cx": 640,
        "cy": 360,
        "resolution_x": 1280,
        "resolution_y": 720,
        "clip_start": 0.10000000149011612,
        "clip_end": 1000,
        "t": [
            5.816105365753174,
            21.875133514404297,
            2.772583246231079
        ],
        "R": [
            [
                0.03479209542274475,
                -0.9984201192855835,
                0.044123295694589615
            ],
            [
                -0.9954691529273987,
                -0.038530927151441574,
                -0.08692909777164459
            ],
            [
                0.08849187195301056,
                -0.04089892655611038,
                -0.995236873626709
            ]
        ],
        "distortion": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    },
    ...
}
```

#### Example of ```<cameras-images>/cameras.json```

```
{
  "1": {
    "fx": 711.1111111111111,
    "fy": 711.1111111111111,
    "cx": 640,
    "cy": 360,
    "resolution_x": 1280,
    "resolution_y": 720,
    "clip_start": 0.10000000149011612,
    "clip_end": 1000,
    "t": [
      -4.242201805114746,
      3.6500678062438965,
      2.7108936309814453
    ],
    "R": [
      [
        -0.6672439575195312,
        -0.35407891869544983,
        0.6552966237068176
      ],
      [
        -0.7448351979255676,
        0.32009637355804443,
        -0.5854560732841492
      ],
      [
        -0.0024604161735624075,
        -0.8787299990653992,
        -0.4773128032684326
      ]
    ],
    "distortion": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  },
  "2": {
    "fx": 533.3333333333334,
    "fy": 533.3333333333334,
    "cx": 640,
    "cy": 360,
    "resolution_x": 1280,
    "resolution_y": 720,
    "clip_start": 0.10000000149011612,
    "clip_end": 1000,
    "t": [
      -1.9186244010925293,
      3.781113386154175,
      2.735273838043213
    ],
    "R": [
      [
        -0.9999966025352478,
        -0.0022767793852835894,
        0.001121936016716063
      ],
      [
        -0.002230584854260087,
        0.5773668885231018,
        -0.8164815902709961
      ],
      [
        0.0012111797695979476,
        -0.8164814710617065,
        -0.577370285987854
      ]
    ],
    "distortion": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  },
  ...
}
```
