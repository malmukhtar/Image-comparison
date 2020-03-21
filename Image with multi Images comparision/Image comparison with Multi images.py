import numpy as np
import cv2
from os import listdir

# printing a brief of the function of the script
print("\n \n \n \n This app compares between an image and a set of images and returns the image with the highest similarity percentage \n \n \n \n")

# asking for the image path
image_path = input("Enter the Image path: ")

# asking for path of the set of images 
set_path = input("Enter the path of the folder that contains the set of images: ") 

# loading the image and getting the images in folder
image = cv2.imread(image_path)
images = listdir(set_path)

# Definig the comparsion function 
def comparsion(Image1,Image2):
    #make them gray
    try:
        SGray = cv2.cvtColor(Image1, cv2.COLOR_BGR2GRAY)
    except:
        print("Unable to load the image 1, Please check the entered path.")   
    
    try:
        RGray = cv2.cvtColor(Image2, cv2.COLOR_BGR2GRAY)
    except:
        print("Unable to load the image 2, Please check the entered path.")
    


    #apply erosion
    kernel = np.ones((2, 2),np.uint8)
    SErosion = cv2.erode(SGray, kernel, iterations = 1)
    RErosion = cv2.erode(RGray, kernel, iterations = 1)


    #retrieve edges with Canny
    thresh = 175
    SEdges = cv2.Canny(SErosion, thresh, thresh*2)
    REdges = cv2.Canny(RErosion, thresh, thresh*2)


    #extract contours
    SContours, Shierarchy = cv2.findContours(SEdges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    RContours, Rhierarchy = cv2.findContours(REdges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    return (cv2.matchShapes(RContours[0],SContours[0],cv2.CONTOURS_MATCH_I1, 0.0))

# defining the results array
results = []

# checking if path ends with \ and if not add it
if set_path.endswith('\\'):
    pass
else:
    set_path = set_path + '\\'

# Looping through the referance shapes
for img in images:
    image2 = cv2.imread(set_path+img)
    results.append(comparsion(image,image2))
    
# Display result
print('\n \n \n \n===================================================================================\n \n \n \nThe image with the highest similarity percentage is: ' + set_path + images[results.index(min(results))]+ '\n \n \n \n===================================================================================\n \n \n \n')
