# Consuming a REST API

## `requests` package

The [`requests`](https://docs.python-requests.org/en/latest/) is easy to use library for making HTTP requests to an API.

## Coindeck API

The [Coindeck API](https://old.coindesk.com/coindesk-api) is what we call a free and public API. Meaning that everyone can consume the API without paying and the documentation is available for everyone.

An API endpoint is called the url via which the data can be accessed - https://api.coindesk.com/v1/bpi/currentprice.json

## Requesting the data

An HTTP GET request can be send using the `get()` method:

```python
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
```

Its recommended that the status code is checked before using the received data:

```python
>>> response.status_code
200
```

Status code 200 means OK. HTTP status codes are well known.

Data is accessed via the `text` property or via the helper `json()` method that returns a python `dict` object.

```python
>>> response.text
'{"time":{"updated":"Oct 21, 2021 18:27:00 UTC", ...'
>>> response.json()
{'time': {'updated': 'Oct 21, 2021 18:27:00 UTC', ... }
```