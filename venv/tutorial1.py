from PIL import Image
from PIL import Image, ImageDraw
from PIL import Image, ImageEnhance

#Opens the demo image in file
image1 = Image.open("demo_image.jpg")

#File Format
print(image1.format)

#The Pixel Format by the image
print(image1.mode)

#Pixel Dimenstions of Image
print(image1.size)

#Colour Pallete
print(image1.palette)

#Changing name and file formate of orginal image
image1.save("new_image.png")

#Resizeing Image
image2 = image1.resize((800,800))
image2.save("image_800.jpg")

print(image1.size)
print(image2.size)

#Fix Aspect Ratio
#image1.thumbnail((800,800))
#image1.save("image_thumbnail.jpg")

#print(image1.size)

#Cropping an image
box = (300,200,700,500) #(left,upper,right,lower) (left,upper) = upper left coordinate and (right,lower) = lower right coordinate
cropped_image = image1.crop(box)
cropped_image.save("cropped_image.jpg")
print(cropped_image.size)

cropped_image.show()

#Applying a water mark
image_copy = image1.copy()
logo = Image.open("logo.png")
position = ((image_copy.width-logo.width),(image_copy.height-logo.height))
image_copy.paste(logo,position,logo)
image_copy.save("pasted_image.jpg")

#rotation of image
image90 = image1.rotate(90)
image90.save("image_rot_90.jpg")

image180 = image1.rotate(180)
image180.save("image_rot_180.jpg")

image90.rotate(20,expand=True).save("image_rot_110.jpg")

#Flip Image
image_flip = image1.transpose(Image.FLIP_LEFT_RIGHT)
image_flip.save("image_flip.jpg")

image_flip.show()

#Drawing on Image
canvas = Image.new("RGB",(400,300),"black")
img_draw = ImageDraw.Draw(canvas)
img_draw.rectangle((70,50,270,200),outline="red",fill="purple")
img_draw.text((70,250),"Wazz Up",fill = "purple")
canvas.save("drawn_image.jpg")
canvas.show()

#Grey Scale
greyscale_image = image1.convert("L")
greyscale_image.save("greyscale_image.jpg")

print(image1.mode)
print(greyscale_image.mode)

#Splitting and Mergin Bands
red,green,blue = image1.split()
print(image1.mode)
print(red.mode)
print(green.mode)
print(blue.mode)

new_image = Image.merge("RGB", (blue, red, green))
new_image.save('new_image.jpg')
new_image.show()

#Image Color Enhancement
contrast = ImageEnhance.Contrast(image1)
contrast.enhance(2).save("contrast.jpg")
contrast.show()