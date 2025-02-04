# Image_background_clearity
Given an image of a person, You need to classify whether the background of the person is of uniform color, meaning a single color

The objective of these experiments is to determine whether the background of an image is "clear" or "not clear" by analyzing its colors and structure.
 Different approaches, including color variance, hue distribution, and deep learning, were tested to achieve accurate classification. 
The first two methods rely on color-based analysis after segmenting and masking the foreground, while the third approach 
leverages a deep learning model for classification.


- Variance of Background Color after Masking Foreground
This approach checks the color variation of the background after
isolating the person. However, it struggles when similar background colors or noise are present,
leading to incorrect results, especially if shadows cause different hues to appear.

- Hue-Based Classification Using Color Distribution
The program checks if the background is clear based on the distribution of hues (colors). 
It loads images, segments the person, and analyzes the colors in the background. 
If one color is dominant, it labels the background as "clear"; otherwise, it is labeled as "not clear." 
This method can fail when shadows create multiple hues, making it difficult to infer clarity.

- Deep Learning Model Using VGG16
This approach uses a deep learning model built on the VGG16 architecture to classify backgrounds as "clear" or "not clear."
The model preprocesses and augments the training images, then fine-tunes a pre-trained VGG16 model for feature extraction and classification. 
Due to a lack of data, the model overfits, and adding more data is needed to improve performance.
In summary, the first two methods focus on color-based approaches, while the third uses deep learning to classify the background. Adding more data will help reduce overfitting in the deep learning model and improve accuracy.


For The first and second methods I used segmentation to mask out the Foreground and work with background.
