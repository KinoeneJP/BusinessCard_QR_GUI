#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import qrcode

import NameCard

def English():
    myCard.setEng() #print('English')
    genvcf()
    genqr()

def Japanese():
    myCard.setJap() #print('Japanese')
    genvcf()
    genqr()
    
def genvcf():
    myCard.nPrefix = [nPrefix1.get(),nPrefix2.get()]
    myCard.nFormat = [f'{nFamily1.get()} {nFirst1.get()}',f'{nPrefix2.get()} {nFirst2.get()} {nMiddle2.get()} {nFamily2.get()}, {nSuffix2.get()}']
    myCard.nFamily = [nFamily1.get(),nFamily2.get()]
    myCard.nFamPho = [nFamilyF1.get(),'']
    myCard.nFirst  = [nFirst1.get(),nFirst2.get()]
    myCard.nFirPho = [nFirstF1.get(),'']
    myCard.nMiddle = ['',nMiddle2.get()]
    myCard.nNick   = [nNick1.get(),nNick2.get()]
    myCard.nSuffix = ['',nSuffix2.get()]
    myCard.cName   = [nCompany1.get(),nCompany2.get()]
    myCard.cOrg    = [nOrg1.get(),nOrg2.get()]
    myCard.cTitle  = [nTitle1.get(),nTitle2.get()]
    myCard.cCntry  = ['',nCountry2.get()]
    myCard.cZip    = [nZip1.get(),nZip1.get()]
    myCard.cAdd    = [nAddress1.get(),nAddress2.get()]
    myCard.aPhone  = [nTel1.get(),nTel2.get()]
    myCard.aMobile = [nCel1.get(),nCel2.get()]
    myCard.aFax    = [nFax1.get(),nFax2.get()]
    myCard.aEmail  = [nMail1.get(),nMail1.get()]
    myCard.aUrl    = [nUrl1.get(),nUrl2.get()]
    myCard.isPhonetixJ = False if (myCard.nFirPho == '' and myCard.nFamPho =='') else True
    if myCard.isJ == True and myCard.isE == False:
        myCard.genVCFJ()
    elif myCard.isJ == False and myCard.isE == True:
        myCard.genVCFE()

def genqr():
#    print(myCard.vcf)
    myCard.qr = qrcode.make(myCard.vcf, box_size = 4)

def showqr(var, indx, mode):
    global qr_img
    genvcf()
    genqr()
    qr_img = ImageTk.BitmapImage(myCard.qr, master = qframe)
    canvas.create_image(0, 0, image = qr_img, anchor = tk.NW)


# initialization
size = '1200x750'
pad  = 5
isEng = 0
font1 = ('Meiryo',10)
font2= ('Meiryo',12, 'bold')
myCard = NameCard.NameCard()

# Window Definition
root = tk.Tk()
root.geometry(size)
root.resizable(False, False)
root.title(u'Business Card QR Code Generator')

# Language Selection Flame
labelframetext = u'作る名刺はどちらですか? Select Business Card Language'
langframe = tk.LabelFrame(root, text = labelframetext, width = 600, height = 30, borderwidth = 3, font=font1)
langframe.pack(anchor = tk.W, padx = pad, pady = pad)

# Radio Button for Language Select
lang = tk.IntVar()
lang.set(0)
radio1 = tk.Radiobutton(langframe, value=0, variable=lang, text=u'日本語(Japanese)', command = Japanese, font=font2)
radio2 = tk.Radiobutton(langframe, value=1, variable=lang, text=u'英語(English)', command = English, font=font2)

# Place Radio Button
radio1.grid(row = 0, column = 0, padx = 30)
radio2.grid(row = 0, column = 1, padx = 30)

# Inpurt Flame
iframe = tk.LabelFrame(root, text = u'Input Field', width = 600, height = 550, borderwidth = 3, font=font1)
iframe.pack(side = tk.LEFT, padx = pad, fill = tk.Y)

label00_1 = tk.Label(iframe, text = u'日本語(Japanese)', font=font1)
label00_2 = tk.Label(iframe, text = u'英語(English)', font=font1)
label01_0 = tk.Label(iframe, text = u'工学博士など', font=font1)
label02_0 = tk.Label(iframe, text = u'氏 Family Name', font=font1)
label03_0 = tk.Label(iframe, text = u'氏 ふりがな', font=font1)
label04_0 = tk.Label(iframe, text = u'名 First Name', font=font1)
label05_0 = tk.Label(iframe, text = u'名 ふりがな', font=font1)
label06_0 = tk.Label(iframe, text = u'Middle Name', font=font1)
label07_0 = tk.Label(iframe, text = u'Nick Name', font=font1)
label08_0 = tk.Label(iframe, text = u'Suffix', font=font1)
label09_0 = tk.Label(iframe, text = u'会社名', font=font1)
label10_0 = tk.Label(iframe, text = u'部署名', font=font1)
label11_0 = tk.Label(iframe, text = u'職位 Title', font=font1)
label12_0 = tk.Label(iframe, text = u'会社住所', font=font1)
label13_0 = tk.Label(iframe, text = u'〒(Zip)', font=font1)
label14_0 = tk.Label(iframe, text = u'国名', font=font1)
label15_0 = tk.Label(iframe, text = u'固定電話', font=font1)
label16_0 = tk.Label(iframe, text = u'携帯電話', font=font1)
label17_0 = tk.Label(iframe, text = u'FAX', font=font1)
label18_0 = tk.Label(iframe, text = u'E-Mail', font=font1)
label19_0 = tk.Label(iframe, text = u'Web URL', font=font1)

nPrefix1 = tk.StringVar()
nPrefix1.set('')
nPrefix1.trace_add('write', showqr)
nPrefix2 = tk.StringVar()
nPrefix2.set('')
nPrefix2.trace_add('write', showqr)
nFamily1 = tk.StringVar()
nFamily1.set('')
nFamily1.trace_add('write', showqr)
nFamily2 = tk.StringVar()
nFamily2.set('')
nFamily2.trace_add('write', showqr)
nFamilyF1 = tk.StringVar()
nFamilyF1.set('')
nFamilyF1.trace_add('write', showqr)
nFirst1 = tk.StringVar()
nFirst1.set('')
nFirst1.trace_add('write', showqr)
nFirst2 = tk.StringVar()
nFirst2.set('')
nFirst2.trace_add('write', showqr)
nFirstF1 = tk.StringVar()
nFirstF1.set('')
nFirstF1.trace_add('write', showqr)
nMiddle2 = tk.StringVar()
nMiddle2.set('')
nMiddle2.trace_add('write', showqr)
nNick1 = tk.StringVar()
nNick1.set('')
nNick1.trace_add('write', showqr)
nNick2 = tk.StringVar()
nNick2.set('')
nNick2.trace_add('write', showqr)
nSuffix2 = tk.StringVar()
nSuffix2.set('')
nSuffix2.trace_add('write', showqr)
nCompany1 = tk.StringVar()
nCompany1.set('')
nCompany1.trace_add('write', showqr)
nCompany2 = tk.StringVar()
nCompany2.set('')
nCompany2.trace_add('write', showqr)
nOrg1 = tk.StringVar()
nOrg1.set('')
nOrg1.trace_add('write', showqr)
nOrg2 = tk.StringVar()
nOrg2.set('')
nOrg2.trace_add('write', showqr)
nTitle1 = tk.StringVar()
nTitle1.set('')
nTitle1.trace_add('write', showqr)
nTitle2 = tk.StringVar()
nTitle2.set('')
nTitle2.trace_add('write', showqr)
nAddress1 = tk.StringVar()
nAddress1.set('')
nAddress1.trace_add('write', showqr)
nAddress2 = tk.StringVar()
nAddress2.set('')
nAddress2.trace_add('write', showqr)
nZip1 = tk.StringVar()
nZip1.set('')
nZip1.trace_add('write', showqr)
nCountry2 = tk.StringVar()
nCountry2.set('')
nCountry2.trace_add('write', showqr)
nTel1 = tk.StringVar()
nTel1.set('')
nTel1.trace_add('write', showqr)
nTel2 = tk.StringVar()
nTel2.set('')
nTel2.trace_add('write', showqr)
nCel1 = tk.StringVar()
nCel1.set('')
nCel1.trace_add('write', showqr)
nCel2 = tk.StringVar()
nCel2.set('')
nCel2.trace_add('write', showqr)
nFax1 = tk.StringVar()
nFax1.set('')
nFax1.trace_add('write', showqr)
nFax2 = tk.StringVar()
nFax2.set('')
nFax2.trace_add('write', showqr)
nMail1 = tk.StringVar()
nMail1.set('')
nMail1.trace_add('write', showqr)
nUrl1 = tk.StringVar()
nUrl1.set('')
nUrl1.trace_add('write', showqr)
nUrl2 = tk.StringVar()
nUrl2.set('')
nUrl2.trace_add('write', showqr)

entry01_1 = tk.Entry(iframe, textvariable = nPrefix1, font=font1)
entry01_2 = tk.Entry(iframe, textvariable = nPrefix2, font=font1)
entry02_1 = tk.Entry(iframe, textvariable = nFamily1, font=font1)
entry02_2 = tk.Entry(iframe, textvariable = nFamily2, font=font1)
entry03_1 = tk.Entry(iframe, textvariable = nFamilyF1, font=font1)
entry04_1 = tk.Entry(iframe, textvariable = nFirst1, font=font1)
entry04_2 = tk.Entry(iframe, textvariable = nFirst2, font=font1)
entry05_1 = tk.Entry(iframe, textvariable = nFirstF1, font=font1)
entry06_2 = tk.Entry(iframe, textvariable = nMiddle2, font=font1)
entry07_1 = tk.Entry(iframe, textvariable = nNick1, font=font1)
entry07_2 = tk.Entry(iframe, textvariable = nNick2, font=font1)
entry08_2 = tk.Entry(iframe, textvariable = nSuffix2, font=font1)
entry09_1 = tk.Entry(iframe, textvariable = nCompany1, font=font1)
entry09_2 = tk.Entry(iframe, textvariable = nCompany2, font=font1)
entry10_1 = tk.Entry(iframe, textvariable = nOrg1, font=font1)
entry10_2 = tk.Entry(iframe, textvariable = nOrg2, font=font1)
entry11_1 = tk.Entry(iframe, textvariable = nTitle1, font=font1)
entry11_2 = tk.Entry(iframe, textvariable = nTitle2, font=font1)
entry12_1 = tk.Entry(iframe, textvariable = nAddress1, font=font1)
entry12_2 = tk.Entry(iframe, textvariable = nAddress2, font=font1)
entry13_1 = tk.Entry(iframe, textvariable = nZip1, font=font1)
entry14_2 = tk.Entry(iframe, textvariable = nCountry2, font=font1)
entry15_1 = tk.Entry(iframe, textvariable = nTel1, font=font1)
entry15_2 = tk.Entry(iframe, textvariable = nTel2, font=font1)
entry16_1 = tk.Entry(iframe, textvariable = nCel1, font=font1)
entry16_2 = tk.Entry(iframe, textvariable = nCel2, font=font1)
entry17_1 = tk.Entry(iframe, textvariable = nFax1, font=font1)
entry17_2 = tk.Entry(iframe, textvariable = nFax2, font=font1)
entry18_1 = tk.Entry(iframe, textvariable = nMail1, font=font1)
entry19_1 = tk.Entry(iframe, textvariable = nUrl1, font=font1)
entry19_2 = tk.Entry(iframe, textvariable = nUrl2, font=font1)

label00_1.grid(row=0, column=1)
label00_2.grid(row=0, column=2)
label01_0.grid(row=1, column=0)
label02_0.grid(row=2, column=0)
label03_0.grid(row=3, column=0)
label04_0.grid(row=4, column=0)
label05_0.grid(row=5, column=0)
label06_0.grid(row=6, column=0)
label07_0.grid(row=7, column=0)
label08_0.grid(row=8, column=0)
label09_0.grid(row=9, column=0)
label10_0.grid(row=10, column=0)
label11_0.grid(row=11, column=0)
label12_0.grid(row=12, column=0)
label13_0.grid(row=13, column=0)
label14_0.grid(row=14, column=0)
label15_0.grid(row=15, column=0)
label16_0.grid(row=16, column=0)
label17_0.grid(row=17, column=0)
label18_0.grid(row=18, column=0)
label19_0.grid(row=19, column=0)

entry01_1.grid(row=1, column=1)
entry01_2.grid(row=1, column=2)
entry02_1.grid(row=2, column=1)
entry02_2.grid(row=2, column=2)
entry03_1.grid(row=3, column=1)
entry04_1.grid(row=4, column=1)
entry04_2.grid(row=4, column=2)
entry05_1.grid(row=5, column=1)
entry06_2.grid(row=6, column=2)
entry07_1.grid(row=7, column=1)
entry07_2.grid(row=7, column=2)
entry08_2.grid(row=8, column=2)
entry09_1.grid(row=9, column=1)
entry09_2.grid(row=9, column=2)
entry10_1.grid(row=10, column=1)
entry10_2.grid(row=10, column=2)
entry11_1.grid(row=11, column=1)
entry11_2.grid(row=11, column=2)
entry12_1.grid(row=12, column=1)
entry12_2.grid(row=12, column=2)
entry13_1.grid(row=13, column=1)
entry14_2.grid(row=14, column=2)
entry15_1.grid(row=15, column=1)
entry15_2.grid(row=15, column=2)
entry16_1.grid(row=16, column=1)
entry16_2.grid(row=16, column=2)
entry17_1.grid(row=17, column=1)
entry17_2.grid(row=17, column=2)
entry18_1.grid(row=18, column=1)
entry19_1.grid(row=19, column=1)
entry19_2.grid(row=19, column=2)

Japanese()

# QR code Flame
qframe = tk.LabelFrame(root, text = u'QR Code', background = 'lightgrey', width = 600, height = 550, borderwidth = 3)
qframe.pack(side = tk.LEFT, fill = tk.BOTH, padx = pad, expand=True)
canvas = tk.Canvas(qframe, background = 'lightgrey', width=600, height=500)
canvas.pack(fill = tk.BOTH, padx = pad, expand=True)

root.mainloop()


# In[ ]:




