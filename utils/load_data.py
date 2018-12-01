import os
from pathlib import Path
import pandas as pd

STATES_LINK = "https://simple.wikipedia.org/wiki/List_of_U.S._states"


def load_states_from_web():
    fiddy_states = pd.read_html(STATES_LINK)
    states = list(fiddy_states[0][1][1:])
    hpi_names = ['FMAC/HPI_' + abbv for abbv in states]
    return hpi_names


def load_state_names(file_name='states.txt'):
    file_path = '../' + file_name

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        file = open(file_path, 'r')
        content = file.read().splitlines()
        return list(content)
    else:
        hpi_names = load_states_from_web()
        states_file = open(file_path, 'w')
        states_file.writelines(str(hpi_name + '\n') 
                                for hpi_name in hpi_names)
        states_file.close()
        return hpi_names


res = load_state_names()
print(res)
