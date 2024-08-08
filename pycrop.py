import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image using PIL (Python Imaging Library)
img = Image.open('cat.jpg')

# Convert the image to a NumPy array
img_array = np.array(img)

# Define the cropping coordinates
y1, x1 = 1000, 1000  # Top-left corner of ROI
y2, x2 = 2500, 2000  # Bottom-right corner of ROI
cropped_img = img_array[y1:y2, x1:x2]

# Display the original image and the cropped image
plt.figure(figsize=(10, 5))

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')

# Display the cropped image
plt.subplot(1, 2, 2)
plt.imshow(cropped_img)
plt.title('Cropped Image')
plt.axis('off')

plt.tight_layout()
plt.show()