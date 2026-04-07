# For making HTTP requests

import requests

# For parsing the data

from bs4 import BeautifulSoup

import pandas as pd

# The URL I've chosen to scrap
URL = "https://wiki.warframe.com/w/Warframes_Comparison#Acquisition_"

# Store the HTML of the request as variable "page"
page = requests.get(URL)

# Standard way to parse HTML and store as a variable "soup"
soup = BeautifulSoup(page.content, "html.parser")

# Filter down to the table containing data needed
table = soup.find("table", class_="article-table sortable")
# 
# Filter down more to strip the table's headers
aquisition_headers = table.find('tr').text.strip() 
#
# Format the result into strings
aquisition_titles = aquisition_headers.split()
# RESULT 
# ['Warframe', 'Location', 'Mission', 'Boss', 'Other', 'Platinum', 'Credits']


# Puts the list in an empty Data Frame
df = pd.DataFrame(columns = aquisition_titles)

column_data = table.find_all('tr')


for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)


print(df)



