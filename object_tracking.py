import cv2

# Initialize the KCF tracker
tracker = cv2.TrackerKCF_create()

# Read the first frame from the video stream
video = cv2.VideoCapture(0)  # Open the webcam
success, frame = video.read()
if not success:
    print("Failed to read video stream")
    exit()

# Select the initial region of interest (ROI) for the card
bbox = cv2.selectROI("Select ROI", frame, fromCenter=False, showCrosshair=True)

# Initialize the tracker with the initial frame and ROI
tracker.init(frame, bbox)

# Start the video processing loop
while True:
    success, frame = video.read()
    if not success:
        break

    # Update the tracker
    success, bbox = tracker.update(frame)

    if success:
        # Draw the bounding box on the frame
        x, y, w, h = [int(coord) for coord in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Video", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
video.release()
cv2.destroyAllWindows()
