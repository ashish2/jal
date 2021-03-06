import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import sys
import imp
from argparse import ArgumentParser

style.use('ggplot')

class Jal(object):

    datafile = "../../datasets/water_dishwash_bath2.csv"
    SOAP = "soap"
    OIL = "oil"
    OTHER = "otherParticles"
    AD = "afterDishwash"
    BB = "beforeBath"

    def __init__(self, datafile=datafile, *args, **kwargs):
        self.df = pd.read_csv(datafile)

    
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
        sad.name = str(xlab)
        sbb.name = ylab
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



def initJal(datafile):
    j = Jal(datafile=datafile)
    j.soap()
    j.oil()
    j.other()
    #j.soapcorr()


def main():
    if __name__ == "__main__":
        parser = ArgumentParser()
        parser.add_argument('-f', '--file', 
                type=str, 
                help="Path of data file",
                required=True)
        args = parser.parse_args()
        if args.file:
            path = args.file
            #ff = imp.load_source(f, path)

            initJal(path)

main()

