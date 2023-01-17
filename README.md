# SiameseNN

#### Siamese neural network for the website [ucoin.net](ucoin.net)

[![Mixmaster](https://img.shields.io/badge/Developed%20by-mixmaster-blue?style=for-the-badge)](https://github.com/mixma5ter)

A model based on two convolutional neural networks (CNNs) with equal weights and architecture.

The model accepts two images as input and outputs the images similarity coefficient ranging between 0 and 1.

Differs from similar neural networks in using a small dataset.

### Tech stack

* Python 3.7
* Jupyter
* Tensorflow
* Keras
* Keras-tuner
* Numpy
* Pillow

### Описание

* `images_prep` - images preparation
* `data_prep` - data preparation
* `model_tuner` - hyper parameters tuning
* `siamese_nn` - network creation and learning
* `images` - directory for user’s images
* `data` - directory with prepared data

To train the model on your images, create a cascade of directories, each of which contains a set of images of the same class/type.

Example:
```
images
   |_____s1
   |   |_____1.jpg
   |   |_____2.jpg
   |   |_____ ...
   |   |_____10.jpg
   |_____s2
   |_____s3
   |_____ ...
   |_____s40
```

### Network metrics

![Accuracies](docs/acc.png)

![Losses](docs/loss.png)
