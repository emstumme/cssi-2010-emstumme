# make charts

import webbrowser

chart_url = "http://chart.apis.google.com/chart?"

def piechart(data, labels):
    url = chart_url + "cht=p3&chd=t:" + data +"&chs=250x100&chl=" +labels
    webbrowser.open(url)
    return url

print piechart("40,30,30", "python|food|sleep")
print piechart("60,40", "emily|stumme")
time = (40, "python"), (30, "food"), (20, "sleep"), (10, "scrabble")

percents = ["40", "30", "20", "10"]
activities = ["python", "food", "sleep", "scrabble"]

def chart_activities(percents, activities):
    # do some stuff
    data = ",".join(percents)
    labels = "|".join(activities)
    piechart(data, labels) 
    
chart_activities(percents,activities)

time = [(40, "python"),
        (30, "food"),
        (20, "sleep"),
        (10, "scrabble")]

def chart_time(time):
    data = []
    labels = []

    for p,c in time:
        data.append(p)
        labels.append(c)

    return chart_activities(p,c)
    
    return piechart(data, labels)
    return chart_activities(percents, activities)

def piechart(data, labels):
    url = chart_url + "cht=p3&chd=t:" + data +"&chs=250x100&chl=" +labels
    webbrowser.open(url)
    return url

def linechart(data lo = 0, high = 100):
    url = (chart_url +
           "cht=lc&chd=y:" +
           data +
           "&chds=" + str(lo) + "," + str(hi) +
           "&chs=250x100")
    return url
