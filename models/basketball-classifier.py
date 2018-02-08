"""
Original file is located at
    https://colab.research.google.com/drive/1mSPTxe5XSGFHG87TuILFg5qUHACO6E6i
"""

# Importing Tensorflow
import tensorflow as tf

# Checking version of Tensorflow
pip list | grep tensorflow

# Ensuring GPU setup for this notebook
tf.test.gpu_device_name()

# Download Pre-Trained TensorFlow models
git clone https://github.com/tensorflow/models.git

# Directory where the imagenet model is located:
cd models/models/tutorials/image/imagenet/

# Saving picture of basketball to our instance
# We will use this image with the pre-trained imagenet classifier
wget http://3.bp.blogspot.com/_qjlkTyHLyuw/TFt3adewwrI/AAAAAAAAAAk/Bdz2jz79Yjs/s1600/Basketball-large.png

# Running pre-trained classification model on the image of a basketball
# This will return the top 5 most likely categorical labels of the image and their score
python classify_image.py --image_file Basketball-large.png
