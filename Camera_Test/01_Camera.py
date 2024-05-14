import cv2
import requests
import numpy as np
from io import BytesIO
import time 

# Cambia las credenciales y la URL según la configuración de tu cámara
username = 'root'
password = 'admin'
url = 'http://192.168.0.11/axis-cgi/mjpg/video.cgi'

cv2.namedWindow("Frame_1", cv2.WINDOW_NORMAL)

# Configura las credenciales para la solicitud
auth = requests.auth.HTTPDigestAuth(username, password)

try:
    response = requests.get(url, auth=auth, stream=True)
    response.raise_for_status()
    bytes_data = bytes()

    for chunk in response.iter_content(chunk_size=100000):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')
        b = bytes_data.find(b'\xff\xd9')

        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]

            # Decodifica la imagen
            frame1 = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow("Frame_1", frame1)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        print("AAAAAAAA")
except requests.exceptions.RequestException as e:
    print(f"Error de solicitud: {e}")

cv2.destroyAllWindows()

