
sampNumb='Total: 2,11,6 viruses'

def getSampNumb(sampNumb):
    part1=sampNumb.replace('Total: ', '')
    part2=part1.replace(' viruses', '')
    part3=part2.replace(',', '')
    return(part3)

if int(getSampNumb(sampNumb))>0:
    print('download')
    print(getSampNumb(sampNumb))
else:
    print('next')