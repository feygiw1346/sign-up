import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


BASE_DIR = Path(__file__).parent
DEFAULT_IMAGE = BASE_DIR / "data" / "71.jpg"
DEFAULT_OUTPUT = BASE_DIR / "outputs" / "rgb_histogram.png"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate and plot RGB histogram using NumPy."
    )
    parser.add_argument(
        "--image",
        type=Path,
        default=DEFAULT_IMAGE,
        help="Path to input image (default: data/71.jpg)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Path to save histogram image (default: outputs/rgb_histogram.png)",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Skip opening a GUI window with the plot.",
    )
    return parser.parse_args()


def ensure_rgb_image(image_path: Path) -> np.ndarray:
    if not image_path.exists():
        raise FileNotFoundError(
            f"Image file '{image_path}' not found. Use --image to set a path."
        )

    img = Image.open(image_path)
    if img.mode != "RGB":
        img = img.convert("RGB")

    img_array = np.array(img)
    if len(img_array.shape) != 3 or img_array.shape[2] != 3:
        raise ValueError(
            f"Expected RGB image with 3 channels, got shape: {img_array.shape}"
        )
    return img_array


args = parse_args()
image_path = args.image if args.image.is_absolute() else BASE_DIR / args.image
output_path = args.output if args.output.is_absolute() else BASE_DIR / args.output
output_path.parent.mkdir(parents=True, exist_ok=True)

img_array = ensure_rgb_image(image_path)

r_hist, r_bins = np.histogram(img_array[:, :, 0], bins=256, range=(0, 256))
g_hist, g_bins = np.histogram(img_array[:, :, 1], bins=256, range=(0, 256))
b_hist, b_bins = np.histogram(img_array[:, :, 2], bins=256, range=(0, 256))

plt.figure(figsize=(12, 6))
plt.plot(r_bins[:-1], r_hist, color="red", label="Red", alpha=0.7)
plt.plot(g_bins[:-1], g_hist, color="green", label="Green", alpha=0.7)
plt.plot(b_bins[:-1], b_hist, color="blue", label="Blue", alpha=0.7)
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.title("RGB Color Histogram")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(output_path)

if not args.no_show:
    plt.show()

