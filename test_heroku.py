import requests
import json

# POST
# load the test data
with open('testdata.json', 'r') as f:
    testdata = json.load(f)

r = requests.post('https://mysterious-reef-90699.herokuapp.com/predict', json={'newdata': testdata})
#print(r.json())
data = r.json()

print('Good day to you. The prediction for the data is: ', data)
