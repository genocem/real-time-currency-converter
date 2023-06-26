from PyQt5.QtWidgets import  QApplication
from PyQt5.uic import loadUi
import requests
def get_currency_exchange_rate(from_currency, to_currency):
    api_key = '5PPNSNRLSU9W1J21' 
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return exchange_rate


currencies = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BZD","CAD","CDF","CHF","CLF","CLP","CNH","CNY","COP","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","ICP","IDR","ILS","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RUR","RWF","SAR","SBDf","SCR","SDG","SDR","SEK","SGD","SHP","SLL","SOS","SRD","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"]

app = QApplication([])
window = loadUi("untitled.ui")
window.comboBox.addItems(currencies)
window.comboBox_2.addItems(currencies)
window.show()




def currency ():



    amount = window.lineEdit.text()

    from_currency = window.comboBox.currentText() 

    to_currency = window.comboBox_2.currentText()

    exchange_rate = get_currency_exchange_rate(from_currency, to_currency)

    print(f"The exchange rate from {from_currency} to {to_currency} is: {exchange_rate}")

    output = round(float(amount)*float(exchange_rate),3)


    window.label_2.setText(f'<html><head/><body><p align="center" style="font-size:14pt;">{str(output)}</p></body></html>')



window.pushButton.clicked.connect(currency)


app.exec()


