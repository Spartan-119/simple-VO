import json
from pathlib import Path


def save_json(data, path):
    """Save data to JSON file."""
    path = Path(path)
    with path.open("w") as file:
        json.dump(data, file)


def estimate_distance(coco_dataset):
    """Estimate distance travelled in each frame of the COCO dataset."""
    # Load COCO dataset
    with Path(coco_dataset).open('r') as f:
        data = json.load(f)

    # TODO: Implement visual odometry here
    # example naive implementation where frame index is the distance travelled in meters
    distances = [{"x": i, "y": 0, "z": 0} for i in range(len(data['images']))]
    return distances


def _main():
    """Main entry point"""
    distances = estimate_distance('./data.json')
    save_json(distances, './predictions.json')


if __name__ == "__main__":
    _main()
