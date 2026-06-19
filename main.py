import cv2
import mediapipe as mp

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils

# Tip landmark IDs for each finger (index, middle, ring, pinky)
FINGER_TIPS = [8, 12, 16, 20]
# PIP (middle joint) IDs for the same fingers
FINGER_PIPS = [6, 10, 14, 18]

def count_fingers(landmarks):
    fingers = []

    # Thumb — compare tip x to the joint above it (lm 3)
    # Flip logic for left hand if needed
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Four fingers — tip y vs pip y (lower y = higher on screen = finger up)
    for tip, pip in zip(FINGER_TIPS, FINGER_PIPS):
        if landmarks[tip].y < landmarks[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.6
    ) as hands:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Flip so it feels like a mirror
            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape

            # MediaPipe needs RGB
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb.flags.writeable = False
            results = hands.process(rgb)
            rgb.flags.writeable = True

            count = 0

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw the skeleton
                    mp_draw.draw_landmarks(
                        frame, hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_draw.DrawingSpec(color=(80, 200, 120), thickness=2, circle_radius=4),
                        mp_draw.DrawingSpec(color=(80, 200, 120), thickness=2)
                    )

                    # Get landmark list (normalised 0–1 coords)
                    lm = hand_landmarks.landmark
                    count = count_fingers(lm)

            # Draw a dark rounded box + big number
            box_x, box_y = 20, 20
            box_w, box_h = 180, 120
            overlay = frame.copy()
            cv2.rectangle(overlay, (box_x, box_y),
                          (box_x + box_w, box_y + box_h),
                          (30, 30, 30), -1)
            cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

            # Finger count (large)
            cv2.putText(frame, str(count),
                        (box_x + 30, box_y + 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 3.5,
                        (80, 200, 120), 6, cv2.LINE_AA)

            # Label
            cv2.putText(frame, "fingers",
                        (box_x + 115, box_y + 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (200, 200, 200), 2, cv2.LINE_AA)

            # Quit hint
            cv2.putText(frame, "Q to quit",
                        (w - 140, h - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (150, 150, 150), 1, cv2.LINE_AA)

            cv2.imshow("Finger Counter", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()