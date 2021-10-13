# REST API

## API

Application Programming Interface (API) is the user facing function/methods/endpoints/etc. of a software that a programmer could use to interact with this software. Often this is split logically into Public API and Private API. The public API is those subset of function/methods/endpoints/etc. that are available to be used outside of the module. The Private API is the remaining function/methods/endpoints/etc. that are used internally for supporting the Public API.


## REST, RESTful

Representational state transfer (REST) is an architecture style. 

REST defines a set of architectural constraints. An API could be called RESTful if this API satisfies the architectural constraints.

Detailed explanation can be found [here](https://en.wikipedia.org/wiki/Representational_state_transfer).

## Serialization and de-serialization of data

Serialization means transforming a object type to a plain data type (e.g. python object to a json/xml/etc).

De-serialization is the same process, but in reverse, transforming a plain data to a object. (e.g. creating a python object from json/xml/etc.)

Serialization is done before the data is sent over the network and de-serialization when the data is received on the destination for easier processing.

## Django rest framework

Official quick start guide - https://www.django-rest-framework.org/tutorial/quickstart/

Guide followed in class - https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/