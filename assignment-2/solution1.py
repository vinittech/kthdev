import cv2
import numpy as np

def main():
    # Read video from disk and count frames
    cap = cv2.VideoCapture('test_videos/2.mp4')
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    count = 0

    # Read every frame till the end of video
    while count < frameCount:
        ret, frame = cap.read()
        if ret == True:
            count = count + 1
            frame_cloned = np.copy(frame)
            img_HSV = cv2.cvtColor(frame_cloned, cv2.COLOR_RGB2HSV)
            
            # For Blue cone
            img_thresh_low = cv2.inRange(img_HSV, np.array([0, 135, 135]), np.array([15, 255, 255])) #всё что входит в "левый красный"
            img_thresh_high = cv2.inRange(img_HSV, np.array([159, 135, 135]), np.array([179, 255, 255])) #всё что входит в "правый красный"
            img_thresh = cv2.bitwise_or(img_thresh_low, img_thresh_high)

            kernel = np.ones((5,5))
            img_thresh_opened = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
            img_thresh_blurred = cv2.medianBlur(img_thresh_opened, 5)
            img_edges = cv2.Canny(img_thresh_blurred, 80, 160)
            contours, _ = cv2.findContours(np.array(img_edges), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            coordinates = []
            rects = []
            for cnt in contours:
                rect = cv2.boundingRect(cnt)
                rects.append(rect)
                (x,y,w,h) = rect
                aspect_ratio = w/h
            
                cv2.rectangle(frame_cloned ,(x,y-h), (x+w,y+(2*h)), (0, 255, 255), 5)
                cv2.putText(frame_cloned, 'blue cone', (int(x),int(y)-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            
            # For yellow cone
            
            img_thresh_yellow = cv2.inRange(img_HSV, np.array([45,155,215], dtype=np.uint8), np.array([190, 255,245], dtype=np.uint8)) #всё что входит в "правый красный"
            
            img_edges = cv2.Canny(img_thresh_yellow, 80, 160)
            contours, _ = cv2.findContours(np.array(img_edges), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            coordinates = []
            rects = []
            for cnt in contours:
                rect = cv2.boundingRect(cnt)
                rects.append(rect)
                (x,y,w,h) = rect
                aspect_ratio = w/h
                if aspect_ratio < 0.5:
                    cv2.rectangle(frame_cloned ,(x,y-h), (x+w,y+(2*h)), (0, 255, 255), 5)
                    cv2.putText(frame_cloned, 'yellow cone', (int(x),int(y)-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

          
            cv2.imshow('Original frame', frame)
            cv2.imshow('Detected frame', frame_cloned)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
       
if __name__ == '__main__':
    main()
