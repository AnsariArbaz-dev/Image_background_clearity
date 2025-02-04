from segment import *
import os


images = os.listdir("frames")

sum = 0

for im in images:
    # print(im)
    og = cv2.imread(f"frames/{im}")
    
    image,_ = draw_person_segmentation(og)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    variance = np.var(gray_image)
    # print(f"{image.shape} - variance: {variance}")
    if variance < 1000:
        print(im)
        if "unclear" in im:
            print(im)
            sum += 1
        
            print("Uncler\n---------")
    else:
        if "clear" in im:
            print(im)
            sum += 1
            print("Clear\n---------")


# accuracy calculation
print(sum)
accuracy = sum / len(images)
print(f"Accuracy: {accuracy}")



# variance of the color of background after masking the foreground
# The approach fails when similr color of noice is present in the background
# Accuracy is 0.959375
