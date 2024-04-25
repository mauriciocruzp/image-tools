import cv2
import os

def extract_frames(videos_folder, fps=6):
    # Itera sobre cada archivo en la carpeta de videos
    for filename in os.listdir(videos_folder):
        # Solo procesa archivos de video
        if filename.endswith(".mp4") or filename.endswith(".avi"):
            video_path = os.path.join(videos_folder, filename)
            # Crea una subcarpeta en 'data/' con el nombre del video
            output_folder = os.path.join('rostro_data', os.path.splitext(filename)[0])
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Abre el video
            cap = cv2.VideoCapture(video_path)
            frame_count = 0
            number_frame = 0
            frame_rate = cap.get(cv2.CAP_PROP_FPS)

            # Calcula el intervalo de fotogramas para extraer
            frame_interval = round(frame_rate / fps)

            # Itera sobre cada fotograma
            while True:
                # Lee el siguiente fotograma
                success, frame = cap.read()
                if not success:
                    break

                # Guarda el fotograma si es un fotograma que queremos extraer
                if frame_count % frame_interval == 0:
                    frame_filename = f"frame_{number_frame:04d}.png"
                    frame_path = os.path.join(output_folder, frame_filename)
                    cv2.imwrite(frame_path, frame)
                    number_frame += 1

                frame_count += 1

            # Cierra el video
            cap.release()

            print(f"{number_frame} frames extraídos y guardados en '{output_folder}'")

if __name__ == "__main__":
    video_path = "rostro"
    extract_frames(video_path)
