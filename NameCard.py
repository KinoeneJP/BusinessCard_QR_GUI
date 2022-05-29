#!/usr/bin/env python
# coding: utf-8

# In[28]:


# coding:utf_8
# Save This as 'NameCard.py' and import as 'from NameCard import *'

from PIL import Image
import pickle

class NameCard:
    def __init__(self):
        self.isE = False
        self.isJ = True
        self.isPhonetixJ = False #Furigana
        # 以下、[0]=Japanese, [1]=English
        self.nPrefix = ['',''] #Dr. Mr. Ms. PhD Sur 工学博士など
        self.nFormat = ['',''] #表示される状態の名前 (Mundatory)
        self.nFamily = ['',''] #Family Name (Mundatory)
        self.nFamPho = ['',''] #Family Name Furigana
        self.nFirst  = ['',''] #First Name (Mundatory)
        self.nFirPho = ['',''] #First Name Furigana
        self.nMiddle = ['',''] #Middle Name
        self.nNick   = ['',''] #Nick Name
        self.nSuffix = ['',''] #Jr. Sr. IIなど(日本語では使わないはず)
        self.cName   = ['',''] #Company Name (Mundatory)
        self.cOrg    = ['',''] #Organization Name (Dept., Division...)
        self.cTitle  = ['',''] #Title
        self.cCntry  = ['',''] #Country of Company (Mundatory in English)
        self.cZip    = ['',''] #Zip Number (Eng == Jap **TEXT**) (Mundatory)
        self.cAdd    = ['',''] #Company Address (Mundatory)
        self.aPhone  = ['',''] #Company Phone (**TEXT**)
        self.aMobile = ['',''] #Mobile Phone (**TEXT**) (Mundatory)
        self.aFax    = ['',''] #Fax Number (**TEXT**)
        self.aEmail  = ['',''] #E-Mail Address (**TEXT**) (Mundatory)
        self.aUrl    = ['',''] #Company Web URL
        self.vcf     = ['',''] #vCard Format Text
        self.qr      = Image.new(mode = '1', size = (1024, 1024)) #QRCode image
    def genVCFJ(self):
        if self.isE == True:
            raise 'You selected Japanese though English Flag set'
        elif self.isJ == False:
            raise 'You selected Japanese though Japanese Flag unset'
        else:
            phonetix = f'X-PHONETIC-FIRST-NAME:{self.nFirPho[0]}\r\nX-PHONETIC-LAST-NAME:{self.nFamPho[0]}\r\n' if self.isPhonetixJ == True else ''
            nick   = '' if self.nNick[0]   == '' else f'NICKNAME:{self.nNick[0]}\r\n'
            tel    = '' if self.aPhone[0]  == '' else f'TEL;WORK;VOICE:{self.aPhone[0]}\r\n'
            mobile = '' if self.aMobile[0] == '' else f'TEL;WORK;CELL:{self.aMobile[0]}\r\n'
            fax    = '' if self.aFax[0]    == '' else f'TEL;WORK;FAX:{self.aFax[0]}\r\n'
            url    = '' if self.aUrl[0]    == '' else f'URL:{self.aUrl[0]}\r\n'
            self.vcf = (f'BEGIN:VCARD\r\nVERSION:3.0\r\nN:{self.nFamily[0]}; {self.nFirst[0]};;{self.nPrefix[0]}\r\nFN:{self.nFormat[0]}\r\n{phonetix}{nick}ORG:{self.cOrg[0]},{self.cName[0]}\r\nTITLE:{self.cTitle[0]}\r\n{tel}{mobile}{fax}ADR;WORK:;;{self.cAdd[0]},{self.cZip[0]}\r\nEMAIL;PREF;INTERNET:{self.aEmail[0]}\r\n{url}END:VCARD')

    def genVCFE(self):
        if self.isJ == True:
            raise 'You selected English though Japanese Flag set'
        elif self.isE == False:
            raise 'You selected English though ENglish Flag unset'
        else:
            nick   = '' if self.nNick[1]   == '' else f'NICKNAME:{self.nNick[1]}\r\n'
            tel    = '' if self.aPhone[1]  == '' else f'TEL;WORK;VOICE:{self.aPhone[1]}\r\n'
            mobile = '' if self.aMobile[1] == '' else f'TEL;WORK;CELL:{self.aMobile[1]}\r\n'
            fax    = '' if self.aFax[1]    == '' else f'TEL;WORK;FAX:{self.aFax[1]}\r\n'
            url    = '' if self.aUrl[1]    == '' else f'URL:{self.aUrl[1]}\r\n'
            self.vcf = (f'BEGIN:VCARD\r\nVERSION:3.0\r\nN:{self.nFamily[1]}; {self.nFirst[1]}; {self.nMiddle[1]}; {self.nPrefix[1]}; {self.nSuffix[1]}\r\n{nick}FN:{self.nFormat[1]}\r\nORG:{self.cOrg[1]},{self.cName[1]}\r\nTITLE:{self.cTitle[1]}\r\n{tel}{mobile}{fax}ADR;WORK:;;{self.cAdd[1]}, {self.cZip[1]},{self.cCntry[1]}\r\nEMAIL;PREF;INTERNET:{self.aEmail[1]}\r\n{url}END:VCARD')
#            self.vcf = (f'BEGIN:VCARD\r\nVERSION:3.0\r\nN:{self.nFirst[1]}; {self.nMiddle[1]}; {self.nFamily[1]}; {self.nPrefix[1]}; {self.nSuffix[1]}\r\n{nick}FN:{self.nFormat[1]}\r\nORG:{self.cOrg[1]},{self.cName[1]}\r\nTITLE:{self.cTitle[1]}\r\n{tel}{mobile}{fax}ADR;WORK:;;{self.cAdd[1]}, {self.cZip[1]},{self.cCntry[1]}\r\nEMAIL;PREF;INTERNET:{self.aEmail[1]}\r\n{url}END:VCARD')
    def setEng(self):
        self.isE = True
        self.isJ = False
    def setJap(self):
        self.isE = False
        self.isJ = True
    def saveVCF(self, fname):
        with open(fname, mode='wb') as f:
            pickle.dump(self.vcf, f)
    def loadVCF(self, fname):
        with open(fname, mode='rb') as f:
            return(pickle.load(f))
    def initVCF(self):
        self.vcf = ['','']
    def initCard(self):
        self.__init__()
    def saveCard(self, fname):
        with open(fname, mode='wb') as f:
            pickle.dump(self, f)
    def loadCard(self, fname):
        with open(fname, mode='rb') as f:
            return(pickle.load(f))


pref = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',        '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',        '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県',        '岐阜県', '静岡県', '愛知県', '三重県',        '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県',        '鳥取県', '島根県', '岡山県', '広島県', '山口県',        '徳島県', '香川県', '愛媛県', '高知県',        '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']

pref_jiscode = {1: '北海道', 2: '青森県', 3: '岩手県', 4: '宮城県', 5: '秋田県', 6: '山形県', 7: '福島県',
    8: '茨城県', 9: '栃木県', 10: '群馬県', 11: '埼玉県', 12: '千葉県', 13: '東京都', 14: '神奈川県',
    15: '新潟県', 16: '富山県', 17: '石川県', 18: '福井県', 19: '山梨県', 20: '長野県',
    21: '岐阜県', 22: '静岡県', 23: '愛知県', 24: '三重県',
    25: '滋賀県', 26: '京都府', 27: '大阪府', 28: '兵庫県', 29: '奈良県', 30: '和歌山県',
    31: '鳥取県', 32: '島根県', 33: '岡山県', 34: '広島県', 35: '山口県',
    36: '徳島県', 37: '香川県', 38: '愛媛県', 39: '高知県',
    40: '福岡県', 41: '佐賀県', 42: '長崎県', 43: '熊本県', 44: '大分県', 45: '宮崎県', 46: '鹿児島県', 47: '沖縄県'}

#import vcfpy #https://vcfpy.readthedocs.io/en/stable/index.html
if __name__ == '__main__':
    import qrcode
    myCard = NameCard()
    myCard.nPrefix = ['工学博士','Mr.']
    myCard.nFormat = ['水澤 和哉', 'Kazuya Mizusawa']
    myCard.nFamily = ['水澤', 'Mizusawa']
    myCard.nFirst  = ['和哉', 'Kazuya']
    myCard.nFamPho = ['みずさわ','']
    myCard.nFirPho = ['かずや','']
    myCard.nNick   = ['', 'Keith']
    myCard.isPhonetixJ = False
    myCard.cName   = ['トヨタ自動車株式会社', 'TOYOTA MOTOR CORPORATION']
    myCard.cOrg    = ['レクサス電子システム設計部　コックピットシステム設計室','Cockpit Design Department, Lexus Electronics System Design Divisiom']
    myCard.cTitle  = ['主幹','Project Manager']
    myCard.cZip    = ['471-8572', '471-8572']
    myCard.cAdd    = ['愛知県豊田市トヨタ町1番地', '1, Toyota-cho, Toyota, Aichi']
    myCard.cCntry  = ['', 'Japan']
    myCard.aMobile = ['050-3165-7279','+81-50-3165-7279']
    myCard.aEmail  = ['kazuya_mizusawa@mail.toyota.co.jp','kazuya_mizusawa@mail.toyota.co.jp']
    myCard.aUrl    = ['https://lexus.jp', 'https://lexus.com']
    myCard.aFax    = ['0565-94-1040','']
#    myCard.setEng()
    if myCard.isE == False and myCard.isJ == True:
        myCard.vcf = myCard.genVCFJ()
    if myCard.isE == True and myCard.isJ == False:
        myCard.vcf = myCard.genVCFE()        
    myCard.qr = qrcode.make(myCard.vcf)
#    myCard.qr.show()
#    print(myCard.vcf)
#    print(myCard.qr.format, myCard.qr.size, myCard.qr.mode)
    
# 三項演算子: (変数) = (条件がTrueのときの値) if (条件) else (条件がFalseのときの値
# https://gist.github.com/gerwin3/ef9ae04d2b156c405db45dc70b93f716

