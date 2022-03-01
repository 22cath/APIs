import requests

respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=620B201C-09FA-4757-9A9E-E7E431EAEF68")

print(respuesta.status.code)

data = respuesta.json()

print(data["rates"][3])
