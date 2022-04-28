import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
params = {
    'q': 'python developer',
    'l': 'Jakarta',
    'vjk': '283a5a754ee6b05e'
}
"""
# soup = BeautifulSoup(res.text, 'html.parser')
# res = requests.get(url, params=params, headers=headers)


url = 'https://id.indeed.com/jobs?'
site = 'https://id.indeed.com'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}


def get_total_pages(query, location):
    params = {
        'q': query,
        'l': location,
        'vjk': '283a5a754ee6b05e'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    # Scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul', 'pagination-list')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    # print(total)
    return total

def get_all_items(query, location, start, page):
    params = {
        'q': query,
        'l': location,
        'start': start,
        'vjk': '283a5a754ee6b05e'
    }

    res = requests.get(url, params=params, headers=headers)

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')

    # scraping process
    contents = soup.findAll('table', 'jobCard_mainContent big6_visualChanges')

    # pick item
    # * title
    # * company name
    # * company Link
    # * company address
    jobs_list = []
    for item in contents:
        title = item.find('h2', 'jobTitle').text
        company = item.find('span', 'companyName')
        company_name = company.text


        # Sorting Data
        data_dict = {
            'title': title,
            'company_name': company_name
        }

        jobs_list.append(data_dict)


    # cetak data di sini
    # print(jobs_list)
    # print('Jumlah Data yang telah di scraping:', len(jobs_list))
    # print(f'Jumlah data: {len(jobs_list)}')

    # Writing json file
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open(f'json_result/{query}_in_{location}_page_{page}.json', 'w+') as json_data:
        json.dump(jobs_list, json_data)

    print('json created')
    return jobs_list

    """
    # digantikan dengan fungsi baru di video chapter 11
    # Create CSV
    df = pd.DataFrame(jobs_list)
    df.to_csv('indeed_data.csv', index=False)
    df.to_excel('indeed_data.xlsx', index=False)

    # Data has created to 2 format : XML & XLSX
    print("Data input has been formatting to xml & xlsx")
    """

def create_document(dataframe, filename):
    try:
        os.mkdir('data_result')
    except FileExistsError:
        pass

    df = pd.DataFrame(dataframe)
    df.to_csv(f'data_result/{filename}.csv', index=False)
    # di tutor ada typo
    df.to_excel(f'data_result/{filename}.xlsx', index=False)

    print(f'File {filename}.csv and {filename}.xlsx successfully created')


def run():
    query = input('Enter Your Query: ')
    location = input('Enter Your Location: ')

    total = get_total_pages(query,location)
    counter = 0
    final_result = [] # kirain 0 taunya list kosong

    for page in range(total):
        page += 1
        counter += 10
        final_result += get_all_items(query, location, counter, page)

    # formatting data
    try:
        os.mkdir('reports')
    except FileExistsError:
        pass

    with open('reports/{}.json'.format(query), 'w+') as final_data: # kurang focus 'w+'
        json.dump(final_result, final_data)

    print('Data JSON has created')

    # create document
    create_document(final_result, query)

if __name__ == '__main__':
    run()