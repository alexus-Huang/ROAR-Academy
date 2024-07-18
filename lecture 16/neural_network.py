## This is course material for Introduction to Modern Artificial Intelligence
## Example code: mlp.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Load dependencies
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Create data
linearSeparableFlag = False
x_bias = 6

def toy_2D_samples(x_bias ,linearSeparableFlag):
    label1 = np.array([[1, 0, 0, 0]])
    label2 = np.array([[0, 1, 0, 0]])
    array1 = np.array([[0, 0, 1, 0]])
    array2 = np.array([[0, 0, 0, 1]])

    if linearSeparableFlag:
        samples1 = np.random.multivariate_normal([5+x_bias, 0], [[1, 0],[0, 1]], 100)
        samples2 = np.random.multivariate_normal([-5+x_bias, 0], [[1, 0],[0, 1]], 100)
        samples = np.concatenate((samples1, samples2), axis=0)
        
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'rx')
        plt.show()
    else:
        samples1 = np.random.multivariate_normal([5+x_bias, 5], [[1, 0], [0, 1]], 50)
        samples2 = np.random.multivariate_normal([-5+x_bias, -5], [[1, 0], [0, 1]], 50)
        samples3 = np.random.multivariate_normal([-5+x_bias, 5], [[1, 0], [0, 1]], 50)
        samples4 = np.random.multivariate_normal([5+x_bias, -5], [[1, 0], [0, 1]], 50)
        samples = np.concatenate((samples1, samples2, samples3, samples4), axis=0)
        
        # Plot the data
        plt.plot(samples1[:, 0], samples1[:, 1], 'bo')
        plt.plot(samples2[:, 0], samples2[:, 1], 'bo')
        plt.plot(samples3[:, 0], samples3[:, 1], 'rx')
        plt.plot(samples4[:, 0], samples4[:, 1], 'rx')
        plt.show()

    labels1 = np.repeat(label1, 50, axis=0)
    labels2 = np.repeat(label2, 50, axis=0)
    labels3 = np.repeat(array1, 50, axis=0)
    labels4 = np.repeat(array2, 50, axis=0)
    labels = np.concatenate((labels1, labels2, labels3, labels4), axis=0)
    return samples, labels

samples, labels = toy_2D_samples(x_bias, linearSeparableFlag)

# Split training and testing set
randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[0:100], :]
trainingY = labels[randomOrder[0:100], :]
testingX = samples[randomOrder[100:200], :]
testingY = labels[randomOrder[100:200], :]

model = Sequential()
model.add(Dense(4, input_shape=(2,), activation='sigmoid', use_bias=True))
model.add(Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(trainingX, trainingY, epochs=400, batch_size=10, verbose=1, validation_split=0.2)

# Evaluate model
score = model.evaluate(testingX, testingY, verbose=0)
print('Test accuracy:', score[1])

# Visualize the results
predictions = model.predict(testingX)
for i in range(100):
    estimate = np.argmax(predictions[i])
    if estimate < 2:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    else:
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')
plt.show()
