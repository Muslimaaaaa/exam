import requests
import json
import threading
from task1 import database

product_url = requests.get(' https://dummyjson.com/products/ ')
user_url = requests.get(' https://dummyjson.com/products/ ')

product_list = product_url.json()['product']
query = '''insert into product() values(%s,%s,%s);'''
for product in product_list:
    database.execute(query, (product['name'], product['price'], product['']))

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as f:
        json.dump(response.json(), f, indent=4)
        print(response.status_code)

urls = [
    ('https://dummyjson.com/products', 'products.json'),
    ('https://dummyjson.com/users', 'users.json')
]

threads = [
    threading.Thread(target=download_file, args=(url, filename))
    for url, filename in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
