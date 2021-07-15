import cv2

cap = cv2.VideoCapture(0)
background_1 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_1.jpg")
background_2 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_2.jpg")
background_3 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_3.jpg")
background_4 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_4.jpg")
background_5 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_5.jpg")
background_6 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_6.jpg")

while True:
    k = cv2.waitKey(10)
    flag, frame = cap.read()
    if not flag:
        print("Could not access the WebCam")
        break
    else:
        x = cv2.imshow("Original Frame", frame)
        # k = cv2.waitKey(10)
        if k == ord("1"):
            cv2.destroyWindow(x)
            # cap.release()
            # cv2.destroyAllWindows()
            background_1 = cv2.resize(background_1, (frame.shape[1], frame.shape[0]))
            blended_frame_1 = cv2.addWeighted(background_1, 0.2, frame, 0.8, gamma=0.1)
            cv2.imshow("Blended Frame 1", blended_frame_1)
            if cv2.waitKey(10) == ord("0"):
                break
            else:
                pass
        elif k == ord("2"):
            # cap.release()
            # cv2.destroyAllWindows()
            background_1 = cv2.resize(background_2, (frame.shape[1], frame.shape[0]))
            blended_frame_2 = cv2.addWeighted(background_2, 0.2, frame, 0.8, gamma=0.1)
            cv2.imshow("Blended Frame 2", blended_frame_2)
            if cv2.waitKey(10) == ord("0"):
                break
            else:
                pass
        elif k == ord("3"):
            # cap.release()
            # cv2.destroyAllWindows()
            background_1 = cv2.resize(background_3, (frame.shape[1], frame.shape[0]))
            blended_frame_3 = cv2.addWeighted(background_3, 0.2, frame, 0.8, gamma=0.1)
            cv2.imshow("Blended Frame 3", blended_frame_3)
            if cv2.waitKey(10) == ord("0"):
                break
            else:
                pass
        elif k == ord("4"):
            # cap.release()
            # cv2.destroyAllWindows()
            background_1 = cv2.resize(background_4, (frame.shape[1], frame.shape[0]))
            blended_frame_4 = cv2.addWeighted(background_4, 0.2, frame, 0.8, gamma=0.1)
            cv2.imshow("Blended Frame 4", blended_frame_4)
            if cv2.waitKey(10) == ord("0"):
                break
            else:
                pass
        elif k == ord("5"):
            # cap.release()
            # cv2.destroyAllWindows()
            background_1 = cv2.resize(background_5, (frame.shape[1], frame.shape[0]))
            blended_frame_5 = cv2.addWeighted(background_5, 0.2, frame, 0.8, gamma=0.1)
            cv2.imshow("Blended Frame 5", blended_frame_5)
            if cv2.waitKey(10) == ord("0"):
                break
            else:
                pass
        elif k == ord("6"):
            # cap.release()
            # cv2.destroyAllWindows()
            background_1 = cv2.resize(background_6, (frame.shape[1], frame.shape[0]))
            blended_frame_6 = cv2.addWeighted(background_6, 0.2, frame, 0.8, gamma=0.1)
            cv2.imshow("Blended Frame 6", blended_frame_6)
            if cv2.waitKey(10) == ord("0"):
                break
            else:
                pass
        else:
            if k == ord("0"):
                break
cap.release()
cv2.destroyAllWindows()
