# For making HTTP requests
import requests

# For parsing the data
from bs4 import BeautifulSoup

# For creating Data Frames
import pandas as pd

#=====================Standard Scraper Setup======================
#=================================================================

# Standard way to set the URL being scraped
URL = "https://wiki.warframe.com/w/Warframes_Comparison#Acquisition_"

# Standard way to store the HTML of the request as variable "page"
page = requests.get(URL)

# Standard way to parse HTML and store as a variable "soup"
soup = BeautifulSoup(page.content, "html.parser")

#=====================Column Headers==============================

table_data = soup.find('table', class_='article-table sortable')

# Filter down to just the headers "Warframe, Location, etc."
column_headers = table_data.find('tr').text.strip() 
#
# Format the result into list of strings
# Filter out tags and spacing for clean result
aquisition_header = column_headers.split()

# Result should be the below list 
# ['Warframe', 'Location', 'Mission', 'Boss', 'Other', 'Platinum', 'Credits']


# Puts the list in an empty Data Framemagick input.heic -quality 92 output.jpg
df = pd.DataFrame(columns = aquisition_header)

#==========================Rows/Warframe names====================


# Filter down to the table containing data needed
table_data = soup.find("table", class_="article-table sortable")

# Section containing Warframe names
row_data = soup.find("table")

# Filter down to Warframe name data
wf_name_data = row_data.find_all('a')

for wf in wf_name_data:
    total_wf_data = row_data.find_all('a')
    warframe_name_data = [warframe.text.strip() for warframe in total_wf_data]
warframe_names = warframe_name_data[6:]
#print(warframe_names)  <--- List of all Warframes

#=================================================================

'''
#=================================================================
#=================================================================
    At this point I have the categories/columns ("Warframe, Location, Mission, Boss, Other, Platinum, Credits") and the Warfame names to be used as rows

    I need to get the data and add everything to the data framelike the command I ran for the column headers
#=================================================================
#=================================================================
'''


'''
I'm pretty sure I need to run this loop at least two or three times due to the setup of the table on the webpage. Once for the headers, then for the Warframe names, then for the data. Trying several ways before moving forward. Keeping what I know works until ready to slim down what isn't needed. 
'''


# Data from each column, except the Warframe
column_data = table.find_all('tr')

'''
 This is should be all of the Warfame info I will be using

for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)


 This is all of the Warfame info I will be using

for column in column_data:
     total_data = column.find_all('td')
     warframe_data = [data.text.strip() for data in total_data]
     print(warframe_data)


'''
# print(df)
