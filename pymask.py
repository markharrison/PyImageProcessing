import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image using PIL (Python Imaging Library)
img = Image.open('cat.jpg')

# Convert the image to a NumPy array
img_array = np.array(img)

# Create a binary mask
mask = np.zeros_like(img_array[:, :, 0], dtype=np.uint8)
center = (img_array.shape[0] // 2, img_array.shape[1] // 2)
radius = min(img_array.shape[0], img_array.shape[1]) // 2  # Increase radius for a bigger circle
rr, cc = np.meshgrid(np.arange(img_array.shape[0]), np.arange(img_array.shape[1]), indexing='ij')
circle_mask = (rr - center [0]) ** 2 + (cc - center [1]) ** 2 < radius ** 2
mask[circle_mask] = 1

# Apply the mask to the image
masked_img = img_array.copy()
for i in range(img_array.shape[2]):  # Apply to each color channel
    masked_img[:,:,i] = img_array[:,:,i] * mask

# Displaying the original image and the masked image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(masked_img)
plt.title('Masked Image')
plt.axis('off')

plt.tight_layout()
plt.show() 