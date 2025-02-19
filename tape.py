import cv2
import numpy as np

cap = cv2.VideoCapture("dummy1.webm") 

while True:
    ret, frame = cap.read()
    if not ret:
        break  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    x_positions = []
    y_positions = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        x_positions.append(x + w // 2) 
        y_positions.append(y + h // 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Bantları işaretle

    x_positions.sort()


    if len(x_positions) == 2:
        distance = (x_positions[1] - x_positions[0]) ** 2 + (y_positions[1] - y_positions[0]) ** 2
        distance = int(np.sqrt(distance))
        cv2.putText(frame, f"Mesafe: {distance}px", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print(distance)

    cv2.imshow("Mask", mask)
    cv2.imshow("Detected", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
