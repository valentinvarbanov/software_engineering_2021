# Instructions

In order to create crypto currencies, you should create them via the Python terminal.
You can enter the mode of this terminal by typing:

```
python3 manage.my shell
```

Then you will be able to create some crypto currencies. You can use the examples below:

```
from crypto.models import Currency

currency1 = Currency(name="Bitcoin", price=55000, code="BTC", supply=10000)
currency2 = Currency(name="Ethereum", price=4000, code="ETH", supply=20000)
currency3 = Currency(name="Litecoin", price=200, code="LTC", supply=30000)
currency4 = Currency(name="Bitcoin Cash", price=600, code="BCH", supply=40000)
currency5 = Currency(name="XRP", price=2, code="XRP", supply=50000)
currency6 = Currency(name="DASH", price=185, code="DASH", supply=60000)
currency7 = Currency(name="Cardano", price=3, code="ADA", supply=70000)

currency1.save()
currency2.save()
currency3.save()
currency4.save()
currency5.save()
currency6.save()
currency7.save()

exit()
```
