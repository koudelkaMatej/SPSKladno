import tensorflow as tf  # Import hlavní knihovny TensorFlow pro práci s neuronovými sítěmi
from tensorflow import keras  # Import API Keras pro snadnější definici modelů
TF_ENABLE_ONEDNN_OPTS=0
model = keras.models.load_model('AI/mnist_model_v2.h5')
import numpy as np
from PIL import Image
# Načtení vlastního obrázku pro testování modelu
# Předpokládáme obrázek ve stupních šedi s rozměry 28x28 pixelů
image_path = 'AI/img3.png'  # Zadejte cestu k vlastnímu obrázku
image = Image.open(image_path).convert('L')  # Převedení na odstíny šedi
image = image.resize((28, 28))  # Změna velikosti na 28x28
image_array = np.array(image) / 255.0  # Normalizace pixelů na rozsah 0-1
image.save("novy.png")



# Přidání dimenze pro dávku (model očekává vstup ve tvaru (batch_size, 28, 28))
image_array = image_array.reshape(1, 28, 28)

# Predikce číslice modelem
predictions = model.predict(image_array)
print(predictions)
predicted_label = np.argmax(predictions)

print(f'Model si myslí, že je na obrázku číslo: {predicted_label}')