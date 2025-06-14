from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

np.set_printoptions(suppress=True)

model = load_model("keras_Model.h5", compile=False)

class_names = open("labels.txt", "r").readlines()

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def classify(img):
    image = Image.open(img).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return [class_name[2:],confidence_score]
    # print("Class:", class_name[2:], end="")
    # print("Accuracy:", confidence_score)


if  __name__ == '__main__':
    
    pass