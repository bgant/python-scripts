#!/usr/bin/python3
#
# Brandon Gant
# 2019-12-05
#
# sudo apt-get install python3-bs4
#
# This script downloads and parses Ameren Power Smart Pricing hourly data.
#
# The power_state() function will be used to determine whether a power outlet
# should be enabled or not depending on the price of electricity.
#
# Table Data:
#    * Time of Day (CT), Actual Price (Cents per kWh)
#    * Data is 24 hours starting at 11PM
#    * Tomorrow's prices are available after 4:30PM CT
#
# Source: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Source: https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

import datetime
current_hour = datetime.datetime.now().hour
#current_hour = 23  # For Testing after 4:30PM CT
if not current_hour == 23:
   # Use Today's date 
   date = datetime.datetime.now().strftime('%Y%m%d')
else:
   # During the 11PM hour use Tomorrow's date
   date = datetime.datetime.now() + datetime.timedelta(days=1)
   date = date.strftime('%Y%m%d')


def main():
    number_of_hours = int(input('Enter Number of Hours: '))
    print('%s cheapest hours today are %s' % (number_of_hours, cheapest_hours(date, number_of_hours)))
    print('Should power be on now?', power_state(number_of_hours))


def cheapest_hours(date, number_of_hours):
    url = 'http://www.powersmartpricing.org/psp/servlet?type=pricingtabledatesingle&date=' + date
    html_file = 'psp_' + date + '.html'

    # Download html table if not already downloaded
    import os.path
    if not os.path.isfile(html_file):
        import requests
        r = requests.get(url)
        open(html_file, 'wb').write(r.content)

    with open(html_file, 'r') as fp:
        psp_html = fp.read()

    # Removing some text before parsing
    psp_html = psp_html.replace('&cent;', '')
    psp_html = psp_html.replace('<small>', '')
    psp_html = psp_html.replace('</small>', '')
    psp_html = psp_html.replace('<div class=\'pricingBox green\'></div>', '')
    #print(psp_html)

    data = []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(psp_html, 'lxml')
    table_body = soup.find('tbody')

    rows = table_body.find_all('tr')
    for index, row in enumerate(rows):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        #print('columns:', index, cols)
    
        # Convert to table data to hour numbers
        if index == 0:
            hour_cols = [23, cols[1]]
        else:
            hour_cols = [index - 1, cols[1]]
        #print('hours:', hour_cols)
        data.append([ele for ele in hour_cols])

    # Sort List by second pricing element
    data.sort(key = lambda x: x[1])

    # Pull only the cheapest hours out of the data
    hours = [hour for hour, price in data[0:number_of_hours]]
    return hours


def power_state(number_of_hours):
    hours_list = cheapest_hours(date, number_of_hours)
 
    #print('Current Hour:', current_hour)
    #print('Hours List:', hours_list)
    
    if current_hour in hours_list:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

