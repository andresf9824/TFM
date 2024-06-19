#Importar Librerias necesarias

from ij import IJ
import os
from ij.io import DirectoryChooser



#Funcion para aplicar umbralización automática:
def umbralizacion_automatica(imagen):
    IJ.setAutoThreshold(imagen, "Default")
    IJ.run(imagen, "Convert to Mask","")
    return imagen
    
#Funcion para aplicar operacion morfologica outline:
def outline(imagen):
	IJ.run(imagen, "Outline", "")
	return imagen

	
#Funcion para aplicar operacion morfologica fill holes:
def fill_holes(imagen):
	IJ.run(imagen, "Fill Holes", "")
	return imagen

	
#Funcion para aplicar operacion morfologica erosion:

def erode(imagen):
	IJ.run(imagen,"Erode", "")
	return imagen
	
#Funcion para aplicar  median:
def median(imagen,radio):
	IJ.run(imagen,"Median","radius=" + str(radio))
	return imagen
	

# Rutas de las carpetas de entrada y salida
carpeta_original = ""
carpeta_destino = ""

# Obtener la lista de archivos en la carpeta original
datasets = os.listdir(carpeta_original)
	
for imagenes in datasets:
    # Construir la ruta completa de la imagen original
    ruta_imagen = os.path.join(carpeta_original, imagenes)
        
    # Abrir cada una de las imagenes originales
    imagen_original = IJ.openImage(ruta_imagen)
    
       
    # Llamamos a nuestra funcion de umbralización
    imagen_umbralizada = umbralizacion_automatica(imagen_original)
    
    #Llamamos a nuestra funcion outline
    
    morfologica_outline= outline(imagen_umbralizada)
    
    
    #Llamamos a nuestra funcion fill holes
    
    llenar_espacios= fill_holes(morfologica_outline)
    
    
    #Llamamos a nuestra funcion de erosion
    
    
    erosion=erode(llenar_espacios)
    
    #Llamamos a nuestra funcion median
    
    media= median(erosion, 13)
    
    
    imagen_final= media
    
    # Guardar la imagen umbralizada en la misma carpeta de destino con el mismo nombre
    IJ.saveAs(imagen_final,"jpg", os.path.join(carpeta_destino, imagenes))

