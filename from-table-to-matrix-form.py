import yaml


def load_and_convert_yaml_to_matrices(file_path, full_output_file, simplified_output_file):
    # Load YAML data
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    # Extract camera matrix and distortion coefficients
    camera_matrix = data['camera_matrix']
    dist_coeff = data['dist_coeff'][0]

    # Intrinsic parameters
    fx = camera_matrix[0][0]
    fy = camera_matrix[1][1]
    cx = camera_matrix[0][2]
    cy = camera_matrix[1][2]

    # Flatten distortion coefficients
    dist_coeff_flat = []
    for item in dist_coeff:
        if isinstance(item, list):
            dist_coeff_flat.extend(item)
        else:
            dist_coeff_flat.append(item)

    # Construct the full matrix form
    full_matrix_form = [fx, fy, cx, cy] + dist_coeff_flat
    # Construct the simplified matrix form
    simplified_matrix_form = [fx, fy, cx, cy]

    # Save full matrix form to a text file
    with open(full_output_file, "w") as f:
        f.write(str(full_matrix_form))

    # Save simplified matrix form to a different text file
    with open(simplified_output_file, "w") as f:
        f.write(str(simplified_matrix_form))

    return full_matrix_form, simplified_matrix_form


# Example usage
file_path = 'yaml-files/test-camera-2'  # Update this path if the file is located differently
full_output_file = 'matrix-from-yaml/test-camera-2-full.txt'  # The file where the full matrix form will be saved
simplified_output_file = 'matrix-from-yaml/test-camera-2-simplified.txt'  # The file where the simplified matrix form will be saved
full_matrix_form, simplified_matrix_form = load_and_convert_yaml_to_matrices(file_path, full_output_file,
                                                                             simplified_output_file)
print("Full Matrix Form saved to", full_output_file)
print("Simplified Matrix Form saved to", simplified_output_file)