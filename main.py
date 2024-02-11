import cv2, numpy, os

def loadImage(filename: str="example.jpg"):
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray

if __name__ == '__main__':
    filepath = "content/Scanner/"
    for name in os.listdir(filepath):
        print(loadImage(filepath+name).shape)
