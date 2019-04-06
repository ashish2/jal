import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import sys

style.use('ggplot')

class Jal(object):

    datafile = "../../datasets/water_dishwash_bath2.csv"
    SOAP = "soap"
    OIL = "oil"
    OTHER = "otherParticles"
    AD = "afterDishwash"
    BB = "beforeBath"

    def __init__(self, *args, **kwargs):
        self.df = pd.read_csv(Jal.datafile)

    
    def soap(self):
        """
        Soap content in water after Dishwash and before Bath
        """
        # soap content after dishwash
        sad = self.df[self.df.content == Jal.SOAP][Jal.AD]
        # soap content before bath
        sbb = self.df[self.df.content == Jal.SOAP][Jal.BB]
        xlab = Jal.SOAP + " " + Jal.AD
        ylab = Jal.SOAP + " " + Jal.BB
        x = sad.plot(label=xlab)
        y = sbb.plot(label=ylab)
        xlabel = "Percentage of Soap content in water After Dishwash and Before Bath"
        plt.xlabel(xlabel)
        plt.show()

    def oil(self):
        """
        Oil content in water after Dishwash and before Bath
        """
        # Oil content after dishwash
        sad = self.df[self.df.content == Jal.OIL][Jal.AD]
        # oil content before bath
        sbb = self.df[self.df.content == Jal.OIL][Jal.BB]
        x = sad.plot(label= Jal.OIL + " " + Jal.AD )
        y = sbb.plot(label= Jal.OIL + " " + Jal.BB )
        xlabel = "Percentage of Oil Content in water After Dishwash and Before Bath"
        plt.xlabel(xlabel)
        plt.show()
   
    def other(self):
        """
        Other content in water after Dishwash and before Bath
        """
        # other content after dishwash
        sad = self.df[self.df.content == Jal.OTHER][Jal.AD]
        # other content before bath
        sbb = self.df[self.df.content == Jal.OTHER][Jal.BB]
        x = sad.plot(label= Jal.OTHER + " " + Jal.AD )
        y = sbb.plot(label= Jal.OTHER + " " + Jal.BB )
        xlabel = "Percentage of Other particles in water After Dishwash and Before Bath"
        plt.xlabel(xlabel)
        plt.show()

    def soapcorr(self):

        # soap content after dishwash
        sad = self.df[self.df.content == Jal.SOAP][Jal.AD]
        # soap content before bath
        sbb = self.df[self.df.content == Jal.SOAP][Jal.BB]
        print(sad.corr(sbb))

j = Jal()
j.soap()
#j.oil()
#j.other()
#j.soapcorr()

