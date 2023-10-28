from bs4 import BeautifulSoup
import requests
import os
from google.colab import drive

# Google Driveをマウント
drive.mount('/content/drive')

# ウェブページのURLを指定
url = 'https://example.com'

# ウェブページからデータを取得
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# <tbody> タグを探す
tbody_tags = soup.find_all('tbody')


directory_path = '/content/drive/My Drive/example'
existing_files = os.listdir(directory_path)
existing_numbers = [int(filename.split('_')[-1].split('.')[0]) for filename in existing_files if filename.startswith('finland_word_')]
next_number = max(existing_numbers, default=-1) + 1


with open(f'{directory_path}/finland_word_{next_number}.txt', 'w', encoding='utf-8') as file:
    for tbody in tbody_tags:
        rows = tbody.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            row_data = []
            for column in columns:
                if "フィンランド語名" in column.get_text():
                    row_data.append(column.get_text() + ":")
                else:
                    row_data.append(column.get_text() + ",")
            file.write(''.join(row_data)[:-1] + '\n') 

print(f'ファイルを {directory_path} に保存しました。')
