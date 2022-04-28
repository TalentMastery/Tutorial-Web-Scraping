import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {
    "usd":
        {
        "code": "USD", "alphaCode": "USD", "numericCode": "840", "name": "U.S. Dollar", "rate": 6.9103669538454e-5,
        "date": "Thu, 28 Apr 2022 11:55:01 GMT", "inverseRate": 14471.011549445
        },
    "eur":
        {
        "code": "EUR", "alphaCode": "EUR", "numericCode": "978", "name": "Euro", "rate": 6.5680477992806e-5,
        "date": "Thu, 28 Apr 2022 11:55:01 GMT", "inverseRate": 15225.224154269
        }
}

# print (json_data.json())
# print(json_data)
for data in json_data.values():
    # print(data)
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
