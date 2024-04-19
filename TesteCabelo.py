import cv2
import numpy as np

# Load images
face_image = cv2.imread('homemCareca.jpg')
hair_image = cv2.imread('hair.png')

# Resize and align hair image
resized_hair = cv2.resize(hair_image, (face_image.shape[1], face_image.shape[0]))

# Create a mask to identify the region of the face where the hair will be placed
mask = np.zeros_like(face_image)
# Assuming the region where hair will be placed is white in the mask
# You can generate this mask manually or using other techniques
mask[:] = (255, 255, 255)  

# Blend images
blended_image = cv2.seamlessClone(resized_hair, face_image, mask, (face_image.shape[1] // 2, face_image.shape[0] // 2), cv2.NORMAL_CLONE)

# Display the result
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
