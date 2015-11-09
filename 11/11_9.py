#PIL：python imaging library 。python的图像处理标准库。
#PIL仅支持到python2.7 ，有新的兼容版本支持python 3.x,就是Pillow
#1.操作图像
#例如缩放图像
from PIL import Image
im=Image.open('test.jpg')#打开一张图片，当前路径
w,h=im.size#获得图片尺寸
print('Original image size:%sx%s' %(w,h))
#缩放的50%
im.thumbnail((w/2,h/2))
print('Resize image to:%sx%s' % (w/2,h/2))
im.save('thumbnail2.png','png')#图像以png格式保存

#添加模糊效果
from PIL import Image,ImageFilter
im=Image.open('test.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')

#PIL的ImageDraw提供了很多绘图方法，可以直接绘图
#例如生成字母验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#随机字母
def rndChar():
	return chr(random.randint(65,90))
#随机颜色
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
width=80*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
font=ImageFont.truetype('SansPlateCaps.ttf',36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
	draw.text((80*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊 
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')