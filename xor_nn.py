import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# XOR input/output
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

#  model
model = Sequential()
model.add(Dense(8, input_dim=2, activation='tanh'))  
model.add(Dense(1, activation='sigmoid'))

# compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train
model.fit(X, y, epochs=5000, verbose=0)  # training epochs

# predict
predictions = model.predict(X)
print("Predicted outputs:")
print(predictions.round(3))
