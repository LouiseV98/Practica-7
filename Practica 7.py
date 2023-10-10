import tkinter as tk
from tkinter import PhotoImage
import threading
import time

class MovingImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Imágenes en movimiento")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # Cargar las imágenes
        self.image_horizontal = PhotoImage(file="Imagen1.png")
        self.image_vertical = PhotoImage(file="Imagen2.png")

        self.horizontal_thread = threading.Thread(target=self.move_horizontal)
        self.vertical_thread = threading.Thread(target=self.move_vertical)

        self.horizontal_direction = 1  # Dirección inicial (1 para derecha, -1 para izquierda)
        self.vertical_direction = 1    # Dirección inicial (1 para abajo, -1 para arriba)

        self.horizontal_start_x = (800 - self.image_horizontal.width()) // 2
        self.vertical_start_y = (600 - self.image_vertical.height()) // 2

        self.horizontal_thread.start()
        self.vertical_thread.start()

    def move_horizontal(self):
        x = self.horizontal_start_x
        while True:
            self.canvas.delete("horizontal_image")
            self.canvas.create_image(x, self.vertical_start_y, image=self.image_horizontal, anchor=tk.NW, tags="horizontal_image")
            x += 10 * self.horizontal_direction

            # Cambiar de dirección cuando alcance los bordes de la ventana
            if x <= 0 or x >= 800 - self.image_horizontal.width():
                self.horizontal_direction *= -1

            self.root.update()
            time.sleep(0.04)

    def move_vertical(self):
        y = self.vertical_start_y
        while True:
            self.canvas.delete("vertical_image")
            self.canvas.create_image(self.horizontal_start_x, y, image=self.image_vertical, anchor=tk.NW, tags="vertical_image")
            y += 10 * self.vertical_direction

            # Cambiar de dirección cuando alcance los bordes de la ventana
            if y <= 0 or y >= 600 - self.image_vertical.height():
                self.vertical_direction *= -1

            self.root.update()
            time.sleep(0.04)

if __name__ == "__main__":
    root = tk.Tk()
    app = MovingImageApp(root)
    root.mainloop()
