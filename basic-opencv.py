


import cv2

def main(capture):
    while True:

        #printf(capture.read())
        #Baca Kamera
        ret, frame = capture.read()
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #lepas cam dan destroy windows
    frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Get data camera
    camera = cv2.VideoCapture(0)
    main(camera)