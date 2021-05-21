import numpy as np
import keras


def load(path_to_model):
    '''
    Load the model only on initializing. 
    '''
    model = keras.models.load_model(path_to_model)
    return model


def preprocessing(images):
    '''
    Preprocess the raw image array generated from readImg
    which has the shape like [[img], [...]]

    The model input shape should be the same as the model
    built, which is [None, 28, 28, 1]

    @Param
    @Return:
        2d numpy array shape in [None, 28, 28, 1], which 
        ranges in 0 ~ 1
    '''
    return images.reshape((images.shape[0], 28, 28, 1)).astype('float32') / 255


def predict(model, image):
    '''
    Run the model with predicting function, and output the
    index that having the maximum probability.
    '''
    data = preprocessing(image)
    prediction = model.predict(data)
    return np.argmax(prediction, axis=1)


def test_mnist():
    '''
    Test the model with mnist dataset.
    '''
    from keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_test = x_test.reshape(10000, 28, 28, 1)
    x_test = x_test.astype('float32') / 255
    model = Classificator('./model/cnn16.h5')
    number = model.predict(x_test[0:10])
    print(number)


def test_cnn_img():
    import readImg
    test = readImg.readImg(r"upload/test2.png")
    model = Classificator('./model/cnn16.h5')
    data = model.preprocessing(test)
    number = model.predict(data)
    print(number)


if __name__ == '__main__':
    test_cnn_img()
