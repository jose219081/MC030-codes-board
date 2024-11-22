import ujson
import urequests

firebase_url = 'https://bees-f6e6b-default-rtdb.firebaseio.com/bee_data'

def read_data():
    response = urequests.get(firebase_url + '.json')
    response.close()
    if response.status_code == 200:
        data = response.json()
        print('Data read from Firebase:', data)
        return data
    else:
        print('Failed to read data:', response.status_code)
        return None

def write_data(data):
    headers = {'Content-Type': 'application/json'}
    response = urequests.put(firebase_url + '.json', data=ujson.dumps(data), headers=headers)
    response.close()
    if response.status_code == 200:
        print('Data written to Firebase successfully')
    else:
        print('Failed to write data:', response.status_code)

def patch_data(data):
    headers = {'Content-Type': 'application/json'}
    response = urequests.patch(firebase_url + '.json', data=ujson.dumps(data), headers=headers)
    response.close()
    if response.status_code == 200:
        print('Data patched in Firebase successfully')
    else:
        print('Failed to patch data:', response.status_code)