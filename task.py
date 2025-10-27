import requests
url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

response = requests.get(url)
data = response.json()
usd_rate = 0
eur_rate = 0
date = ""
for item in data:
    if item["Ccy"] == "USD":
        usd_rate = float(item["Rate"])
        date = item["Date"]
    elif item["Ccy"] == "EUR":
        eur_rate = float(item["Rate"])

amount = float(input("Summa:"))
from_currency = input("Qaysi valyutadan ")
to_currency = input("Qaysi valyutaga  ")

result = 0

if from_currency == "USD" and to_currency == "UZS":
    result = amount * usd_rate
elif from_currency == "UZS" and to_currency == "USD":
    result = amount / usd_rate
elif from_currency == "EUR" and to_currency == "UZS":
    result = amount * eur_rate
elif from_currency == "UZS" and to_currency == "EUR":
    result = amount / eur_rate
elif from_currency == "USD" and to_currency == "EUR":
    result = amount * usd_rate / eur_rate
elif from_currency == "EUR" and to_currency == "USD":
    result = amount * eur_rate / usd_rate
else:
    print("Xatolik!!!")
print(f"\n {amount:,.2f} {from_currency} = {result:,.2f} {to_currency} ({date})")