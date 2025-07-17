import cv2

def apply_gaussian_blur(image, kernel_size=(5,5), sigma=0):
    return cv2.GaussianBlur(image, kernel_size, sigma)

def apply_median_blur(image, ksize=5):
    return cv2.medianBlur(image, ksize)

def apply_canny(image, low_threshold=50, high_threshold=150):
    return cv2.Canny(image, low_threshold, high_threshold)
