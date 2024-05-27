import json
from pathlib import Path

import cv2


def visualise(coco_dataset_path, images_folder_path=None):
    # Load COCO dataset
    coco_dataset_path = Path(coco_dataset_path)
    if images_folder_path is None:
        images_folder_path = coco_dataset_path.parent
    with open(coco_dataset_path, 'r') as f:
        data = json.load(f)

    # Create a mapping of image id to image details for easy access
    image_id_to_image = {img['id']: img for img in data['images']}
    image_id_to_annotations = {img['id']: [] for img in data['images']}
    for ann in data['annotations']:
        image_id_to_annotations[ann['image_id']].append(ann)

    # Sort by image id
    image_id_to_annotations = dict(sorted(image_id_to_annotations.items()))

    # Read the image
    for image in data['images']:
        image_path = images_folder_path / image['file_name']
        img = cv2.imread(str(image_path))

        # Iterate over annotations to display bounding boxes
        for annotation in image_id_to_annotations[image['id']]:
            # Get bounding box details
            x, y, width, height = map(int, annotation['bbox'])

            # Draw bounding box
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

        # Display the image
        cv2.imshow('Image with Bounding Boxes', img)
        cv2.waitKey(1)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    visualise('./annotated_data_coco.json')
