import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image using PIL (Python Imaging Library)
img = Image.open('cat.jpg')

# Convert the image to a NumPy array
img_array = np.array(img)

# Check if the image is grayscale or RGB
is_grayscale = len(img_array.shape) < 3

# Function to create negative of an image
def create_negative(image):
    if is_grayscale:
        # For grayscale images
        negative_image = 255 - image
    else:
        # For color images (RGB)
        negative_image = 255 - image
    return negative_image

# Create negative of the image
negative_img = create_negative(img_array)

# Display the original and negative images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_img)
plt.title('Negative Image')
plt.axis('off')

plt.tight_layout()
plt.show() 