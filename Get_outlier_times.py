# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 14:44:51 2017

@author: User
"""

from collections import namedtuple
Application = namedtuple('Application', 'name run_times')

apps = [
        Application("Collator", [12, 20, 8]), 
        Application("Messager", [96, 101, 200, 106, 87]), 
        Application("Profiler", [30, 32, 31]), 
        Application("Writer", [2, 3, 10]), 
        Application("Reconciliator", [3, 3, 3, 4, 3])
        ]

def get_outlier_times(app):
    total = sum(app.run_times)
    average = total / len(app.run_times)
    return {
            app.name :
            time for time in app.run_times
            if (time) > average * 1.5
    }


"""
What methods below will return a dictionary whose keys are
application names and values are runtimes which are above the
average run time? Application that have not exceeded 50% abvoe the average
run time should not be included in the dictionary
"""    
    
    
print [get_outlier_times(app) for app in apps]
print { res for app in apps for res in get_outlier_times(app)}
print {k:res for app in apps for k, res in get_outlier_times(app).items()}
print dict((k, res) for app in apps for k, res in get_outlier_times(app).items() if res)
print list(get_outlier_times(app) for app in apps)