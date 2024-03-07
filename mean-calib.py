import os
import numpy as np
import yaml

def read_calibration_data(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def calculate_mean_calibration(files):
    camera_matrices = []
    dist_coeffs = []

    for file_path in files:
        data = read_calibration_data(file_path)
        camera_matrices.append(data['camera_matrix'])
        dist_coeffs.append(data['dist_coeff'])

    mean_camera_matrix = np.mean(camera_matrices, axis=0)
    mean_dist_coeff = np.mean(dist_coeffs, axis=0)

    return mean_camera_matrix, mean_dist_coeff

# the folder where the yaml files are present
calib_dir = 'calib-variants/iphone-15-promax-alex'

# Adjust the range if you have a different number of files; and adjust the name.yaml
file_paths = [os.path.join(calib_dir, f'{i}-iphone-15-promax-alex-calib.yaml') for i in range(1, 7)]

mean_camera_matrix, mean_dist_coeff = calculate_mean_calibration(file_paths)

# Extracting individual elements for clarity
fx = mean_camera_matrix[0, 0]
fy = mean_camera_matrix[1, 1]
cx = mean_camera_matrix[0, 2]
cy = mean_camera_matrix[1, 2]
k1, k2, p1, p2, k3 = mean_dist_coeff[0, :5]

# Assuming k4, k5, and k6 are zero if not present
k4 = k5 = k6 = 0.0

formatted_output = f"{fx} {fy} {cx} {cy} [{k1} {k2} {p1} {p2} [{k3} [{k4} {k5} {k6}]]]]"


print("Formatted Calibration Parameters:")
print(formatted_output)

# print the camera matrix
print("\nCamera Matrix in Matrix Form:")
print(mean_camera_matrix)
print("\nDistortion Coefficients in Matrix Form:")
print(mean_dist_coeff)
