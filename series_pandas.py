import pandas as pd
##series
data=[1, 2, 3, 4, 5]
series=pd.Series(data)
print(series)
datat=[1.1, 2.2, 3.3, 4.4, 5.5]
serie=pd.Series(datat)
print(serie)
datat1=["a", 2.2, 3.3, 4.4, 5.5]
serial=pd.Series(datat1)
print(serial)
datat2=[True, False, True, False, True]
serian=pd.Series(datat2)
print(serian)
##
data3=[1, 2, 3, 4, 5]
seris=pd.Series(data3,index=["apartment1","apartment2","apartment3","apartment4","apartment5"])
print(seris)

##
seris.loc["apartment1"]=10
print(seris)
print(seris.iloc[2])

##
print(seris[seris>3])

##dictionaries comes under series 
calories={"day1":1750,"day2":2000,"day3":1800}
series=pd.Series(calories)
print(series)
series.loc["day1"]+=500
print(series)
print(series[series>2000])

###DataFramesgit status

