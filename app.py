from deepface import DeepFace
import cv2

def capturar_imagen(nombre_archivo="login.jpg"):
    cam = cv2.VideoCapture(0)
    
    print("Presiona 'q' para tomar la foto...")
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("Camara", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(nombre_archivo, frame)
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"Imagen guardada como {nombre_archivo}")


def verificar_usuario():
    try:
        resultado = DeepFace.verify(
            img1_path="usuario.jpg",
            img2_path="login.jpg"
        )

        if resultado["verified"]:
            print("Acceso permitido")
        else:
            print("Acceso denegado")

    except Exception as e:
        print("Error en la verificación:", e)


if __name__ == "__main__":
    print("=== Sistema de login facial ===")

    capturar_imagen()
    verificar_usuario()
