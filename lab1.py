import requests

res = requests.get("https://raw.githubusercontent.com/dennea/404_lab1/main/lab1.py")

print(res.text)
