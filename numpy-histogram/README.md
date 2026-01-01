# Numpy RGB Histogram

Creates an RGB histogram for an input image using NumPy and Matplotlib.

## Setup
- `pip install -r requirements.txt`

## Run
- Default image: `data/71.jpg`
- Save to `outputs/rgb_histogram.png`, open plot window:
  - `python histogram.py`
- Choose a different image or output path:
  - `python histogram.py --image path/to/image.jpg --output outputs/custom.png`
- Skip GUI window (useful for CI/servers):
  - `python histogram.py --no-show`

