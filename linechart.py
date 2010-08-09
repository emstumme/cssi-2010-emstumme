

def linechart(data lo = 0, high = 100):
    url = (chart_url +
           "cht=lc&chd=y:" +
           data +
           "&chds=" + str(lo) + "," + str(hi) +
           "&chs=250x100")
    return url
