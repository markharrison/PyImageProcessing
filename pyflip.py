import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image using PIL (Python Imaging Library)
img = Image.open('cat.jpg')

# Convert the image to a NumPy array
img_array = np.array(img)

# Flip the image horizontally
flipped_img = np.fliplr(img_array)

# Display the original image and the flipped image
plt.figure(figsize=(10, 5))

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')

# Display the flipped image
plt.subplot(1, 2, 2)
plt.imshow(flipped_img)
plt.title('Flipped Image')
plt.axis('off')

plt.tight_layout()
plt.show() 