import pandas as pd

def stats_columns(filename, xlabel, ylabel):
    dF= pd.read_csv(filename)
    
    xdata=dF[xlabel]
    ydata=dF[ylabel]
    
    xstats=xdata.describe()
    ystats=ydata.describe()
    
    return xstats, ystats
if __name__=='__main__':
    print(stats_columns('tempMainYearly.csv', 'temp', 'main'))