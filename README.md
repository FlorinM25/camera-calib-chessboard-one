Camera Calibration and Matrix Conversion Repository
===================================================

This repository is dedicated to camera calibration and the conversion of camera parameters from YAML files to matrix form. It contains Python scripts and calibration samples designed to process and analyze camera intrinsic parameters.

Structure
---------

The project consists of the following files and directories:

-   **.idea/**: IDE-specific settings for project management and configuration.
-   **calib-variants/**: Contains Python scripts that offer different variations of camera calibration procedures.
-   **matrix-from-yaml**: Scripts to convert camera parameters from YAML files into matrix representation.
-   **yaml-files/**: Sample YAML files with camera calibration parameters.
-   **README.md**: A guide to understanding and navigating the repository.
-   **from-table-to-matrix-form.py**: Converts calibration parameters from table form to matrix form.
-   **mean-calib.py**: Averages multiple calibration results for more precise intrinsic parameters.
-   **multiple-view-keypoints.py**: Detects keypoints from multiple views to improve the accuracy of the camera matrix.
-   **only-one-keypoint.py**: A simplified script for single keypoint detection and calibration.

Overview
--------

The repository consists of Python scripts developed for the purpose of camera calibration and the conversion of calibration data into two matrix forms:

1.  **The simplified form**:
    `fx fy cx cy`

2.  **The extended form**:
    `fx fy cx cy [k1 k2 p1 p2 [ k3 [ k4 k5 k6 ]]]`

The scripts read YAML files containing camera calibration parameters, which typically include the camera matrix and distortion coefficients, and convert them into the desired matrix forms.

Getting Started
---------------

### Prerequisites

-   Python 3.x
-   Required Python libraries: `numpy`, `opencv-python`

### Installation

1.  Clone the repository to your local machine:
    `git clone https://github.com/yourusername/camera-calibration-matrix-conversion.git`

2.  Navigate to the project directory:
    `cd camera-calibration-matrix-conversion`

3.  Install the required Python libraries:
    `pip install numpy opencv-python`

Usage
-----

1.  **Converting YAML to Matrix Form**:

    -   Use the script `matrix-from-yaml.py` to convert camera parameters from a YAML file to matrix form.
    -   Example:
        `python matrix-from-yaml.py path/to/your/yamlfile.yaml`

2.  **Averaging Calibration Results**:

    -   Use the script `mean-calib.py` to average multiple calibration results for more accurate intrinsic parameters.
    -   Example:
        `python mean-calib.py path/to/calibration/results/`

3.  **Detecting Multiple View Keypoints**:

    -   Use the script `multiple-view-keypoints.py` to detect keypoints from multiple views.
    -   Example:
        `python multiple-view-keypoints.py path/to/images/`

4.  **Single Keypoint Detection and Calibration**:

    -   Use the script `only-one-keypoint.py` for a simplified calibration process using a single keypoint.
    -   Example:
        `python only-one-keypoint.py path/to/image.jpg`
