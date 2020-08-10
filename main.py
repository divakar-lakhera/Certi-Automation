import sys
sys.path.append(".")
from imageLib import imageWorker as iWork
import config as cfg
import pandas as pd
from PIL import Image
import os
from barLoader import buildQR as bq
## Load User Configurations
userc=cfg.config()
## Load CSV file
rawdata=pd.read_csv(userc.datapack);
## OK
img=iWork.imageWorker()
img.loadFont(userc.fontLocation)
img.loadImage(userc.templateLocation)
print(img.imageXmax)
print(img.imageYmax)
name_table=[]
ctr=0
scode="NITUK/CSE/20/STTP/00"
for index, i in rawdata.iterrows():
    print(i)
    img.reloadImage(userc.templateLocation)
    cCode=scode+str(ctr)
    usr=""
    for j in userc.writeData:
        if(j[0]==userc.nameId):
            usr=i[j[0]]
            if(userc.checkForNamePrefix==True):
                i[j[0]]=i[userc.namePrefixId]+" "+i[j[0]]
        ## Calculate X coordinate from where to start printing to make sure text always get to center of feild.
        ## Calculate middle then shift it to right according to text size
        ## In some cases name might be bigger than feild size so force write form beginning
        xcal = (j[2] - j[1] - (len(i[j[0]]) * (userc.fontSize/2))) / 2;
        ## Text to big causing underflow .... re-adjust
        xcal = max(0, xcal) + j[1];
        ## Write
        img.writeText(xcal,j[3],i[j[0]].title())
        ##
    ## Flush Buffer
    img.flush("CERT"+str(ctr)+"_"+usr+".png");
    bq(cCode,"BCDE"+str(ctr)+".png")
    ## Merge Barcode
    barcodeImage=Image.open(userc.outputFolder+"/"+"BCDE"+str(ctr)+".png")
    certi=Image.open(userc.outputFolder+"/"+"CERT"+str(ctr)+"_"+usr+".png")
    certi.paste(barcodeImage, (60, 70)) ## Set It
    certi.save(userc.outputFolder+"/"+"CERT_FINAL"+str(ctr)+"_"+usr+".png", quality=100)
    ## REMOVE Temp
    os.remove(userc.outputFolder+"/"+"BCDE"+str(ctr)+".png")
    os.remove(userc.outputFolder+"/"+"CERT"+str(ctr)+"_"+usr+".png")
    ctr+=1;


exit()







