import requests
from datetime import datetime
nu = datetime.now()
print(nu)
response = requests.get("https://api.myip.com", timeout=10)
data = response.json()
ip = data.get("ip")
print (ip)
country = data.get("country")
print (country)
        
