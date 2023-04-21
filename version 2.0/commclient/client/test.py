import json

from client.utils import ConfigUtil

import requests
if __name__ == '__main__':
    url = ConfigUtil.read_serverUrl().replace("\"", "") + "info/updateOnline"
    print(url)
    clientName = ConfigUtil.read_clientName()
    print(clientName)
    headers = {
        'Content-Type': 'application/json',
    }
    data = {'clientName': clientName.replace("\"", ""), 'online': "1"}
    print(data)
    result = requests.post(url, headers=headers, data=json.dumps(data))
    print(result)
