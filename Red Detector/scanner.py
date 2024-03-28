import cv2

def detect_red(file):
    count = 0
    try:
        print(f"File size of {file}: {count_pixels(file)}")
        img = cv2.imread(file, 1)
    except(TypeError()):
        print("File not found")
    else:
        for row in img:
            for pixel in row:
                if pixel[2] > 200 and pixel[1] < 100 and pixel[0] < 100:
                    count += 1
    finally:
        print(f"{count} red pixels counted")

def count_pixels(file):
    img = cv2.imread(file)


    return len(img) * len(img[0])


detect_red("assets/white.jpg")
detect_red("assets/Color-blue.JPG")
detect_red("assets/Red_Color.jpg")
detect_red("assets/gren.jpg")
detect_red("assets/redball.png")