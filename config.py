"""
    config.py
    Written By: Divakar Lakhera
    Contains Main Configuration Information Required For Automation
    WARNING: Setting Wrong Values in Config can lead to unexpected results or even crash
             Change only if you know what to do.

"""

class config:
    def __init__(self):
        ## Mail Config
        self.senderMailId=""
        self.senderMailPassword=""
        self.senderSubject="Certificate for participation"
        self.smtpServer="smtp.gmail.com"  ## SMTP Server of Gmail
        self.port="587"
        ## CSV Parser Config
        self.datapack="data_final.csv"   ## Default CSV file if not provided
        self.templateLocation="template/temp_bar.png"
        self.fontLocation="fonts/roboto/roboto-Bold.ttf"
        self.fontSize=75
        self.fontColor=(255,255,255)   #RGB
        self.outputFolder="output/"
        self.loadDefaultDataPack=True   ## Enabled Due to Debugging (loads self.datapack)
        self.autoEmailsend=False  ## Automatically send Emails to the people with certificate
        self.checkForNamePrefix=False
        ## TABLE DATA TO FETCH FEILDS
        self.namePrefixId="Name Prefix"
        self.nameId="Name"
        self.genderFeild="Gender"
        self.emailFeild="Email"
        self.writeData=[
            ##
            ## (Feild Name, X index Min, X index Max, Y index)
            ## Feild name is used to fetch data from CSV and write it on certificate.
            ##
            ("Name",1440,3150,1026),
            ("College Name",253,2399,1175),
            #("Topic of Lecture",400,3000,1615)
        ]
