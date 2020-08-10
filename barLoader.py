import sys
sys.path.append(".")
import config as cfg
from PIL import Image
import treepoem
def buildQR(dat,fout):
    userConfig = cfg.config()
    image = treepoem.generate_barcode(barcode_type='qrcode',data=dat,)
    image = image.resize((260, 260))
    image.convert('1').save(userConfig.outputFolder+"/"+fout)