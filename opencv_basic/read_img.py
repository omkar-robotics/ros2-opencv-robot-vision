import cv2

# Load an image from file
image = cv2.imread("/home/aryan/Downloads/arduino.jpg")  # Replace with the path to your image

# Check if the image is loaded properly
if image is None:
    print("Error: Could not open or find the image!")
else:
    # Display the image
    cv2.imshow("Displayed Image", image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the window