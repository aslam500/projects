import cv2 as cv
import os
import shutil
import sys
# This function takes two image paths, a minimum and maximum shape size,
# and calculates the shapes in the images, saving them to separate folders.
def calculate_subfs(image_path1, image_path2, min_shape_size, max_shape_size):

    # Define folders to store the reference and test image shapes.
    reference_output_folder = "reference_output_shapes"
    test_output_folder = "test_output_shapes"

    # Create the folders if they don't exist.
    if not os.path.exists(reference_output_folder):
        os.makedirs(reference_output_folder)

    if not os.path.exists(test_output_folder):
        os.makedirs(test_output_folder)

    # Process the reference image and save the shapes.
    detect_and_save_shapes(image_path1, reference_output_folder, min_shape_size, max_shape_size)

    # Process the test image and save the shapes.
    detect_and_save_shapes(image_path2, test_output_folder, min_shape_size, max_shape_size)

    # Print a success message.
    print("Shapes from reference and test images have been saved.")

    # Try to remove the temporary folders, but ignore errors if they already got removed.
    try:
        shutil.rmtree(reference_output_folder)
        shutil.rmtree(test_output_folder)
        print("Output folders removed.")
    except OSError as e:
        print(f"Error: {e}")

# This function takes an image path, an output folder, and minimum and maximum shape size,
# and detects and saves shapes found in the image.
def detect_and_save_shapes(image_path, output_folder, min_shape_size, max_shape_size):

    # Create the output folder if it doesn't exist.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read and pre-process the image.
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the image.
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour.
    for contour in contours:

        # Calculate the perimeter approximation accuracy.
        epsilon = 0.04 * cv.arcLength(contour, True)

        # Simplify the contour and get the number of vertices.
        approx = cv2.approxPolyDP(contour, epsilon, True)
        num_vertices = len(approx)

        # Get the bounding rectangle of the contour.
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the shape is within the specified size range.
        if w >= min_shape_size and h >= min_shape_size and w <= max_shape_size and h <= max_shape_size:

            # Extract the region of interest (ROI) from the original image.
            roi = image[y:y + h, x:x + w]

            # Skip if the ROI is empty.
            if len(roi) > 0:

                # Determine the shape name based on the number of vertices.
                if num_vertices == 3:
                    shape_name = "Triangle"
                elif num_vertices == 4:
                    # Calculate the aspect ratio to distinguish squares from rectangles.
                    aspect_ratio = float(w) / h
                    if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                        shape_name = "Square"
                    else:
                        shape_name = "Rectangle"
                elif num_vertices == 5:
                    shape_name = "Pentagon"
                elif num_vertices == 6:
                    shape_name = "Hexagon"
                else:
                    shape_name = "Circle"

                # Generate a unique filename for the shape based on its type and count.
                # shape_filename = os.path.join(output_)
