"""
    imageWorker.py
    Sets/Writes/Saves/Loads/Exports Images
    Written by: Divakar Lakhera
    BETA Version (ITS BUGGY BUT DOES THE JOB !)
    TODO:
        Add Tons of Error Handling
        Add Mutlithreading Support
        BugFixes
"""

import sys
import os
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import config as cfg
class imageWorker:
    def __init__(self):
        self.userConfig=cfg.config()
        self.font="../fonts/arial.ttf"    ## Font
        self.imageXmax=0 ## max width of image
        self.imageYmax=0  ## max height of image
        self.color=(0,0,0) ## Colour RGB
        self.exportParam="output/out.png"
    def loadImage(self,filename):
        ##  Write Exception Handling !
        self.fileImageOpened=Image.open(filename)
        ## Just hope it opens
        self.imageXmax,self.imageYmax=self.fileImageOpened.size

    def reloadImage(self,filename):
        del self.fileImageOpened
        ##  Write Exception Handling !
        self.fileImageOpened=Image.open(filename)
        ## Just hope it opens
        self.imageXmax,self.imageYmax=self.fileImageOpened.size

    def loadFont(self,fontpath):
        ## Load Font
        self.font = ImageFont.truetype(fontpath, self.userConfig.fontSize)
        ## Hope it loads

    def writeText(self,x,y,txt):
        drawimg=ImageDraw.Draw(self.fileImageOpened)
        drawimg.text((x,y),txt,font=self.font,fill=self.color)
        ##self.fileImageOpened.save(self.exportParam)

    def flush(self,filename):
        self.fileImageOpened.save(self.userConfig.outputFolder+"/"+filename);