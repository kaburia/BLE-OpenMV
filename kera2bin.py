from tensorflow import keras
import tensorflow as tf

# load keras model
model = keras.models.load_model('mobi.h5')

# convert the model to tflite and quantize
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()

# save the converted model
with open('model.tflite', 'wb') as f:
    f.write(tflite_quant_model)