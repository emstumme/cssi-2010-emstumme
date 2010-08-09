# make charts

import webbrowser

chart_url = "http://chart.apis.google.com/chart?"

def piechart(data, labels):
    url = chart_url + "cht=p3&chd=t:" + data +"&chs=250x100&chl=" +labels
    return url


time = (40, "python"), (30, "food"), (20, "sleep"), (10, "scrabble")

percents = ["40", "30", "20", "10"]
activities = ["python", "food", "sleep", "scrabble"]

def chart_activities(percents, activities):
    # do some stuff
    data = ",".join(percents)
    labels = "|".join(activities)
    return piechart(data, labels) 
    
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

sample = {
    'justin ' :5,
    'ladygaga ' :7,
    'guido' :2
    }

def dictionary_chart(d):
    labels = d.keys()
    data = [str (x)for x in d.values()]
    return chart_activities(data, labels)


def piechart(data, labels):
    url = chart_url + "cht=p3&chd=t:" + data +"&chs=250x100&chl=" +labels
    return url

