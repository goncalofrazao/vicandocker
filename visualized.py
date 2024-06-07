import scipy.io as io

x = io.loadmat('dataset/pose_est.mat')

print(x.keys())