import cv2
import numpy as np
import sys
from tensorflow.keras.models import load_model

# categories_model1 = ['airplane', 'ant', 'axe', 'banana', 'bicycle', 'bridge', 'butterfly', 'castle', 'cat', 'chair', 'diamond', 'donut', 'The_Eiffel_Tower']
categories = ['apple', 'banana', 'cup', 'finger', 'fish', 'key', 'smiley face', 'sock', 'sword']

def convert_to_grayscale_bitmap(input):
    # Load the black and white image using OpenCV
    image = cv2.imread(input, cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded correctly
    if image is None:
        print("Error: Could not open the image.")
        exit()

    # Resize the image to 28x28 pixels
    resized_image = cv2.resize(image, (28, 28), interpolation=cv2.INTER_AREA)

    # Normalize the pixel values to the range [0, 255]
    normalized_image = cv2.normalize(resized_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # White to Black and Black to White
    for line in range(0,28):
        for col in range(0,28):
            normalized_image[line, col] = 255 - normalized_image[line, col]

    result = normalized_image.flatten()

    return result

if __name__ == "__main__":
    result = convert_to_grayscale_bitmap(sys.argv[1])

    result = np.array([result])
    x = np.empty([0, 784])

    x = np.concatenate((x, result), axis=0)
    x = x.reshape(x.shape[0], 28, 28, 1).astype('float32')
    x /= 255.0

    model = load_model("ShiftAppensApp/Model/pretrained_model2.h5")
    predictions = model.predict(x)
    
    maxProb = 0
    maxI = 0
    i = 0
    for prob in predictions[0]:
        if prob > maxProb:
            maxProb = prob
            maxI = i
        i += 1
    
    print(f"Model predicted: {categories[maxI]}!")