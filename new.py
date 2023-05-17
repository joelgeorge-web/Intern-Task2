import cv2

# Load the image
image = cv2.imread("download.jpg")

# Define the bounding box coordinates
x1, y1, w1, h1 = 95, 260, 620, 80
x2, y2, w2, h2 = 70, 400, 350, 60
# Draw the bounding box
cv2.rectangle(image, (x1, y1), (x1+w1, y1+h1), (0, 0, 0), 2)
cv2.rectangle(image, (x2, y2), (x2+w2, y2+h2), (0, 0, 0), 2)
# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
