import json
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def animate_distance(meters_to_frame_file, images_folder_path=None):
    with open(meters_to_frame_file, 'r') as f:
        data = json.load(f)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # images = sorted(list(Path(images_folder_path).glob('*.jpg')), key=lambda x: int(x.stem.split('_')[0]))

    x_data, y_data, z_data = [], [], []

    def update_plot(index):
        ax.clear()

        # Get coordinates
        x, y, z = data[index]['x'], data[index]['y'], data[index]['z']
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)

        # Plot the camera's trail
        ax.plot(x_data, y_data, '-o', c='blue')

        # Calculate meters traveled as distance from the first point
        meters_travelled = np.sqrt((x - x_data[0]) ** 2 + (y - y_data[0]) ** 2 + (z - z_data[0]) ** 2)

        # Display the meters traveled as text
        ax.text2D(0.05, 0.95, f"Meters traveled: {meters_travelled:.2f}m", transform=ax.transAxes)

        # Set limits, title, and labels
        min_x, max_x = min(x_data), max(x_data)
        min_y, max_y = min(y_data), max(y_data)
        min_z, max_z = min(z_data), max(z_data)
        ax.set_xlim([min_x - 1, max_x + 1])
        ax.set_ylim([min_y - 1, max_y + 1])
        ax.set_zlim([min_z - 1, max_z + 1])
        ax.set_title(f"Frame {index}")
        ax.set_xlabel("X Coordinate")
        ax.set_ylabel("Y Coordinate")
        ax.set_zlabel("Z Coordinate")

    ani = animation.FuncAnimation(fig, update_plot, frames=len(data), repeat=True)
    # plt.show()
    ani.save('animation.gif', writer='imagemagick', fps=10)


if __name__ == "__main__":
    animate_distance('predictions.json', './data')
