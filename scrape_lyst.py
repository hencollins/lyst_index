import requests
from bs4 import BeautifulSoup
import pandas as pd


divs_h4_and_a = {'the-lyst-index/2018/q3/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2018', 'q3'],
               'the-lyst-index/2018/q4/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2018', 'q4'],
               'the-lyst-index/2019/q1/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2019', 'q1'],
               'data/the-lyst-index/q219/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2019', 'q2'],
               'data/the-lyst-index/q319/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2019', 'q3'],
               'data/the-lyst-index/q419/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2019', 'q4'],
               'data/the-lyst-index/q120/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2020', 'q1'],
               'data/the-lyst-index/q220/' : ['hottest-brand-item__position', 'hottest-brand-item__name', '2020', 'q2']}

div_h3_and_a = {'data/the-lyst-index/q320/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2020', 'q3'],
                        'data/the-lyst-index/q420/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2020', 'q4'],
                        'data/the-lyst-index/q221/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2021', 'q2'],
                        'data/the-lyst-index/q321/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2021', 'q3'],
                        'data/the-lyst-index/q421/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2021', 'q4'],
                        'data/the-lyst-index/q122/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2022', 'q1'],
                        'data/the-lyst-index/q222/' : ['hottest-brand-item__position', 'hottest-brand-item__name h4', '2022', 'q2'],
                        'data/the-lyst-index/q322/' : ['hottest-brand-item__position', 'hottest-brand-item__name h3', '2022', 'q3'],
                        'data/the-lyst-index/q422/' : ['hottest-brand-item__position', 'hottest-brand-item__name h3', '2022', 'q4'],
                        'data/the-lyst-index/q123/' : ['hottest-brand-item__position', 'hottest-brand-item__name h3', '2023', 'q1'],
                        'data/the-lyst-index/q223/' : ['hottest-brand-item__position', 'hottest-brand-item__name h3', '2023', 'q2'],
                        }

div_and_h3 = {'data/the-lyst-index/q121/' : ['hottest-brand-item__position', 'hottest-brand-item__container', 'hottest-brand-item__name h4', '2021', 'q1'],
               'data/the-lyst-index/q323/' : ['hottest-brand-item__position', 'hottest-brand-item__container', 'hottest-brand-item__name h3', '2023', 'q3'],
               'data/the-lyst-index/q423/' : ['hottest-brand-item__position', 'hottest-brand-item__container', 'hottest-brand-item__name h3', '2023', 'q4'],}

div_and_more_div = {'data/the-lyst-index/q124/' : ['mono-type blue', 'mono-type padding-left', '2024', 'q1'],
                    'the-lyst-index/2024/q2/' : ['mono-type blue', 'mono-type padding-left', '2024', 'q2'],
                    'the-lyst-index/2024/q3/' : ['mono-type blue', 'mono-type padding-left', '2024', 'q3'],
                    'the-lyst-index/2024/q4/' : ['mono-type blue', 'mono-type padding-left', '2024', 'q4']}

##SCRAPING DIV_AND_MORE_DIV LYSTS##

for list_name in div_and_more_div:

    # URL of the Lyst Hottest Brands Index page for the given Q
    url = 'https://www.lyst.com/' + list_name

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        #Create data collectors
        data = {'Rank': [], 'Brand': []}

        # Find the elements containing the brand names and rankings
        rankings = soup.find_all('div', class_=div_and_more_div[list_name][0])
        brands = soup.find_all('div', class_=div_and_more_div[list_name][1])

        # Ensure that both lists have the same length
        if len(rankings) == len(brands):
            for i in range(len(rankings)):
                rank = rankings[i].text.strip()
                name = brands[i].text.strip()
                data['Rank'].append(rank)
                data['Brand'].append(name)
        else:
            print('Mismatch in the number of rankings and brands')

        # Create the dataframe
        df = pd.DataFrame(data)

        #Add year and quarter columns
        year = div_and_more_div[list_name][2]
        quarter = div_and_more_div[list_name][3]

        df['Year'] = year
        df['Quarter'] = quarter

        #Convert all brand names to lowercase
        df['Brand'] = df['Brand'].str.lower()


        # Save to a CSV file
        df.to_csv('lyst_hottest_brands_' + year + '_' + quarter + '.csv', index=False)

        #Check that CSV is correct
        print(df)
    else:
        print('Failed to retrieve the webpage')



##SCRAPING DIV_AND_H3 LYSTS##


for list_name in div_and_h3:

    # URL of the Lyst Hottest Brands Index page for the given Q
    url = 'https://www.lyst.com/' + list_name

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        #Create data collectors
        data = {'Rank': [], 'Brand': []}

        # Find the elements containing the brand names and rankings, filter out past rankings.
        rankings = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == [div_and_h3[list_name][0]])
        brands = soup.find_all('h3', class_=div_and_h3[list_name][2])


        # Ensure that both lists have the same length
        if len(rankings) == len(brands):
            for i in range(len(rankings)):
                rank = rankings[i].text.strip()
                name = brands[i].text.strip()
                data['Rank'].append(rank)
                data['Brand'].append(name)
        else:
            print('Mismatch in the number of rankings and brands', div_and_h3[list_name][3], div_and_h3[list_name][4])

        # Create the dataframe
        df = pd.DataFrame(data)

        #Add year and quarter columns
        year = div_and_h3[list_name][3]
        quarter = div_and_h3[list_name][4]

        df['Year'] = year
        df['Quarter'] = quarter

        #Convert all brand names to lowercase
        df['Brand'] = df['Brand'].str.lower()


        # Save to a CSV file
        df.to_csv('lyst_hottest_brands_' + year + '_' + quarter + '.csv', index=False)

        #Check that CSV is correct
        print(df)
    else:
        print('Failed to retrieve the webpage')



##SCRAPING DIV_AND_A LYSTS##


for list_name in div_h3_and_a:

    # URL of the Lyst Hottest Brands Index page for the given Q
    url = 'https://www.lyst.com/' + list_name

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        #Create data collectors
        data = {'Rank': [], 'Brand': []}

        # Find the elements containing the brand names and rankings, filter out past rankings.
        rankings = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == [div_h3_and_a[list_name][0]])
        brands = soup.find_all('h3', class_=div_h3_and_a[list_name][1])


        # Ensure that both lists have the same length
        if len(rankings) == len(brands):
            for i in range(len(rankings)):
                rank = rankings[i].text.strip()
                name = brands[i].text.strip()
                data['Rank'].append(rank)
                data['Brand'].append(name)
        else:
            print('Mismatch in the number of rankings and brands')

        # Create the dataframe
        df = pd.DataFrame(data)

        #Add year and quarter columns
        year = div_h3_and_a[list_name][2]
        quarter = div_h3_and_a[list_name][3]

        df['Year'] = year
        df['Quarter'] = quarter

        #Convert all brand names to lowercase
        df['Brand'] = df['Brand'].str.lower()


        # Save to a CSV file
        df.to_csv('lyst_hottest_brands_' + year + '_' + quarter + '.csv', index=False)

        #Check that CSV is correct
        print(df)
    else:
        print('Failed to retrieve the webpage')



##SCRAPING DIVS_H4_AND_A LYSTS##


for list_name in divs_h4_and_a:

    # URL of the Lyst Hottest Brands Index page for the given Q
    url = 'https://www.lyst.com/' + list_name

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        #Create data collectors
        data = {'Rank': [], 'Brand': []}

        # Find the elements containing the brand names and rankings, filter out past rankings.
        rankings = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == [divs_h4_and_a[list_name][0]])
        brands = soup.find_all('h4', class_=divs_h4_and_a[list_name][1])


        # Ensure that both lists have the same length
        if len(rankings) == len(brands):
            for i in range(len(rankings)):
                rank = rankings[i].text.strip()
                name = brands[i].text.strip()
                data['Rank'].append(rank)
                data['Brand'].append(name)
        else:
            print('Mismatch in the number of rankings and brands')

        # Create the dataframe
        df = pd.DataFrame(data)

        #Add year and quarter columns
        year = divs_h4_and_a[list_name][2]
        quarter = divs_h4_and_a[list_name][3]

        df['Year'] = year
        df['Quarter'] = quarter

        #Convert all brand names to lowercase
        df['Brand'] = df['Brand'].str.lower()


        # Save to a CSV file
        df.to_csv('lyst_hottest_brands_' + year + '_' + quarter + '.csv', index=False)

        #Check that CSV is correct
        print(df)
    else:
        print('Failed to retrieve the webpage')