from camera.webcam import open_webcam, read_frame, release_webcam
from processing.skin_segmentation import segment_skin
from processing.contour_utils import find_largest_contour, draw_bounding_box
from utils.display import show_window
import cv2

def main():
    cap = open_webcam()

    while True:
        frame = read_frame(cap)

        mask = segment_skin(frame)
        contour = find_largest_contour(mask)
        draw_bounding_box(frame, contour)

        show_window("Skin detection", frame)
        show_window("Mask", mask)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    release_webcam(cap)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
