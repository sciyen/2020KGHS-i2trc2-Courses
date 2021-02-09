import cv2
import numpy as np

#呼叫時引數是圖片的路徑
#會將圖片中的字切成一個一個的圖片
#回傳一個依據 x 座標排序好的 list，內容是 [[x座標0,圖片0],[x座標1,圖片1],......]
def readImg(path):
    #以灰階格式讀圖片進來
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #二值化
    ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #找輪廓
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
    #存個別的數字圖及其左上角x座標
    nums = []
    #對每條輪廓做處理
    for i in range(len(contours)):
        #篩選掉面積太小或在其他輪廓內的輪廓
        if(hierarchy[0,i,3] == 0 and cv2.contourArea(contours[i]) > 20):
            #找到這條輪廓外的最小長方形
            x, y, w, h = cv2.boundingRect(contours[i])
            #算出這條輪廓外的最小正方形 (Sx, Sy, l, l)
            l = max(w, h)
            Sx = x - (l - w) // 2
            Sy = y - (l - h) // 2
            #做一個 Mask ，長方形區域為白色，其餘區域黑色
            Mask = np.zeros((th.shape[0], th.shape[1]), dtype = np.uint8)
            Mask[y:y+h, x:x+w] = 255
            #做另一個 Mask2，和 Mask 剛好相反
            Mask2 = cv2.bitwise_not(Mask)
            #把 Mask 和二值化過的圖 and 起來
            masked = cv2.bitwise_and(th, th, mask = Mask)
            #將 在最小正方形內，但不在最小長方形內 的區域也填成白色
            masked[Mask2 == 255] = 255
            #把長方形左上角座標和截下來的正方形放到 nums 中
            tmp = masked[Sy:Sy+l, Sx:Sx+l]
            nums.append([x, tmp])
    
    #依據 x 座標將數字圖片排序
    nums_sorted = sorted(nums, key = lambda nums : nums[0])
    return nums_sorted

if __name__ == "__main__":
    test = readImg(r"imgs/99543.jpg")
    for i in range(len(test)):
        cv2.imshow('num', test[i][1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()