import os
import cv2

def compress_images(folder_path, output_size=(64, 128)):
    # Obtener la lista de carpetas dentro de la carpeta principal
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    for subfolder in subfolders:
        # Obtener la lista de imágenes dentro de cada subcarpeta
        image_files = [f.path for f in os.scandir(subfolder) if f.is_file() and f.name.endswith(('.jpg', '.jpeg', '.png'))]

        for image_file in image_files:
            # Leer la imagen
            image = cv2.imread(image_file)

            # Redimensionar la imagen
            resized_image = cv2.resize(image, output_size)

            # Obtener la ruta de salida
            output_file = os.path.join(subfolder, os.path.basename(image_file))

            # Guardar la imagen comprimida
            cv2.imwrite(output_file, resized_image)

            print(f"Imagen comprimida y guardada en: {output_file}")

# Ruta de la carpeta principal
folder_path = "data"

# Comprimir las imágenes en la carpeta principal y sus subcarpetas
compress_images(folder_path)
