import requests, json
from bs4 import BeautifulSoup

months = {
    "január": 1, "február": 2, "március": 3, "április": 4,
    "május": 5, "június": 6, "július": 7, "augusztus": 8,
    "szeptember": 9, "október": 10, "november": 11, "december": 12,
}

response = requests.get('https://hu.wikipedia.org/wiki/Magyar_n%C3%A9vnapok_list%C3%A1ja_bet%C5%B1rendben')
page = BeautifulSoup(response.text, 'html.parser')
li_tags = page.find_all('li')
scraped_data = {}

for li in li_tags:
    b_tag = li.find('b')
    if b_tag:
        first_a_tag = b_tag.find('a')
        if first_a_tag:
            item_name = first_a_tag.text
        else: continue

        date_a_tags = li.find_all('a')[1:]
        for date_a_tag in date_a_tags:
            item_date = date_a_tag.text
            if item_date not in scraped_data:
                scraped_data[item_date] = []
            scraped_data[item_date].append(item_name)

def date_convert(date_str: str):
    month_str, day_str = date_str.split()
    month_num = int(months[month_str])
    day_num = int(day_str[:-1])
    return (month_num, day_num)

sorted_scraped_data = sorted(scraped_data.items(), key=lambda item: date_convert(item[0]))
output = {}
for date_str, name in sorted_scraped_data:
    month_num, day_num = date_convert(date_str)
    if month_num not in output:
        output[month_num] = {}
    output[month_num][day_num] = name

with open('nevnapok.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=4)

print("kesz :)")
