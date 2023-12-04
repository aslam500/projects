import cv2

# Open the video file
video_capture = cv2.VideoCapture('your_video.mp4')

if not video_capture.isOpened():
    print("Error: Could not open the video file.")
else:
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Video resolution: {width}x{height}")
video_capture.release()
