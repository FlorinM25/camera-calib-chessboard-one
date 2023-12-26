import numpy as np
import cv2

if __name__ == '__main__':
    pattern_size = (9, 6)
    square_size = 0.02  # cm

    img_points = []
    obj_points = []
    w, h = 0, 0

    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    cap = cv2.VideoCapture(0)

    while True:
        ok, frame = cap.read()
        if ok:
            h, w = frame.shape[:2]

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            found, corners = cv2.findChessboardCorners(img, pattern_size)

            if found:
                term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
                cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

                cv2.drawChessboardCorners(frame, pattern_size, corners, found)

                img_points.append(corners.reshape(-1, 2))
                obj_points.append(pattern_points)

            cv2.imshow("Image with corners", frame)

        if cv2.waitKey(1) == ord('q') or len(img_points) > 10:
            cv2.destroyAllWindows()
            break

    rms = 0  # Initialize RMS to a value greater than 0.25
    iteration = 0

    while rms <= 0.25:
        print(f"\nCalculating - Iteration {iteration + 1}...")
        rms, camera_matrix, dist_coeffs, _rvecs, _tvecs = cv2.calibrateCamera(
            obj_points, img_points, (w, h), None, None
        )

        print("RMS:", rms)
        print("Camera matrix:\n", camera_matrix)
        print("Distortion coefficients: ", dist_coeffs.ravel())

        iteration += 1

        if rms >= 0.25:

            print("Adjust camera or capture more frames for better calibration.")

    print("\nCalibration successful! RMS:", rms)
    print("Camera matrix:\n", camera_matrix)
    print("Distortion coefficients: ", dist_coeffs.ravel())
