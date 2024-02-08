import pandas as pd

def startdatas():
    files=['LiftE1.csv','LiftE2.csv','LiftE3.csv']
    columns=["Width","Door time","1.0","1.6","2.0","2.5","3.0","3.5"]
    dfE1=pd.read_csv(files[0],header=None,sep=";",names=columns)
    dfE2=pd.read_csv(files[1],header=None,sep=";",names=columns)
    dfE3=pd.read_csv(files[2],header=None,sep=";",names=columns)
    return dfE1, dfE2,dfE3

