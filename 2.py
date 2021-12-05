import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_first_element_tree():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_all_fields(channel: ET.Element):
    news = []
    for i in channel.findall('item'):
        fields = {}
        for field in i:
            fields[field.tag] = field.text
        news.append(fields)
    return news


def save_json(first_element):
    json_file = json.dumps(get_all_fields(first_element), ensure_ascii=False).encode('utf8')
    with open("all_fields_news.json", 'wb') as file:
        file.write(json_file)


first_element_tree = get_first_element_tree()
save_json(first_element_tree)
