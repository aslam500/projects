import cv2 as cv
import os
import shutil

def calculate_subfs(image_path1, image_path2, min_shape_size, max_shape_size):
    """
    This function takes two image paths, a minimum and maximum shape size, and calculates the subshapes
    within each image. It saves the subshapes to separate folders and then removes those folders.

    Args:
        image_path1 (str): Path to the reference image.
        image_path2 (str): Path to the test image.
        min_shape_size (int): Minimum size of a subshape to be considered.
        max_shape_size (int): Maximum size of a subshape to be considered.

    Returns:
        None
    """

    reference_output_folder = "reference_output_shapes"
    test_output_folder = "test_output_shapes"

    # Create output folders if they don't exist
    if not os.path.exists(reference_output_folder):
        os.makedirs(reference_output_folder)

    if not os.path.exists(test_output_folder):
        os.makedirs(test_output_folder)

    # Process the reference image
    detect_and_save_shapes(image_path1, reference_output_folder, min_shape_size, max_shape_size)

    # Process the test image
    detect_and_save_shapes(image_path2, test_output_folder, min_shape_size, max_shape_size)

    print("Shapes from reference and test images have been saved.")

    try:
        # Remove the output folders after processing
        shutil.rmtree(reference_output_folder)
        shutil.rmtree(test_output_folder)
        print("Output folders removed.")
    except OSError as e:
        print(f"Error: {e}")


def detect_and_save_shapes(image_path, output_folder, min_shape_size, max_shape_size):
    """
    This function detects and saves subshapes from an image within a specified size range.

    Args:
        image_path (str): Path to the image.
        output_folder (str): Path to the folder where subshapes will be saved.
        min_shape_size (int): Minimum size of a subshape to be considered.
        max_shape_size (int): Maximum size of a subshape to be considered.

    Returns:
        None
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read and pre-process the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the perimeter approximation accuracy
        epsilon = 0.04 * cv.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        num_vertices = len(approx)

        # Get the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Filter out shapes outside the specified size range
        if w >= min_shape_size and h >= min_shape_size and w <= max_shape_size and h <= max_shape_size:
            # Extract the region of interest
            roi = image[y:y + h, x:x + w]

            # Skip empty ROIs
            if len(roi) > 0:
                # Identify the shape based on the number of vertices
                if num_vertices == 3:
                    shape_name = "Triangle"
                elif num_vertices == 4:
                    # Check for squareness based on aspect ratio
                    aspect_ratio = float(w) / h
                    if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                        shape_name = "Square"
                    else:
                        shape_name = "Rectangle"
                elif num_vertices == 5:
                    shape
