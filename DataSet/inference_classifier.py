#Importacion de librerias necesarias
import pickle
import cv2
import mediapipe as mp
import numpy as np
#Fin de la importación de librerias
class Recognizer:
    def __init__(self):
        self.last_detected_letter = None
        self.detected_letters = ""

    def startCamera(self):
        # Cargamos el modelo IA, previamente entrenado
        # Cargar con la ruta de tu Desktop
        model_dict = pickle.load(open('../model.p', 'rb'))
        model = model_dict['model']

        # Abrimos la cámara web, para comenzar a detectar
        cap = cv2.VideoCapture(0)

        # Pasamos los puntos detectados a la red neuronal CNN (Convolucional)
        mp_hands = mp.solutions.hands  # Puntos de la mano
        mp_drawing = mp.solutions.drawing_utils  # Dibujamos los puntos
        mp_drawing_styles = mp.solutions.drawing_styles  # Le damos color a los puntos

        hands = mp_hands.Hands(static_image_mode=True,
                               min_detection_confidence=0.8)  # Iniciamos el procesamiento neuronal con 80% de precisión

        # Establecemos etiqueta para cada clase de señas detectada, manejada de 0 al 26
        labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
                       5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
                       10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'Ñ',
                       15: 'O', 16: 'P', 17: 'Q', 18: 'R',
                       19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W',
                       24: 'X', 25: 'Y', 26: 'Z'}  # Concierte en el abecedario completo en Español

        # Ciclo para detectar constantemente los puntos de las manos
        while True:
            try:
                data_aux = []
                x_ = []
                y_ = []

                ret, frame = cap.read()
                H, W, _ = frame.shape
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = hands.process(frame_rgb)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,  # image to draw
                            hand_landmarks,  # model output
                            mp_hands.HAND_CONNECTIONS,  # hand connections
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

                    for hand_landmarks in results.multi_hand_landmarks:
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y

                            x_.append(x)
                            y_.append(y)

                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x - min(x_))
                            data_aux.append(y - min(y_))

                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10
                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10

                    prediction = model.predict([np.asarray(data_aux)])
                    predicted_character = labels_dict[int(prediction[0])]

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                                cv2.LINE_AA)

                    # Agregar la letra detectada solo si es diferente a la anterior
                    if predicted_character != self.last_detected_letter:
                        self.detected_letters += predicted_character
                        self.last_detected_letter = predicted_character
                        self.showLetter()

                cv2.imshow('frame', frame)
                cv2.waitKey(1)

            except Exception as ex:
                print(f"Se detectaron demasiados puntos en la cámara: {ex} line 93 of classifier")

        cap.release()
        cv2.destroyAllWindows()

    def showLetter(self):
        try:
           from UI import InitRecognizer
           Instance = InitRecognizer()
           Instance.print_letter(self.detected_letters)
        except Exception as ex:
            print(f"Hubo un error al obtener las letras detectadas: {ex} line 104 of classifier")