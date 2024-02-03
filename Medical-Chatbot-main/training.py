import tensorflow as tf
import pandas as pd
import numpy as np
data = pd.read_csv("Training.csv")
x = data.drop(["prognosis"], axis = 1).to_numpy()
y_data = data.loc[:, "prognosis"]
labels = y_data.drop_duplicates().to_list()
y = []
for i in y_data:
    y.append(labels.index(i))
y = np.array(y)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(38)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(x, y, epochs=5, verbose = 2, validation_split=0.3)
model.save('my_model.h5')
