import cv2

def show_window(name, image, width=600, height=400):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, width, height)
    cv2.imshow(name, image)
