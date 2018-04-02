import pandas as pd
from collections import OrderedDict
from datetime import date
from bs4 import BeautifulSoup
import numpy as np
import requests

# Function to get a list of dics from an HTML table

def HTMLtableToDic(tableSoup):
    trArray = tableSoup.find_all('tr')

    headers = trArray[0].find_all('th')
    labels = []
    for i in range (0, len(headers)):
        labels.append(headers[i].string)

    # Loop on rows
    tableContent = []
    for i in range(1, len(trArray)):
        row = {}
        tdList = trArray[i].find_all('td')

        #Loop on entries
        for j in range(0, len(tdList)):
            row[labels[j]] = tdList[j].string

        tableContent.append(row)

    return tableContent
