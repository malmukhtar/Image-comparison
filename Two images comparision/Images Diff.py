import numpy as np
import cv2

Image1_path = input("Enter the Image 1 path: ")
Image2_path = input("Enter the Image 2 path: ") 

Image1 = cv2.imread(Image1_path)
Image2 = cv2.imread(Image2_path)

# Definig the comparsion function 
def comparsion(Image1,Image2):
    #make them gray
    try:
        SGray = cv2.cvtColor(Image1, cv2.COLOR_BGR2GRAY)
    except:
        print("Unable to load the image 1, Please check the entered path.")   
    
    try:
        RGray = cv2.cvtColor(Image2, cv2.COLOR_BGR2GRAY)
    except expression as identifier:
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

print(comparsion(Image1,Image2))