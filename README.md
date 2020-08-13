

# Certi-Automation
> Automates certificate generation for colleges and school events
> 
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) [![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/contributors/) 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)

# How to install:
> Clone the repo 

    git clone https://github.com/divakar-lakhera/Certi-Automation.git

	
	

> Configure config.py

    ## Set CSV file to read from
    self.datapack="data_final.csv"  
    
    ## Set Template for Certificates
    self.templateLocation="template/template_final.png"  
	
	## Set Font Location, Size, Color
    self.fontLocation="fonts/roboto/roboto-Bold.ttf"
    self.fontSize=75
    self.fontColor=(255,255,255)   #RGB

	## Set output folder
    self.outputFolder="output/"

>Set field names in config.py`
>Setting field dimensions is bit tricky and is explained afterwards.

    self.writeData=[
            ##
            ## (Feild Name, X index Min, X index Max, Y index)
            ## Feild name is used to fetch data from CSV and write it on certificate.
            ##
            ("Name",1440,3150,1035),
            ("College Name",253,2399,1184),
            ("Topic of Lecture",400,3000,1615)
        ]

> Run the Program
	
	python main.py

# Field Names and Dimensions
Since different certificates have different formats, we need to define a custom dimensions for every field we need to fill.
Field Names refer to the column name (in CSV file) from which corresponding data will be taken for example a CSV file with data:
|  Name|College |
|--|--|
| Person A| Some College  |
| Person B| Some College  |

Here in table above field names are "Name" and "College".

## How to set dimensions for field

> Setting dimensions is tricky and may require a brute force approach.
> 
> Warning: Setting wrong dimensions may cause program to give unexpected results.
> 
* For example the image given below:

![enter image description here](https://github.com/divakar-lakhera/Certi-Automation/blob/master/template_withSign.png)

****The dimensions for "Name" field will be [x-indexMin(x-start) ,x-indexMax(x-end), y-index(starting from top of certificate) ]***.*

> Tip: Take top right corner of certificate as (0,0) (x,y).

 ## TODOs
 

 - Add SMTP protocol for automatic certificate delivery via Email.
 - Add UI for better user experience and ease.
 - Add exception handling
 - Add Barcode Support :heavy_check_mark:
 - Add Requirements.txt file
