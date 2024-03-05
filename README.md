# Camera Calibration and Matrix Conversion Repository

This repository is dedicated to camera calibration and the conversion of camera parameters from YAML files to matrix form. It contains Python scripts and calibration samples designed to process and analyze camera intrinsic parameters.

## Structure

- `.idea`: IDE-specific settings for project management and configuration.
- `calib-variants`: Contains Python scripts that offer different variations of camera calibration procedures.
- `matrix-from-yaml`: Scripts to convert camera parameters from YAML files into matrix representation.
- `yaml-files`: Sample YAML files with camera calibration parameters.
- `README.md`: A guide to understanding and navigating the repository.
- `from-table-to-matrix-form.py`: Converts calibration parameters from table form to matrix form.
- `mean-calib.py`: Averages multiple calibration results for more precise intrinsic parameters.
- `multiple-view-keypoints.py`: Detects keypoints from multiple views to improve the accuracy of the camera matrix.
- `only-one-keypoint.py`: A simplified script for single keypoint detection and calibration.

## Overview

The repository consists of Python scripts developed for the purpose of camera calibration and the conversion of calibration data into two matrix forms:

1. The simplified form `fx fy cx cy`.
2. The extended form `fx fy cx cy [k1 k2 p1 p2 [ k3 [ k4 k5 k6 ]]]`.

The scripts read YAML files containing camera calibration parameters, which typically include the camera matrix and distortion coefficients, and convert them into the desired matrix forms