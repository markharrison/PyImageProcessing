import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image using PIL (Python Imaging Library)
img = Image.open('cat.jpg')

# Convert the image to a NumPy array
img_array = np.array(img)

# Grayscale conversion formula: Y = 0.299*R + 0.587*G + 0.114*B
gray_img = np.dot (img_array[..., :3], [0.299, 0.587, 0.114])

# Display the original RGB image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original RGB Image')
plt.axis('off')

# Display the converted grayscale image
plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.title('Grayscale Image')
plt.axis('off')

plt.tight_layout()
plt.show() 