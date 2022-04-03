import requests

response = requests.get("http://ip-api.com/json/?fields=61439",proxies=dict(http="socks5://127.0.0.1:9050",https="socks5://127.0.0.1:9050")).json()["query"]
print(response)