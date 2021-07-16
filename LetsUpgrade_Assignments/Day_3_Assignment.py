import cv2

# https://www.youtube.com/watch?v=MVLuexuikv4
# https://github.com/codingforentrepreneurs?tab=repositories

cap = cv2.VideoCapture(0)
background_1 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_1.jpg")
background_2 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_2.jpg")
background_3 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_3.jpg")
background_4 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_4.jpg")
background_5 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_5.jpg")
background_6 = cv2.imread("../LetsUpgrade_Lecture_Practice/Images/background_6.jpg")


def filter_1(frame, background_1):
    background_1 = cv2.resize(background_1, (frame.shape[1], frame.shape[0]))
    blended_frame_1 = cv2.addWeighted(background_1, 0.2, frame, 0.8, gamma=0.1)
    return blended_frame_1


def filter_2(frame, background_2):
    background_2 = cv2.resize(background_2, (frame.shape[1], frame.shape[0]))
    blended_frame_2 = cv2.addWeighted(background_2, 0.2, frame, 0.8, gamma=0.1)
    return blended_frame_2


def filter_3(frame, background_3):
    background_3 = cv2.resize(background_3, (frame.shape[1], frame.shape[0]))
    blended_frame_3 = cv2.addWeighted(background_3, 0.2, frame, 0.8, gamma=0.1)
    return blended_frame_3


def filter_4(frame, background_4):
    background_4 = cv2.resize(background_4, (frame.shape[1], frame.shape[0]))
    blended_frame_4 = cv2.addWeighted(background_4, 0.2, frame, 0.8, gamma=0.1)
    return blended_frame_4


def filter_5(frame, background_5):
    background_5 = cv2.resize(background_5, (frame.shape[1], frame.shape[0]))
    blended_frame_5 = cv2.addWeighted(background_5, 0.2, frame, 0.8, gamma=0.1)
    return blended_frame_5


def filter_6(frame, background_6):
    background_6 = cv2.resize(background_6, (frame.shape[1], frame.shape[0]))
    blended_frame_6 = cv2.addWeighted(background_6, 0.2, frame, 0.8, gamma=0.1)
    return blended_frame_6


k = cv2.waitKey(10)


while True:
    flag, frame = cap.read()
    # k = cv2.waitKey(10)
    if not flag:
        print("Could not access the WebCam")
        break
    elif flag and k == ord("1"):
        frame = filter_1(frame, background_1)
        cv2.imshow("Filter 1", frame)
    elif flag and k == ord("2"):
        frame = filter_2(frame, background_2)
        cv2.imshow("Filter 2", frame)
    elif flag and k == ord("3"):
        frame = filter_3(frame, background_3)
        cv2.imshow("Filter 3", frame)
    elif flag and k == ord("4"):
        frame = filter_4(frame, background_4)
        cv2.imshow("Filter 4", frame)
    elif flag and k == ord("5"):
        frame = filter_5(frame, background_5)
        cv2.imshow("Filter 5", frame)
    elif flag and k == ord("6"):
        frame = filter_6(frame, background_6)
        cv2.imshow("Filter 6", frame)
    elif flag and k == -1:
        cv2.imshow("Frame", frame)
        # k = cv2.waitKey(10)
    else:
        break
cap.release()
cv2.destroyAllWindows()

# while True:
#     flag, frame = cap.read()
#     if not flag:
#         print("main")
#         print("Could not access the WebCam")
#         break
#     else:
#         cv2.imshow("Original Frame", frame)
#         k = cv2.waitKey(10)
#         if k == ord('1') or k == ord('2') or k == ord('3') or k == ord('4') or k == ord('5') or k == ord('6'):
#             cap.release()
#             # cv2.destroyAllWindows()
#             continue
#     # k = cv2.waitKey(10)
#
#     if k == ord('1'):
#         while True:
#             print("1")
#             flag, frame = cap.read()
#             if not flag:
#                 print("Could not access the WebCam")
#                 break
#             else:
#                 background_1 = cv2.resize(background_1, (frame.shape[1], frame.shape[0]))
#                 blended_frame_1 = cv2.addWeighted(background_1, 0.2, frame, 0.8, gamma=0.1)
#                 cv2.imshow("Blended Frame 1", blended_frame_1)
#                 if cv2.waitKey(10) == ord("0"):
#                     break
#     elif k == ord("2"):
#         while True:
#             print("2")
#             flag, frame = cap.read()
#             if not flag:
#                 print("Could not access the WebCam")
#                 break
#             else:
#                 background_2 = cv2.resize(background_2, (frame.shape[1], frame.shape[0]))
#                 blended_frame_2 = cv2.addWeighted(background_2, 0.2, frame, 0.8, gamma=0.1)
#                 cv2.imshow("Blended Frame 2", blended_frame_2)
#                 if cv2.waitKey(10) == ord("0"):
#                     break
#     elif k == ord("3"):
#         while True:
#             print("3")
#             flag, frame = cap.read()
#             if not flag:
#                 print("Could not access the WebCam")
#                 break
#             else:
#                 background_3 = cv2.resize(background_3, (frame.shape[1], frame.shape[0]))
#                 blended_frame_3 = cv2.addWeighted(background_3, 0.2, frame, 0.8, gamma=0.1)
#                 cv2.imshow("Blended Frame 3", blended_frame_3)
#                 if cv2.waitKey(10) == ord("0"):
#                     break
#     elif k == ord("4"):
#         while True:
#             print("4")
#             flag, frame = cap.read()
#             if not flag:
#                 print("Could not access the WebCam")
#                 break
#             else:
#                 background_4 = cv2.resize(background_4, (frame.shape[1], frame.shape[0]))
#                 blended_frame_4 = cv2.addWeighted(background_4, 0.2, frame, 0.8, gamma=0.1)
#                 cv2.imshow("Blended Frame 4", blended_frame_4)
#                 if cv2.waitKey(10) == ord("0"):
#                     break
#     elif k == ord("5"):
#         while True:
#             print("5")
#             flag, frame = cap.read()
#             if not flag:
#                 print("Could not access the WebCam")
#                 break
#             else:
#                 background_5 = cv2.resize(background_5, (frame.shape[1], frame.shape[0]))
#                 blended_frame_5 = cv2.addWeighted(background_5, 0.2, frame, 0.8, gamma=0.1)
#                 cv2.imshow("Blended Frame 5", blended_frame_5)
#                 if cv2.waitKey(10) == ord("0"):
#                     break
#     elif k == ord("6"):
#         while True:
#             print("6")
#             flag, frame = cap.read()
#             if not flag:
#                 print("Could not access the WebCam")
#                 break
#             else:
#                 background_6 = cv2.resize(background_6, (frame.shape[1], frame.shape[0]))
#                 blended_frame_6 = cv2.addWeighted(background_6, 0.2, frame, 0.8, gamma=0.1)
#                 cv2.imshow("Blended Frame 6", blended_frame_6)
#                 if cv2.waitKey(10) == ord("0"):
#                     break
#     else:
#         print("Last")
#         cv2.destroyAllWindows()


# while True:
#     flag, frame = cap.read()
#     if not flag:
#         print("Could not access the WebCam")
#         break
#     else:
#         x = cv2.imshow("Original Frame", frame)
#         # k = cv2.waitKey(10)
#         if k == ord("1"):
#             cv2.destroyWindow(x)
#             # cap.release()
#             # cv2.destroyAllWindows()
#             background_1 = cv2.resize(background_1, (frame.shape[1], frame.shape[0]))
#             blended_frame_1 = cv2.addWeighted(background_1, 0.2, frame, 0.8, gamma=0.1)
#             cv2.imshow("Blended Frame 1", blended_frame_1)
#             if cv2.waitKey(10) == ord("0"):
#                 break
#             else:
#                 pass
#         elif k == ord("2"):
#             # cap.release()
#             # cv2.destroyAllWindows()
#             background_1 = cv2.resize(background_2, (frame.shape[1], frame.shape[0]))
#             blended_frame_2 = cv2.addWeighted(background_2, 0.2, frame, 0.8, gamma=0.1)
#             cv2.imshow("Blended Frame 2", blended_frame_2)
#             if cv2.waitKey(10) == ord("0"):
#                 break
#             else:
#                 pass
#         elif k == ord("3"):
#             # cap.release()
#             # cv2.destroyAllWindows()
#             background_1 = cv2.resize(background_3, (frame.shape[1], frame.shape[0]))
#             blended_frame_3 = cv2.addWeighted(background_3, 0.2, frame, 0.8, gamma=0.1)
#             cv2.imshow("Blended Frame 3", blended_frame_3)
#             if cv2.waitKey(10) == ord("0"):
#                 break
#             else:
#                 pass
#         elif k == ord("4"):
#             # cap.release()
#             # cv2.destroyAllWindows()
#             background_1 = cv2.resize(background_4, (frame.shape[1], frame.shape[0]))
#             blended_frame_4 = cv2.addWeighted(background_4, 0.2, frame, 0.8, gamma=0.1)
#             cv2.imshow("Blended Frame 4", blended_frame_4)
#             if cv2.waitKey(10) == ord("0"):
#                 break
#             else:
#                 pass
#         elif k == ord("5"):
#             # cap.release()
#             # cv2.destroyAllWindows()
#             background_1 = cv2.resize(background_5, (frame.shape[1], frame.shape[0]))
#             blended_frame_5 = cv2.addWeighted(background_5, 0.2, frame, 0.8, gamma=0.1)
#             cv2.imshow("Blended Frame 5", blended_frame_5)
#             if cv2.waitKey(10) == ord("0"):
#                 break
#             else:
#                 pass
#         elif k == ord("6"):
#             # cap.release()
#             # cv2.destroyAllWindows()
#             background_1 = cv2.resize(background_6, (frame.shape[1], frame.shape[0]))
#             blended_frame_6 = cv2.addWeighted(background_6, 0.2, frame, 0.8, gamma=0.1)
#             cv2.imshow("Blended Frame 6", blended_frame_6)
#             if cv2.waitKey(10) == ord("0"):
#                 break
#             else:
#                 pass
#         else:
#             if k == ord("0"):
#                 break
# cap.release()
# cv2.destroyAllWindows()
