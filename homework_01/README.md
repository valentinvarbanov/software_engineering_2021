# Create a feeling lucky page

## Create a `lucky` page in the crypto project

The aim of this page is to give a suggestion to a "lucky" crypto investor. It will give a suggestion that will have the chance of making the investor very very rich. It chooses which currency is the "lucky" one according to what we will call "the algorithm"

The page should be accessible via the following path: `SITE:PORT/crypto/lucky`.

## "the algorithm"

Find what is your number in class. 

Example: Ivan Ivanov - 5

Now divide the number by 4 with remainder (modulo). The result will be used as what we will call "base value" for the algorithm.

According to the "base value" the algorithm should choose:
- `0` - Find the currency with the highest market cap (cap = price * supply). This is the lucky one. (This is lucky as it may be the most stable currency.)
- `1` - Find the bottom 3 currencies with the lowest price and select one by random from those 3. This is the lucky one. (This is lucky as it may be as it has the higher growth potential.)
- `2` - Find the currency with the lowest market cap (cap = price * supply). This is the lucky one. (This is lucky as it may grow by a lot in short period of time.)
- `3` - Find the top 3 currencies with the highest price and select one by random from those 3. This is the lucky one. (This is lucky as it may be the highest valued currency.)

## Bonus

Add some nice looking style (anything more than a plain html), that displays the currency name, price, etc.

## Where to upload the homework?

Upload your files in a folder named `xx_firstname_lastname` the current folder(`homework_01`) where:
- `xx` is your number in class
- `firstname` is your first name
- `lastname` is your last/family name

Example: 05_ivan_ivanov

Commit only the files that contain changes.

Example: views.py has changes

```
homework_01/
├── 05_ivan_ivanov
│   ├── ...
│   └── views.py
└── README.md
```

## Deadline

```
Sun, 17 Oct 2021 23:59:59 +0300
```