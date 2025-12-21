import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Check if the image file exists
image_path = '71.jpg'
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file '{image_path}' not found in the current directory.")

# Load the image and convert it to a NumPy array
img = Image.open(image_path)

# Convert image to RGB mode if it's not already (handles grayscale, RGBA, etc.)
if img.mode != 'RGB':
    img = img.convert('RGB')

img_array = np.array(img)

# Verify that we have a 3-channel RGB image
if len(img_array.shape) != 3 or img_array.shape[2] != 3:
    raise ValueError(f"Expected RGB image with 3 channels, got shape: {img_array.shape}")

# Calculate histogram for each color channel separately (Red, Green, Blue)
# Using range=(0, 256) to properly include all pixel values from 0 to 255
r_hist, r_bins = np.histogram(img_array[:, :, 0], bins=256, range=(0, 256))
g_hist, g_bins = np.histogram(img_array[:, :, 1], bins=256, range=(0, 256))
b_hist, b_bins = np.histogram(img_array[:, :, 2], bins=256, range=(0, 256))

# Create and display the RGB histogram
plt.figure(figsize=(12, 6))
plt.plot(r_bins[:-1], r_hist, color='red', label='Red', alpha=0.7)
plt.plot(g_bins[:-1], g_hist, color='green', label='Green', alpha=0.7)
plt.plot(b_bins[:-1], b_hist, color='blue', label='Blue', alpha=0.7)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('RGB Color Histogram')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the histogram as an image file
output_path = 'rgb_histogram.png'
plt.savefig(output_path)
print(f"Histogram saved to '{output_path}'")

# Display the histogram in a window
plt.show()

print("RGB Histograms calculated and displayed successfully!")