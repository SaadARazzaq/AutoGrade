import cv2
import numpy as np
import tkinter as tk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk

def display_images_scrollable(images):
    root = tk.Tk()
    root.title("Scrollable Image Viewer")

    # Create a frame to hold the canvas and scrollbars
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create vertical scrollbar
    y_scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create horizontal scrollbar
    x_scrollbar = Scrollbar(frame, orient=tk.HORIZONTAL)
    x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Create a canvas for displaying images
    canvas = Canvas(frame, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    y_scrollbar.config(command=canvas.yview)
    x_scrollbar.config(command=canvas.xview)

    # Calculate the maximum width and height of the concatenated image
    max_width = sum(image.shape[1] for image in images)
    max_height = max(image.shape[0] for image in images)

    # Create a blank white canvas with the maximum width and height
    composite_image = np.full((max_height, max_width, 3), 255, dtype=np.uint8)
    x_coordinate = 0

    # Concatenate the images horizontally onto the canvas
    for image in images:
        if len(image.shape) == 2 or image.shape[2] == 1:  # Check if the image is grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert grayscale to 3 channels
        composite_image[0:image.shape[0], x_coordinate:x_coordinate+image.shape[1]] = image
        x_coordinate += image.shape[1]

    # Convert the composite image to a PhotoImage (Tkinter image object)
    composite_image_tk = ImageTk.PhotoImage(image=Image.fromarray(composite_image))

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=composite_image_tk)
    canvas.image = composite_image_tk

    # Configure the canvas to allow scrolling
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()