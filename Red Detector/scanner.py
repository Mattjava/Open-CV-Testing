import cv2

def detect_red(file):
    count = 0
    print(f"File size of {file}: {count_pixels(file)}")
    img = cv2.imread(file, 1)
    for row in img:
        for pixel in row:
            if pixel[2] > 200 and pixel[1] < 100 and pixel[0] < 100:
                count += 1
    print(f"{count} red pixels counted")

def count_pixels(file):
    img = cv2.imread(file)


    return len(img) * len(img[0])


detect_red("assets/img.png")