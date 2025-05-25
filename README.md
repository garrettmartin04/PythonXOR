# XOR Neural Network

This project represents my first hands-on experience with machine learning in Python, using TensorFlow Keras to build and train a neural network.

The goal was to create a simple feedforward model capable of learning the XOR logic gate — a classic example of a problem that is not linearly separable and thus requires a neural network with a hidden layer to solve.

### Model and Training

- The network has one hidden layer with 8 neurons using the `tanh` activation function.  
- The output layer uses a `sigmoid` activation function to predict values between 0 and 1.  
- The model was trained using binary cross-entropy loss and the Adam optimizer over 5000 epochs.

### Results

After training, the model’s predictions on the four XOR inputs were:

Predicted outputs:
[[0.001]
[0.999]
[0.999]
[0.002]]

These closely approximate the expected XOR outputs `[0, 1, 1, 0]`, demonstrating the network’s successful learning.

### Reflection

This project was a valuable introduction to key machine learning concepts like network architecture, activation functions, and training dynamics. It helped me gain confidence in building and understanding neural networks from scratch.
