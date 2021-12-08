import os
import csv

CSV_FILE = os.path.join('/', 'Users/shivareddy/Downloads/Basic_LinkedInDataExport_12-04-2021', 'Connections.csv')

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]
workingAtGoogle = 0

for contact in contacts:
    for t in contact['Company'].split('/'):
        if (t == 'Google'):
            workingAtGoogle = workingAtGoogle + 1
print('There are %d people who are working at Google.' % (workingAtGoogle))

whoareceos = 0

for contact in contacts:
    for t in contact['Position'].split('/'):
        if (t == 'CEO'):
            whoareceos = whoareceos + 1

print('There are %d people who are CEOs.' % (whoareceos))

import pandas as pd

df = pd.read_csv(CSV_FILE)
print(df.head())

# import plotly.express as px
# fig = px.treemap(df, path=['Position', Company'], width=1200, height=1200)
#
# fig.show()
