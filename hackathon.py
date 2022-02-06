#/Users/MT/Desktop/hackathon/mini.png
from PIL import Image, ImageEnhance
import math


path = "/Users/MT/Desktop/hackathon/hackathon/"#Path to folder with images
imageName = "50x50.png"#Name of image to convert to dice



def collage(diceArray, imageDimX, imageDimY):#Generate image collage
	new = Image.new("RGBA", (imageDimX*50,imageDimY*50))
	for i in range(imageDimX):
		for j in range(imageDimY):		
			val = diceArray
			img = Image.open(str(diceArray[i][j])+".png")
			#img = img.resize((500,500))
			new.paste(img, (i*50,j*50))

	new.save("visualization.png")

def generateArr(sizeX, sizeY, brightness):#Generate dice faces
	global path, imageName
	img = Image.open(path+imageName)
	gray_img = img.convert("L")
	pix = gray_img.load()
	imgArr = []
	for i in range(sizeX):
		temp = []
		for j in range(sizeY):
			val = math.ceil((pix[i,j]+brightness)/43)
			if val >= 7:
				val = 6
			if val == 0:
				val+=1
			temp.append(val)
		imgArr.append(temp)

	return imgArr



def dice_PNG_Resize():#Resize dice faces
	global path
	for i in range(1,7):
		img = Image.open(path+str(i)+".png")
		img.resize((50,50)).save(str(i)+".png")


def saveMuralVal(array):#Save image array as text file
	global array
	f = open("miniDice.txt","w") 
	for i in range(len(array)):
		for j in range(len(array[i])):
			f.write(str(array[i][j]) + " ")
		f.write("\n")

image = Image.open("mini.png")#Name of image
image.resize((50,50)).save("50x50.png")

diceVal = generateArr(50,50, 0)#Dimension of image
print (diceVal)
collage(diceVal, 50, 50)
