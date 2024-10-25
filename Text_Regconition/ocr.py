import cv2
import pytesseract as pt
import PIL
from PIL import Image
import numpy as np

#Thiết lập đường dẫn thực thi của Tesseract OCR
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Định nghĩa đường dẫn file ảnh
file = r'D:\Python_File\Text_Regconition\IMG\img.png'
#Mở hình ảnh sử dụng thư viên PIL
raw_img = Image.open(file)

#Hảm xử lý hình ảnh trích xuất từ văn bản
def ocr_core(img):
    text = pt.image_to_string(img)
    return text

raw_img_np = np.array(raw_img) #Chuyển ảnh sang mảng để có thể xử lý bằng openCV

if raw_img is None:
    print("Lỗi: không tìm thấy ảnh") #Nếu không thể tải hình ảnh -> báo lỗi
else:
    #Chuyển đổi ảnh sang thang độ xám
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Loại bỏ nhiễu trong ảnh
    def remove_noise(image):
        return cv2.medianBlur(image, 5)
    #Hàm áp dụng ngưỡng(threshold) để phân đoạn ảnh
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    #Xử lý ảnh với các hàm đã định nghĩa
    proc_img = get_grayscale(raw_img_np)
    proc_img = thresholding(proc_img)
    proc_img = remove_noise(proc_img)

    print(ocr_core(proc_img))