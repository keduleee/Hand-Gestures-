import cv2
import mediapipe as mp
import os
import time

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands # type: ignore
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils # type: ignore

# Kamera
cap = cv2.VideoCapture(0)

# Untuk kontrol aksi supaya tidak spam
last_action = ''
last_time = 0

# Fungsi hitung jumlah jari
def count_fingers(hand_landmarks, hand_label):
    finger_tips = [8, 12, 16, 20]
    count = 0

    # 4 jari: telunjuk–kelingking
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1

    # Ibu jari: cek arah kanan/kiri
    if hand_label == "Right":
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            count += 1
    else:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            count += 1

    return count

while True:
    success, frame = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            label = hand_handedness.classification[0].label

            fingers = count_fingers(hand_landmarks, label)

            cv2.putText(frame, f'Fingers: {fingers}', (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

            # Kontrol aplikasi berdasarkan jumlah jari
            current_time = time.time()
            if current_time - last_time > 3:  # jeda 3 detik
                if fingers == 5 and last_action != 'open':
                    os.system("start notepad")  # Ganti 'notepad' jadi 'winword' kalau mau buka Word
                    print("Buka Notepad")
                    last_action = 'open'
                    last_time = current_time

                elif fingers == 0 and last_action != 'close':
                    os.system("taskkill /im notepad.exe /f")  # Ganti juga kalau pakai winword.exe
                    print("Tutup Notepad")
                    last_action = 'close'
                    last_time = current_time

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
