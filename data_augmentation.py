# -*- coding: UTF-8 -*-
#
# Create by Li on 2022年11月21日
import os
import random
import augly.image as imaugs
import PIL.Image as Image

img_path = "Image"    # 需要增强的图像路径
save_path = "Result"  # 保存路径

def augly_augmentation(aug_image):
    aug = [
        imaugs.blur(aug_image,radius=random.randint(1,9)),                     # 图像模糊
        imaugs.brightness(aug_image,factor=random.uniform(0.1,2.0)),           # 改变亮度
        imaugs.change_aspect_ratio(aug_image, ratio=random.uniform(0.8,1.5)),  # 改变图像宽高比
        imaugs.color_jitter(aug_image, brightness_factor=random.uniform(0.8,1.5), contrast_factor=random.uniform(0.8,1.5), saturation_factor=random.uniform(0.8,1.5)),    # 颜色晃动
        imaugs.crop(aug_image, x1=random.uniform(0,0.1), y1=random.uniform(0,0.1), x2=random.uniform(0.9,1), y2=random.uniform(0.9,1)),     # 随机裁剪
        imaugs.hflip(aug_image),                                               # 水平翻转
        imaugs.opacity(aug_image, level=random.uniform(0.5,1)),                # 改变图像透明度
        imaugs.pixelization(aug_image, ratio=random.uniform(0.5,1)),           # 马赛克
        imaugs.random_noise(aug_image),                                        # 随机噪声
        imaugs.rotate(aug_image, degrees=random.randint(3,10)),                # 随机旋转一定角度
        imaugs.shuffle_pixels(aug_image, factor=random.uniform(0,0.1)),        # 随机像素比任意化
        imaugs.saturation(aug_image, factor=random.uniform(1,1.5)),            # 改变饱和度
        imaugs.contrast(aug_image, factor=random.uniform(1,1.5)),              # 对比度增强
        imaugs.grayscale(aug_image),                                           # 转灰度
        imaugs.meme_format(aug_image,text="hello world",caption_height=50),    # 在图片上方创建一个区域写上文字
        imaugs.overlay_emoji(aug_image),                                       # 在图片中添加表情
        imaugs.overlay_stripes(aug_image, line_width=random.uniform(0,0.1)),   #在图像中间加个横条
        imaugs.overlay_text(aug_image),                                        # 在图片中添加文字
        imaugs.perspective_transform(aug_image),                               #透视变换
        imaugs.sharpen(aug_image, factor=random.uniform(1.5,2.0))              #锐化
    ]
    return random.choice(aug)                                                   # 从以上函数中随机选其一进行数据增强

for name in os.listdir(img_path):
    aug_image = Image.open(os.path.join(img_path,name))
    count = 2                          # 每张图片需要增强的数量
    for i in range(count):
        image = augly_augmentation(aug_image)
        image = image.convert("RGB")
        image.save(os.path.join(save_path,name[:-4]+"_{}.jpg".format(i)))



