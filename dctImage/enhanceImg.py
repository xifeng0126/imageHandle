import cv2
import numpy as np
import os

def enhance_image(image):
    # 进行DCT变换
    dct_image = cv2.dct(np.float32(image))
    # 设置阈值，保留较低频率的系数
    threshold = 0.08
    mask = np.abs(dct_image) > threshold * np.max(np.abs(dct_image))
    filtered_dct_image = dct_image * mask
    # 进行IDCT逆变换
    enhanced_image = cv2.idct(filtered_dct_image)
    # 将图像转换为0-255的灰度图像
    enhanced_image = np.clip(enhanced_image, 0, 255)
    enhanced_image = np.uint8(enhanced_image)
    return enhanced_image

def enhance_image2(image):
    # 进行DCT变换
    dct_image = cv2.dct(np.float32(image))
    # 设置阈值，保留较低频率的系数
    threshold = 0
    mask = np.abs(dct_image) > threshold * np.max(np.abs(dct_image))
    filtered_dct_image = dct_image * mask
    # 进行IDCT逆变换
    enhanced_image = cv2.idct(filtered_dct_image)
    # 将图像转换为0-255的灰度图像
    enhanced_image = np.clip(enhanced_image, 0, 255)
    enhanced_image = np.uint8(enhanced_image)
    return enhanced_image

def do_enhance(image_path, output_path) -> str:
    picture_names = os.listdir(image_path)
    for pic_name in picture_names:
        # 读取原始图像
        image = cv2.imread(image_path + pic_name, cv2.IMREAD_GRAYSCALE)
        # 进行图像增强
        enhanced_image = enhance_image(image)
        enhanced_image2 = enhance_image2(image)
        cv2.imwrite(output_path+pic_name, cv2.subtract(enhanced_image2, enhanced_image))
    return output_path