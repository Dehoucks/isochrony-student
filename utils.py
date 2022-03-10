import datetime
import pandas as pd

def step_timer(n_click, list_press, list_time):

    list_press.append(str(n_click))
    list_time.append(str(datetime.datetime.now()))
    return (list_press, list_time)
