# baseball

import chart


def getdata(filename):
    """return header and data from the file"""
    everything =  [
        line.strip().split(',')
        for line in file(filename)]
    header = everything[0]
    stats = everything[1:]
    return (header,data)

def getstat(data, name):
    """return a list of the stat from the data"""
    header, stats = data 
    position = header.index(name)

    return [line[position]for line in stats]

def getchart(data, name):
    """return a piechart url for statistic labeled with years"""
    amounts = getstat(data, name)
    labels = getstat(data, year)
    return chart.chart_activities(amounts, labels)
        
def getlinechart(data, name, lo, hi):
    """return a line chart of the statistic"""
    amounts = getstat(data, name)
    return chart.linechart(','.join(amounts), lo, hi)

