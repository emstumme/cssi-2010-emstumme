# time.py
#
# class to manipulate times

class Time():
    """represents a time of day in hours, minutes and seconds"""

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        """initalize a new time object"""
        self.init(hours, minutes, seconds) 


    def __str__(self):
        """return time as a string"""
        return ("<time: " +
                str(self.hours) + ":" +
                str(self.minutes) + ":" +
                str(self.seconds) + ">")

    def init(time, hours, minutes, seconds):
        time.hours = hours
        time.minutes = minutes
        time.seconds = seconds
        

def init_time(time, hours, minutes, seconds):
    """initialize time with hours, minutes, and seconds"""
    time.hours = hours
    time.minutes = minutes
    time.seconds = seconds



t1 = Time()
init_time(t, 9, 34, 12)
t2 = Time()
Time.init(t2, 8, 43, 15)
t3 = Time()
t3.init(7, 34, 23)
t4 = Time(6, 56, 34)

# t3.init(7, 34, 23)
#
# object.name(...) <= ah this is a function call, let me look up the class
# object is of type class
# Class.name <= this is the actual function
# Class.name(object, ...)
#
# Time.init(t3, ...)


