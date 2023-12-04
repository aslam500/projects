
```python
import cv2 as cv
import os
import shutil

# This function takes two image paths, a minimum and maximum shape size, and calculates the sub-shapes within those images.
# It saves the detected shapes to separate folders and then deletes those folders.
def calculate_subfs(image_path1, image_path2, min_shape_size, max_shape_size):
    # Define the folders where the reference and test image shapes will be saved.
    reference_output_folder = "reference_output_shapes"
    test_output_folder = "test_output_shapes"

    # Check if the reference output folder exists, if not, create it.
    if not os.path.exists(reference_output_folder):
        os.makedirs(reference_output_folder)

    # Check if the test output folder exists, if not, create it.
    if not os.path.exists(test_output_folder):
        os.makedirs(test_output_folder)

    # Call the function to detect and save shapes from the reference image.
    detect_and_save_shapes(image_path1, reference_output_folder, min_shape_size, max_shape_size)

    # Call the function to detect and save shapes from the test image.
    detect_and_save_shapes(image_path2, test_output_folder, min_shape_size, max_shape_size)

    # Print a message to indicate the shapes have been saved.
    print("Shapes from reference and test images have been saved.")

    try:
        # Try to remove the reference and test output folders after saving the shapes.
        shutil.rmtree(reference_output_folder)
        shutil.rmtree(test_output_folder)
        print("Output folders removed.")
    except OSError as e:
        # If there is an error removing the folders, print the error message.
        print(f"Error: {e}")

# This function takes an image path, an output folder, and a minimum and maximum shape size to detect and save shapes within that image.
def detect_and_save_shapes(image_path, output_folder, min_shape_size, max_shape_size):
    # Create the output folder if it doesn't exist.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the image in color format.
    image = cv2.imread(image_path)

    # Convert the image to grayscale for further processing.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection.
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection to identify the shapes.
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge image.
    _, contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour.
    for contour in contours:
        # Calculate the perimeter approximation accuracy.
        epsilon = 0.04 * cv2.arcLength(contour, True)

        # Simplify the contour using the epsilon parameter.
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Get the number of vertices in the simplified contour.
        num_vertices = len(approx)

        # Get the bounding rectangle of the contour.
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the shape falls within the specified size range.
        if w >= min_shape_size and h >= min_shape_size and w <= max_shape_size and h <= max_shape_size:
            # Get the region of interest (ROI) within the image.
            roi = image[y:y + h, x:x + w]

            # Check if the ROI is not empty.
            if len(roi) > 0:
                # Determine the shape name based on the number of vertices.
                if num_vertices == 3:
                    shape_name = "Triangle"
                elif num_vertices == 4:
                    # Calculate the aspect ratio to distinguish squares from rectangles.
                    aspect_ratio = float(w) / h
                    if aspect_ratio >= 0.95 and aspect_ratio <= 1.
