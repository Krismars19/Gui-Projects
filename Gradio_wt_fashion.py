import tensorflow as tf
import gradio as gr
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train = x_train / 255.0, 
x_test = x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128,activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile
    (optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5)
def classify_image(image):
    prediction = model.predict(image.reshape(-1, 28, 28, 1)).tolist()[0]
    return {class_names[i]: prediction[i] for i in range(10)}
class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'] 
sketchpad = gr.inputs.Sketchpad()
label = gr.outputs.Label(num_top_classes=4)
gr.Interface(fn=classify_image, 
             inputs=sketchpad,
             outputs=label,
             interpretation="default",
             ).launch()