import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image using PIL (Python Imaging Library)
img = Image.open('cat.jpg')

# Convert the image to grayscale
img_gray = img.convert('L')

# Convert the grayscale image to a NumPy array
img_array = np.array(img_gray)

# Binarize the image using a threshold
threshold = 128
binary_img = np.where(img_array < threshold, 0, 255).astype(np.uint8)

# Display the original and binarized images
plt.figure(figsize= (10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(binary_img, cmap='gray')
plt.title('Binarized Image (Threshold = 128)')
plt.axis('off')

plt.tight_layout()
plt.show() 