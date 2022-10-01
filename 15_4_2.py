import json

requirement = {
    'timestamp': int,
    'referer': str,
    'location': str,
    'remoteHost': str,
    'partyId': str,
    'sessionId': str,
    'pageViewId': str,
    'eventType': str,
    'item_id': str,
    'item_price': int,
    'item_url': str,
    'basket_price': str,
    'detectedDuplicate': bool,
    'detectedCorruption': bool,
    'firstInSession': bool,
    'userAgentName': str
}
# print(requirement.keys())
def fields(responce):
    a = set(responce.keys()).difference(set(requirement.keys()))
    if a == set():
        return True
    else:
        print(f'Поля {a} не должны содержаться в ответе')


def countFields(responce):
    if len(responce.keys()) == len(requirement.keys()):
        return True
    else:
        print("Ответ содержит лишние поля")

def types(responce):
    result = True
    for key, value in requirement.items():
        if type(responce[key]) == value:
            if key in  ('referer', 'location', 'item_url'):
                if 'http://'  not in responce[key] and 'https://' not in responce[key]:
                    print(f'Поле {key} не содержит "http://" или "https://"')
                    result = False
            if key == 'eventType':
                if 'itemBuyEvent' not in responce[key] and 'itemViewEvent' not in responce[key]:
                    print('Поле "eventType" не соответствует требованиям')
                    result = False

        else:
            print(f'Значение поля {responce[key]} не соответствует типу')
            result = False
    return result

with open('test.json') as f:
    resp = json.load(f)


for i in range(len(resp)):
    c = fields(resp[i])
    d = countFields(resp[i])
    e = types(resp[i])
    if c and d and e:
        print('Pass')
    else:
        print('Faild')





