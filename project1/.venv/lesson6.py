import requests
import time

while True:
    my_headers = {'Content-Type':'application/json'}
    my_params={'value1':'50', 'value2':'60'}
    r = requests.get('https://maker.ifttt.com/trigger/事件名稱/with/key/你的金鑰',
                    params=my_params,
                    headers=my_headers)
    print(r.url)        
    print(r.status_code)
    time.sleep(60)