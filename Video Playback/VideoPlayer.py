import cv2
import os

# Global variables
g_slider_position = 0
g_current_frame = 0
g_capture = None

g_window_name = "Video Player"
g_trackbar_name = "Progress (%)"

# Use set track bar to update position

script_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(script_dir, 'test.mp4')


def onTrackbarSlide(pos):
    global g_capture, g_current_frame
    if g_slider_position == pos:
        return
    total_frames = int(g_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    g_current_frame = pos/100 * total_frames
    # cv2.setTrackbarPos(g_trackbar_name, g_window_name, pos)
    g_capture.set(cv2.CAP_PROP_POS_FRAMES, frame)
    ret, frame = g_capture.read()
    if ret:
        cv2.imshow(g_window_name, frame)
        cv2.waitKey(33)


def main():
    global g_capture, g_slider_position, g_current_frame

    cv2.namedWindow(g_window_name, cv2.WINDOW_AUTOSIZE)
    g_capture = cv2.VideoCapture(video_path)

    # total frame count for video
    total_frames = int(g_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames != 0:
        cv2.createTrackbar(g_trackbar_name, g_window_name,
                           0, 100, onTrackbarSlide)

    while True:
        ret, frame = g_capture.read()

        if not ret:
            break

        g_current_frame += 1

        g_slider_position = int(g_current_frame / total_frames * 100)

        cv2.setTrackbarPos(g_trackbar_name, g_window_name, g_slider_position)

        cv2.imshow(g_window_name, frame)

        c = cv2.waitKey(33)
        if c == ord('q'):
            break

    g_capture.release()
    cv2.destroyAllWindows()
    for i in range(2):
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
