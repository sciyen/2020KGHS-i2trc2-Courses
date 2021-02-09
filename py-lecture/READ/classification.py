import numpy as np
import keras


class Classificator:
    def __init__(self, path_to_model):
        '''
        Load the model only on initializing. 
        '''
        self.model = keras.models.load_model(path_to_model)

    def preprocessing(self, arr):
        '''
        Preprocess the raw image array generated from readImg
        which has the shape like [[x, img], [...]]

        The model input shape should be the same as the model
        built, which is [None, 28, 28, 1]

        @Param
        @Return:
            2d numpy array shape in [None, 28, 28, 1], which 
            ranges in 0 ~ 1
        '''
        data = []
        for x, img in arr:
            x_test = img.reshape((28, 28, 1))
            x_test = x_test.astype('float32') / 255
            data.append(x_test)
        return np.array(data)

    def predict(self, data):
        '''
        Run the model with predicting function, and output the
        index that having the maximum probability.
        '''
        prediction = self.model.predict(data)
        return np.argmax(prediction, axis=1)


def test_mnist():
    '''
    Test the model with mnist dataset.
    '''
    from keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_test = x_test.reshape(10000, 28, 28, 1)
    x_test = x_test.astype('float32') / 255
    model = Classificator('./cnn16.h5')
    number = model.predict(x_test[0:10])
    print(number)


def test_cnn_img():
    import readImg
    test = readImg.readImg(r"upload/test2.png")
    model = Classificator('./cnn16.h5')
    data = model.preprocessing(test)
    number = model.predict(data)
    print(number)


if __name__ == '__main__':
    test_mnist()
