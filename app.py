from flask import Flask, render_template, Response
import cv2



from flask import Flask, render_template, Response
import cv2
import os

app = Flask(__name__)

cap = cv2.VideoCapture(0)
image_counter = 0  # Contador para nombres de archivos únicos

@app.route('/')
def index():
    global image_counter
    # Captura una imagen cuando alguien accede a la página
    success, frame = cap.read()
    if success:
        # Guarda la imagen con un nombre único
        image_path = f'captura_{image_counter}.jpg'
        cv2.imwrite(image_path, frame)
        image_counter += 1
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
