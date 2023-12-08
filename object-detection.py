import cv2

def main(capture):
    face_dataset = '/home/erlanggabhakti/Documents/assettttss/haarcascade_frontalcatface.xml'
    eye_dataset = '/home/erlanggabhakti/Documents/assettttss/haarcascade_eye.xml'
    smile_dataset = '/home/erlanggabhakti/Documents/assettttss/haarcascade_smile.xml'
    
    face_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)

    while True:
        ret, frame = capture.read()
        
        #ubah warna ke dari BGR ke Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = face_cascade.detectMultiScale(gray, 1.3,5)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        img = cv2.imread('smilel.jpg')

        for (x,y,w,h) in faces:
            center = ((x + w//2, y + h//2))
            #Tampilkan Lingkaran
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)

            face_roi = gray[y:y+h, x:x+w]

            gray_temp = gray[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(face_roi)

            smiles = smile_cascade.detectMultiScale(gray_temp, scaleFactor= 1.3, minNeighbors=5)

            # Untuk setiap mata yang terdeteksi
            for (x2, y2, w2, h2) in eyes:
                # Simpan koordinat titik tengah dari mata yyang terdeteksi
                eye_center = (x + x2 + w2//2, y + y2 + h2//2)
                # Simpan nilai jari-jari dari mata yang terdeteksi
                radius = int(round((w2 + h2) * 0,25))
                #tampilkan lingkaran
                frame = cv2.circle(frame, eye_center, radius, (0, 255, 0), 2)

            for i in smiles:
               if len(smiles) > 1: 
                   cv2.putText(frame,"Smiling",(x,y-50),cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0),3,cv2.LINE_AA)      
               else:
                   print("Anda Tidak Tersenyum")


        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    frame.release()
    cv2.destroyAllwindows()

if __name__ == '__main__':
    # Get data camera
    camera = cv2.VideoCapture(0)
    main(camera)