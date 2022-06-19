
sampNumb='Total: 2,11,6 viruses'

def getSampNumb(sampNumb):
    part1=sampNumb.replace('Total: ', '')
    part2=part1.replace(' viruses', '')
    part3=part2.replace(',', '')
    return(part3)

def checkSumpNumb():
    if int(getSampNumb(sampNumb))>0:
        print('download')
        print(getSampNumb(sampNumb))
    else:
        print('next')


import pandas as pd
date_rng = pd.date_range('2021-01-01','2021-01-03',freq='D')
dates=pd.Series(date_rng.format()).tolist()
print(dates)
