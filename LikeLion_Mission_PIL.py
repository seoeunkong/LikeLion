from PIL import Image
from PIL import ImageFilter

img = Image.open('Mission_PIL/image.jpg')
img_width, img_height = img.size 
print("이미지 확장자:", img.format)
print("이미지 가로길이:", img_width)
print("이미지 세로길이:", img.height)

resize_img = img.resize((100,100))
resize_img_width, resize_img_height = resize_img.size
print("변환 후 이미지 가로길이:", resize_img_width)
print("변환 후 이미지 세로길이:", resize_img.height)
resize_img.save('Mission_PIL/resize_img.jpg')

img = img.resize((400,400))

rotate_img = img.rotate(45)
rotate_img.save('Mission_PIL/rotate_img.jpg')

blur_img = img.filter(ImageFilter.BoxBlur(10))
blur_img.save('Mission_PIL/blur_img.jpg')

new_img = Image.new("RGB",(1000,1000),300000)
new_img.paste(img,(10,10))
new_img.paste(resize_img,(img.width+10,10))
new_img.paste(blur_img,(10,img.height+10))
new_img.paste(rotate_img,(img.width+10,img.height+10))
new_img.save('Mission_PIL/new_img.jpg')

new_img.show()
