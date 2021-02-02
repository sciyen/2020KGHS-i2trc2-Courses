import cv2
import numpy as np
def readImg(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  

    nums = []
    for i in range(len(contours)):
        if(hierarchy[0,i,3] == 0 and cv2.contourArea(contours[i]) > 20):
            x, y, w, h = cv2.boundingRect(contours[i])
            l = max(w, h)
            Sx = x - (l - w) // 2
            Sy = y - (l - h) // 2
            Mask = np.zeros((th.shape[0], th.shape[1]), dtype = np.uint8)
            Mask[y:y+h, x:x+w] = 255
            Mask2 = cv2.bitwise_not(Mask)
            masked = cv2.bitwise_and(th, th, mask = Mask)
            masked[Mask2 == 255] = 255
            tmp = masked[Sy:Sy+l, Sx:Sx+l]
            nums.append([x, tmp])
    
    nums_sorted = sorted(nums, key = lambda nums : nums[0])
    return nums_sorted

if __name__ == "__main__":
    test = readImg(r"imgs/99534.jpg")
    for i in range(len(test)):
        cv2.imshow('num', test[i][1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()