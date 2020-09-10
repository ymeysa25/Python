# Import open-cv library
import cv2

# Load images
img = cv2.imread('smile.jpg')

# Resize image 3 times smaller 
div = 3
img = cv2.resize(img, (img.shape[1] // div,img.shape[0] //div))

# Edges images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Make image graysclae
gray = cv2.medianBlur(gray, 5) # Add median blur to image
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9) # add adaptiveThreshold

# Color images
color = cv2.bilateralFilter(img, 9, 250, 250)

# Cartoon images
cartoon = cv2.bitwise_and(color, color, mask = edges)

# Show Real, Edges, and Cartoon Images
cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()