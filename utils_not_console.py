def currency_rates(name_currency):
    import requests
    import xml.etree.ElementTree as ET
    from datetime import datetime

    path = "http://www.cbr.ru/scripts/XML_daily.asp"

    response = requests.get(path)

    xmlDict = {}
    root = ET.fromstring(response.content)

    num_currency = len(list(root))

    count = 0
    while num_currency > count:
        if root[count][1].text == name_currency:
            print(datetime.strptime(root.attrib['Date'], '%d.%m.%Y').date())
            print(f"Курс валюты: {root[count][4].text}", name_currency)
            break
        count += 1
    else:
        print(None)
