import cv2


def convert(video_file):
    cap = cv2.VideoCapture(video_file)
#cap = cv2.VideoCapture('starcraft.mp4')
    count = 0

    while cap.isOpened():
        count += 1
        ret, frame = cap.read()

        if count > 300:
            cv2.imwrite('thumbnail.png', frame)
            break
    else:
        raise Exception('video is too short')

    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()


