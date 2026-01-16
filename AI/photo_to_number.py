import tensorflow as tf  # Import hlavní knihovny TensorFlow pro práci s neuronovými sítěmi
from tensorflow import keras  # Import API Keras pro snadnější definici modelů


# Načtení datasetu MNIST (obsahuje 60 000 trénovacích a 10 000 testovacích obrázků)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# Normalizace dat (škálování pixelů do rozsahu 0-1)
# Obrázky mají hodnoty pixelů od 0 do 255, normalizací je převedeme na rozsah 0.0 až 1.0
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definice jednoduchého modelu neuronové sítě
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Převedení 2D obrázku 28x28 na 1D vektor s 784 prvky
    keras.layers.Dense(128, activation='relu'),  # Skrytá vrstva s 64 neurony a aktivační funkcí ReLU (max(0, x))
    # Skrytá vrstva umožňuje modelu naučit se složitější vztahy v datech
    keras.layers.Dense(64, activation='relu'),  # Skrytá vrstva s 64 neurony a aktivační funkcí ReLU (max(0, x))
    # Skrytá vrstva umožňuje modelu naučit se složitější vztahy v datech
    keras.layers.Dense(10, activation='softmax') # Výstupní vrstva s 10 neurony (pro číslice 0–9)
    # Softmax vrstva převede výstupy na pravděpodobnosti (součet všech 10 výstupů = 1)
])

# Kompilace modelu
# Optimalizátor 'adam' (Adaptive Moment Estimation) adaptivně upravuje rychlost učení
# Ztrátová funkce 'sparse_categorical_crossentropy' je vhodná pro více tříd s celými čísly jako labely
# Metrika 'accuracy' sleduje přesnost klasifikace
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Trénování modelu na trénovacích datech
# Provede 3 průchody (epochy) celým trénovacím datasetem
model.fit(x_train, y_train, epochs=15)

# Vyhodnocení modelu na testovacích datech
# Funkce evaluate vypočítá ztrátu a přesnost modelu na testovacích datech
test_loss, test_acc = model.evaluate(x_test[0:1500], y_test[0:1500], verbose=2)
print(f'Přesnost: {test_acc:.4f}')  # Výpis výsledné přesnosti modelu na testovací sadě")}]}

#save model to file
model.save('mnist_model.h5')

# open model to use later
model = keras.models.load_model('mnist_model.h5')
import numpy as np
from PIL import Image
# Načtení vlastního obrázku pro testování modelu
# Předpokládáme obrázek ve stupních šedi s rozměry 28x28 pixelů
image_path = 'AI/img1.png'  # Zadejte cestu k vlastnímu obrázku
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