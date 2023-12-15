#import shutil
import logging
import os
import re
def calculate_shapes(reference_image_path: str, test_image_path: str, min_shape_size: int, max_shape_size: int) -> None:

    reference_shapes_folder: str = "reference_output_shapes"
    test_shapes_folder: str = "test_output_shapes"

    os.makedirs(reference_shapes_folder, exist_ok=True)
    os.makedirs(test_shapes_folder, exist_ok=True)

    detect_and_save_shapes(reference_image_path, reference_shapes_folder, min_shape_size, max_shape_size)
    detect_and_save_shapes(test_image_path, test_shapes_folder, min_shape_size, max_shape_size)

    print("Shapes from reference and test images have been saved.")

    try:
        shutil.rmtree(reference_shapes_folder)
        shutil.rmtree(test_shapes_folder)
        print("Output folders removed.")
    except OSError as e:
        logging.error(f"Error removing folders: {e}")

def detect_and_save_shapes(image_path: str, output_folder: str, min_shape_size: int, max_shape_size: int) -> None:

    os.makedirs(output_folder, exist_ok=True)

    image: np.ndarray = cv2.imread(image_path)
    gray: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred: np.ndarray = cv2.GaussianBlur(gray, (5, 5), 0)
    edges: np.ndarray = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon: float = 0.04 * cv2.arcLength(contour, True)

        approx: np.ndarray = cv2.approxPolyDP(contour, epsilon, True)
        num_vertices: int = len(approx)

        x, y, w, h = cv2.boundingRect(contour)

        if w >= min_shape_size and h >= min_shape_size and w <= max_shape_size and h <=
