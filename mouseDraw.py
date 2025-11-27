import cv2
koordinater = []
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"{x},{y}", (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        koordinater.append((x,y))


    if event == cv2.EVENT_RBUTTONDOWN:
        f = open("test.txt","w")
        for koord in koordinater:
            x,y=koord
            f.write(str(x)+" "+str(y)+"\n")
            

if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    ret, img=cap.read()
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()