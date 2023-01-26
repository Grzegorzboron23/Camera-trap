import cv2
import pyautogui
import random
import time

# Enable camera
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
# import cascade file for facial recognition
cubeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_kostka.xml")
delay = 0
while True:
    success, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Getting corners around the cube
    cubes = cubeCascade.detectMultiScale(imgGray, 1.3, 10)  # 1.3 = scale factor, 5 = minimum neighbor
    # drawing bounding box around cube
    for (x, y, w, h) in cubes:
        cv2.putText(img, 'Cube', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if delay % 100 == 0:
            # generating a random number between 1
            # to 5 which will represent the time
            # delay
            #random_time = random.randint(1, 4)
            myScreenshot = pyautogui.screenshot()
            # create a time delay using the sleep()
            #myScreenshot.interval = 100
            #time.sleep(random_time)
            # Save the screenshot shot using current
            # time as file name.
            file_name = str(time.time()) + ".png"
            myScreenshot.save(fr'C:\Users\ASUS\PycharmProjects\pythonProject1\images\{file_name}')
    cv2.imshow('Objects detection', img)
    delay = delay + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow('Objects detection')