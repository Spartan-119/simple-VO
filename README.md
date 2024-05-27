
# Simple VO
### Using the LightGlue feature extractor, implemented a Visual Odometry system to estimate the camera's motion in a 3D environment.

[vo](vo.png)

## Getting Started

```bash
cd simple_vo_challenge
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python read_coco.py
python visual_odometry.py
python animate_plot.py
xdg-open animation.gif
```

## Dataset

The provided dataset (`sample_coco_dataset.json`) is formatted in the COCO style. It contains:
- `images`: Each image entry is associated with an `id`, `width`, `height`, and `file_name`.
- `annotations`: Annotations link detected objects with their bounding boxes in specific images. Each annotation entry has an `image_id`, `bbox` (which provides the bounding box in the format `[x, y, width, height]`), and a `category_id`.

