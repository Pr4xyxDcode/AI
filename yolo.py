import cv2
from ultralytics import YOLO

koordinater = []


def loadMap(filename):
    global koordinater

    f = open(filename,"r")


    line = "   "
    
    while 1:
        try:
            line = f.readline().split(" ")
            x = int(line[0])
            y = int(line[1])
            print(x,y)
            koordinater.append((x,y))
        except:
            break
    




loadMap("test.txt")



def main():


    # Load your trained YOLO model
    model = YOLO("runs/detect/train2/weights/best.pt")
   # ← replace with your weights file

    # Open webcam (0 = default cam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO inference
        results = model(frame)

        # Draw detections on the frame
        annotated_frame = results[0].plot()
        
        

        for i in range(0,len(koordinater)-1):
            x1,y1 = koordinater[i]
            x2,y2 = koordinater[i+1]
            annotated_frame = cv2.line(annotated_frame,(x1,y1),(x2,y2),color=(255,255,255),thickness=3)

        # Show the frame
        cv2.imshow("YOLO Camera", annotated_frame)

       

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
