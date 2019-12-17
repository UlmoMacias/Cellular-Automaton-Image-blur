#import cv2
import numpy
from PIL import Image
from random import randint,random
import time


def getColorHash(rgbValues):
	return rgbValues[0] + rgbValues[1] + rgbValues[2]


def verificaVecinos(actualMatrix,iniX,iniY):
	suma = 0
	for x in range(iniX-1,iniX+1):
		for y in range(iniY-1,iniY+1):
			if actualMatrix[x,y]!= None and getColorHash(actualMatrix[x,y])>= 500 :
			#if actualMatrix[x,y]!= None:
				suma += getColorHash(actualMatrix[x,y])
	#print(suma)
	return suma



def evoluciona(newMatrix,actualMatrix,x,y):
	#(int,int,int) 256
	#Decides respecto a la actualMatrix y actualizas en newMatrix
	# c = r + +
	ownColorHash = getColorHash(actualMatrix[x,y])
	#print(actualMatrix[x,y])
	#si el pixel esta vivo
	if ownColorHash >= 500:
		if verificaVecinos(actualMatrix,x,y) < 1000 or verificaVecinos(actualMatrix,x,y) > 2295 :
			# pixel pierde cant random de un color random, hasta
			# que el color Hash sea menor a 500
			aux = ownColorHash
			while aux >= 500:
				#print("While presente!")
				randomColor = randint(0,2)
				random1 =randint(0,23)

				if randomColor == 0:
					if actualMatrix[x,y][0]- random1 < 0:
						newMatrix[x,y] = (0,actualMatrix[x,y][1],actualMatrix[x,y][2])
					else:	
						newMatrix[x,y] = (actualMatrix[x,y][0]- random1,actualMatrix[x,y][1],actualMatrix[x,y][2])

				elif randomColor == 1:
					if actualMatrix[x,y][1]- random1 < 0:
						newMatrix[x,y] = (actualMatrix[x,y][0],0,actualMatrix[x,y][2])
					else:
						newMatrix[x,y] = (actualMatrix[x,y][0],actualMatrix[x,y][1]- random1,actualMatrix[x,y][2])

				elif randomColor == 2:
					if actualMatrix[x,y][2]- random1 < 0:
						newMatrix[x,y] = (actualMatrix[x,y][0],actualMatrix[x,y][1],0)					
					else:
						newMatrix[x,y] = (actualMatrix[x,y][0],actualMatrix[x,y][1],actualMatrix[x,y][2]- random1)					

				aux = getColorHash(newMatrix[x,y])

	#de otra forma estara muerto
	else:
		if verificaVecinos(actualMatrix,x,y) >= 500 and verificaVecinos(actualMatrix,x,y) <= 755:
		#pixel incrementa cant random de un color random, hasta
			#que el color Hash sea mayor o igual a 500
			aux = ownColorHash
			while aux < 500:
				#print("While presente!")
				randomColor = randint(0,2)
				random1 =randint(0,23)
				if randomColor == 0:
					if actualMatrix[x,y][0]+ random1 > 255:
						newMatrix[x,y] = (255 ,actualMatrix[x,y][1],actualMatrix[x,y][2])
					else:
						newMatrix[x,y] = (actualMatrix[x,y][0]+ random1 ,actualMatrix[x,y][1],actualMatrix[x,y][2])

				elif randomColor == 1:
					if actualMatrix[x,y][1]+ random1 > 255:
						newMatrix[x,y] = (actualMatrix[x,y][0],255,actualMatrix[x,y][2])
					else:
						newMatrix[x,y] = (actualMatrix[x,y][0],actualMatrix[x,y][1]+ random1,actualMatrix[x,y][2])

				elif randomColor == 2:
					if actualMatrix[x,y][2]+ random1 > 255:
						newMatrix[x,y] = (actualMatrix[x,y][0],actualMatrix[x,y][1],255)					
					else:
						newMatrix[x,y] = (actualMatrix[x,y][0],actualMatrix[x,y][1],actualMatrix[x,y][2]+ random1)					

				aux = getColorHash(newMatrix[x,y])

	#print(newMatrix[x,y])
	#print("./././././././././././././")
	return newMatrix


def generacion(matriz):
	print("generacion")
	newMatrix = matriz
	for x in range(0,imgLength):
		for y in range(0,imgWidth):
			#print(imageMatrix[x,y])
			newMatrix = evoluciona(newMatrix,matriz,x,y)
			#matriz = newMatrix
		#print('Acabe un renglon!')
	return newMatrix

# Metodo main
def __main__():
	imageMatrix = img.load()
	start_time = time.time()
	#Change range here to change number of epochs.
	for x in range(1,2):
		print(str(x))
		imageMatrix = generacion(imageMatrix)
		
	end = time.time()
	print('Time taken, program: ', end - start_time)
	#Change here image name: 
	img.save("newImage.png")
	
	

###########################################################################################################
###########################################################################################################
#############			Global config 			###########################################################
###########################################################################################################
###########################################################################################################


#img = Image.open('imgpeque.jpg')
img = Image.open('imagen3.jpg')
print("#######################################")
print(img.format, img.size, img.mode)	
imgLength = img.size[0]
print("Width is " + str(imgLength))
imgWidth = img.size[1]
print("Lenght is " + str(imgWidth))
print("#######################################")
imageMatrix = img.load()

__main__()

