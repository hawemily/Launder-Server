import requests
import ichackr.py

data = {"time": 2401181530, "color": "Dark", "loadSize"="half", "gender"="female"}
url = "http://127.0.0.1:5000/createLaundryRequest"
r = requests.post(url, data=json.dumps(data))
r.status_code