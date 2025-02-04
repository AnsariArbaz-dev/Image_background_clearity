import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from segment import *
import uuid

'''

This program checks if the background of an image is clear or not based on colors.
    Loads Images : Reads all images from the "frames" folder.
    Segments the Person : Removes the background, keeping only the person.
    Analyzes Colors : Converts the image to HSV and counts the colors in the background.
    Decides Clarity ; If one color is dominant, the background is clear. If multiple colors are close in count, it's not clear.
    Saves Results : Creates and saves a bar chart showing the color distribution.
    Repeats : Does this for every image in the folder.

'''
# Please look at result_hsv_plots  for results 
# PS the labels of result plots/images define if background is clear or not 
# for specifc images where due to hsadow different hues are formed and cant be inferred by nacked this approach fails
def plot_hue_distribution(image_path):
    
    img = cv2.imread(image_path)

    image,og = draw_person_segmentation(img)
    og = cv2.cvtColor(og, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    mask = np.any(image > 0, axis=-1)

    hue_channel = hsv_image[:, :, 0][mask]

    unique_hues, counts = np.unique(hue_channel, return_counts=True)

    hue_color_map = {
        "Red": (5, 25),
        "Orange": (15, 25),
        "Yellow": (30, 35),
        "Green": (45, 85),
        "Cyan": (95, 125),
        "Blue": (135, 150),
        "Magenta": (160, 179)
    }

    hue_distribution = {color: 0 for color in hue_color_map}

    def get_color_name(hue):
        for color, (low, high) in hue_color_map.items():
            if low <= hue <= high:
                return color
        return "Unknown"

    for hue, count in zip(unique_hues, counts):
        color_name = get_color_name(hue)
        if color_name in hue_distribution:
            hue_distribution[color_name] += count

    colors = list(hue_distribution.keys())
    counts = list(hue_distribution.values())

    nonzero_indices = [i for i, count in enumerate(counts) if count > 0]
    colors = [colors[i] for i in nonzero_indices]
    counts = [counts[i] for i in nonzero_indices]

    label = "Not Clear"
    
    
    if len(counts) > 1:
        sorted_indices = np.argsort(counts)[::-1]  
        print(sorted_indices)
        highest_count = counts[sorted_indices[0]]
        
        try:
            second_highest_count = counts[sorted_indices[1]]
            third_highest_count = counts[sorted_indices[2]]
        except:
            second_highest_count = None
            third_highest_count = None
        print(highest_count,second_highest_count)
        
        
        
        if second_highest_count and  second_highest_count < (0.4 * highest_count):
            label = "Clear"
            if third_highest_count and third_highest_count >= (0.6 * second_highest_count):
                label = "Not Clear"     
        

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    axes[0].imshow(og)
    axes[0].set_title("Image")
    axes[0].axis("off")

    axes[1].bar(colors, counts, color=[plt.cm.hsv((hue_color_map[color][0] + hue_color_map[color][1]) / (2 * 179)) for color in colors])
    axes[1].set_xlabel("Hue Colors")
    axes[1].set_ylabel("Frequency")
    axes[1].set_title(f"Hue Color Distribution (Excluding Black Pixels) **{label}")
    axes[1].set_xticklabels(colors, rotation=45)
    axes[1].set_yticks(np.arange(0, max(counts) + 500, 500))  

    plt.tight_layout()
    
    id = str(uuid.uuid4()).split('-')[1]
    
    plt.savefig(f"/home/arbaz/Downloads/background_clear_or_not/result_hsv_plots/{id}.jpg")

    return label

image_folder = "frames"
images = sorted(os.listdir(image_folder))

right_preds = 0


for im in images:
    image_path = os.path.join(image_folder, im)
    print(f"Processing: {image_path}")
    label = plot_hue_distribution(image_path)

    if label == "Clear" and "clear" in image_path:
        right_preds +=1
    elif label == "Not Clear" and "unclear" in image_path:
        right_preds +=1
        
#Accuracy Calculations
accuracy = right_preds / len(images)
print(f"Accuracy: {accuracy}")

#Accuracy comes 0.790625"


# Please look at result_hsv_plots  for results 
# PS the labels of result plots/images define if background is clear or not 
# for specifc images where due to hsadow different hues are formed and cant be inferred by nacked this approach fails
