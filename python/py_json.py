# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample json 
userJSON_nkh ='{"first_name": "lana" ,"last_name":"mohammed","age": 16 }'

#parse to dic 
user_nkh = json.loads(userJSON_nkh)
#print(user_nkh['first_name'])
#print(user_nkh)

car_nkh = {'make': 'ford','model':'mustange','year': 1980 } 
carJSON_nkh = json.dumps(car_nkh)
print(carJSON_nkh)
