# For making HTTP requests
import requests

# For parsing the data
from bs4 import BeautifulSoup

# For creating Data Frames
import pandas as pd

#=============== Standard Scraper - Fetch the page ===============
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

'''
=================================================================
=================================================================
    At this point I have the categories/columns 
    ("Warframe, Location, Mission, Boss, Other, Platinum, Credits") 
    and the Warfame names to be used as rows

    I need to get the data and add everything to the data 
    framelike the command I ran for the column headers
=================================================================
=================================================================
'''
# Add Warfame names to the Warframe column of the DataFrame with Primes filtered out(might handle Primes separately)

filtered_names = []

for name in warframe_names:
    if 'Prime' not in name:
        filtered_names.append(name)
    elif name == 'Excalibur Prime':
        filtered_names.append(name)

# Select table rows (only those with <td> cells)
table = soup.find('table', class_='article-table sortable')
table_rows = [row for row in table.find_all('tr') if row.find('td')]

# Populate DataFrame
for idx, table_item in enumerate(table_rows):
    wf_deets = table_item.find_all('td')
    warframe_table_data = [info.text.strip() for info in wf_deets]
    
    if len(warframe_table_data) == 6:
        df.loc[len(df)] = [filtered_names[idx]] + warframe_table_data




'''
================================================================
 Here is where we start taking input and returning data
 about each Warframe in a numbered fashion. 
 Keeping it simple for now
================================================================
'''

# Show user a basic numbered list of all Warframes 
for num, wf_name in enumerate(filtered_names):
    print(f"{num + 1}. {wf_name}")

user_choice = int(input("Pick a number: "))

chosen_warframe = filtered_names[user_choice - 1]

print(f"You chose: {chosen_warframe}")


# Show user a basic numbered list of categories to choose from
for num, category in enumerate(aquisition_header):
    print(f"{num + 1}. {aquisition_header}")


user_second_choice = int(input("Pick a number: "))

chosen_warframe_category = [user_second_choice - 1]


print(f"You chose: {chosen_warframe_category}")

# Preview
#print(df.head(10))
#print(f"\nTotal rows: {len(df)}")

# Save a csv copy
#df.to_csv(r'~/Documents/Warframe_Info.csv')

