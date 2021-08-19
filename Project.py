import pandas as pd
from matplotlib import pyplot as plt


class TravellersTrend:

    def __init__(self):
        self.xlsx = pd.ExcelFile('Project_File.xlsx')

        self.dataFrame= pd.read_excel (r'Project_File.xlsx')

      #replace "na" with "0"
        self.dataFrame = self.dataFrame.replace(["na"],["0"])

   # Get all Europe Countries
        self.dataFrame = self.xlsx.parse (0, usecols=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], names=["United Kingdom", "Germany", "France", "Italy", "Netherlands", "Greece",
        "Belgium & Luxembourg", "Switzerland", "Austria", "Scandinavia", "CIS & Eastern Europe"])


    def UKVisitorTrends(self):
          self.UK = self.dataFrame.loc[360:480, "United Kingdom"]
          print(self.UK)


    def GERMVisitorTrends(self):
        self.GERM = self.dataFrame.loc[360:480, "Germany"]
        print(self.GERM)


    def FRANCVisitorTrends(self):
        self.FRANC = self.dataFrame.loc[360:480, "France"]
        print(self.FRANC)


    def ITALYVisitorTrends(self):
        self.ITALY = self.dataFrame.loc[360:480, "Italy"]
        print(self.ITALY)


    def NETHERVisitorTrends(self):
        self.NETHER = self.dataFrame.loc[360:480, "Netherlands"]
        print(self.NETHER)


    def GREEVisitorTrends(self):
        self.GREE = self.dataFrame.loc[360:480, "Greece"]
        print(self.GREE)


    def BELGVisitorTrends(self):
        self.BELG = self.dataFrame.loc[360:480, "Belgium & Luxembourg"]
        print(self.BELG)


    def SWITZVisitorTrends(self):
        self.SWITZ = self.dataFrame.loc[360:480, "Switzerland"]
        print(self.SWITZ)


    def AUSTVisitorTrends(self):
        self.AUST = self.dataFrame.loc[360:480, "Austria"]
        print(self.AUST)


    def SCANDVisitorTrends(self):
        self.SCAND = self.dataFrame.loc[360:480, "Scandinavia"]
        print(self.SCAND)


    def CISVisitorTrends(self):
        self.CIS = self.dataFrame.loc[360:480, "CIS & Eastern Europe"]
        print(self.CIS)

    def TotalvisitorsUK(self):
        return self.UK.sum()


    def TotalvisitorsGermany(self):
        return self.GERM.sum()


    def TotalvisitorsFrance(self):
        return self.FRANC.sum()



    def TotalvisitorsItaly(self):
        return self.ITALY.sum()


    def TotalvisitorsNetherlands(self):
        return self.NETHER.sum()


    def TotalvisitorsGreece(self):
        return self.GREE.sum()



    def TotalvisitorsBelgium(self):
        return self.BELG.sum()


    def TotalvisitorsSwitzerland(self):
        return self.SWITZ.sum()



    def TotalvisitorsAustria(self):
        return self.AUST.sum()



    def TotalvisitorsScandinavia(self):
        return self.SCAND.sum()


    def TotalvisitorsCISeast(self):
        return self.CIS.sum()

        self.NameSums = [self.UK.sum(), self.GERM.sum(), self.FRANC.sum(), self.ITALY.sum() ,self.NETHER.sum(),
                         self.GREE.sum(), self.BELG.sum(), self.SWITZ.sum(), self.AUST.sum(), self.SCAND.sum(),
                         self.CIS.sum()]

        self.NameSums = self.NameSums.sort.values(ascending = False)

        self.TopFirst = self.NameSums.index[0]
        self.TopSecond = self.NameSums.index[1]
        self.TopThird = self.NameSums.index[2]
        print("The 3 countries that has the most visitors are", self.TopFirst,",", self.TopSecond,",", self.TopThird)


    def MedianvisitorsUK(self):
        return self.UK.median()

    def MedianvisitorsGermany(self):
        return self.GERM.median()

    def MedianvisitorsFrance(self):
        return self.FRANC.median()

    def MedianvisitorsItaly(self):
        return self.ITALY.median()

    def MedianvisitorsNetherlands(self):
        return self.NETHER.median()

    def MedianvisitorsGreece(self):
        return self.GREE.median()

    def MedianvisitorsBelgium(self):
        return self.BELG.median()

    def MedianvisitorsSwitzerland(self):
        return self.SWITZ.median()

    def MedianvisitorsAustria(self):
        return self.AUST.median()

    def MedianvisitorsScandinavia(self):
        return self.SCAND.median()

    def MedianvisitorsCISeast(self):
        return self.CIS.median()

        self.NameMedians = [self.UK.median(), self.GERM.median(), self.FRANC.median(), self.ITALY.median() ,self.NETHER.median(),
                         self.GREE.median(), self.BELG.median(), self.SWITZ.median(), self.AUST.median(), self.SCAND.median(),
                         self.CIS.median()]

        self.NameMedians = self.NameMedians.sort.values(ascending = False)

        self.TopFirstM = self.NameMedians.index[0]
        self.TopSecondM = self.NameMedians.index[1]
        self.TopThirdM = self.NameMedians.index[2]
        print("The 3 countries that has the most median visitors are", self.TopFirstM,",", self.TopSecondM,",", self.TopThirdM)



    def MeanvisitorsUK(self):
        return self.UK.mean()

    def MeanvisitorsGermany(self):
        return self.GERM.mean()

    def MeanvisitorsFrance(self):
        return self.FRANC.mean()

    def MeanvisitorsItaly(self):
        return self.ITALY.mean()

    def MeanvisitorsNetherlands(self):
        return self.NETHER.mean()

    def MeanvisitorsGreece(self):
        return self.GREE.mean()

    def MeanvisitorsBelgium(self):
        return self.BELG.mean()

    def MeanvisitorsSwitzerland(self):
        return self.SWITZ.mean()

    def MeanvisitorsAustria(self):
        return self.AUST.mean()

    def MeanvisitorsScandinavia(self):
        return self.SCAND.mean()

    def MeanvisitorsCISeast(self):
        return self.CIS.mean()

        self.NameMeans = [self.UK.mean(), self.GERM.mean(), self.FRANC.mean(), self.ITALY.mean(),
                        self.NETHER.mean(),
                        self.GREE.mean(), self.BELG.mean(), self.SWITZ.mean(), self.AUST.mean(),
                        self.SCAND.mean(),
                        self.CIS.mean()]

        self.NameMeans = self.NameMeans.sort.values(ascending=False)

        self.TopFirstMe = self.NameMeans.index[0]
        self.TopSecondMe = self.NameMeans.index[1]
        self.TopThirdMe = self.NameMeans.index[2]
        print("The 3 countries that has the most mean visitors are", self.TopFirstMe, ",", self.TopSecondMe, ",", self.TopThirdMe)















































tt = TravellersTrend()
tt.UKVisitorTrends()
tt.GERMVisitorTrends()
tt.FRANCVisitorTrends()
tt.ITALYVisitorTrends()
tt.NETHERVisitorTrends()
tt.GREEVisitorTrends()
tt.BELGVisitorTrends()
tt.SWITZVisitorTrends()
tt.AUSTVisitorTrends()
tt.SCANDVisitorTrends()
tt.CISVisitorTrends()
tt.TotalvisitorsUK()
tt.TotalvisitorsGermany()
tt.TotalvisitorsFrance()
tt.TotalvisitorsItaly()
tt.TotalvisitorsNetherlands()
tt.TotalvisitorsGreece()
tt.TotalvisitorsBelgium()
tt.TotalvisitorsSwitzerland()
tt.TotalvisitorsAustria()
tt.TotalvisitorsScandinavia()
tt.TotalvisitorsCISeast()
tt.MedianvisitorsUK()
tt.MedianvisitorsGermany()
tt.MedianvisitorsFrance()
tt.MedianvisitorsItaly()
tt.MedianvisitorsNetherlands()
tt.MedianvisitorsGreece()
tt.MedianvisitorsBelgium()
tt.MedianvisitorsSwitzerland()
tt.MedianvisitorsAustria()
tt.MedianvisitorsScandinavia()
tt.MedianvisitorsCISeast()
tt.MeanvisitorsUK()
tt.MeanvisitorsGermany()
tt.MeanvisitorsFrance()
tt.MeanvisitorsItaly()
tt.MeanvisitorsNetherlands()
tt.MeanvisitorsGreece()
tt.MeanvisitorsBelgium()
tt.MeanvisitorsSwitzerland()
tt.MeanvisitorsAustria()
tt.MeanvisitorsScandinavia()
tt.MeanvisitorsCISeast()






















