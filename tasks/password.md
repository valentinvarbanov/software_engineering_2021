
# Password verification


## Password generator API endpoint

```
https://passwordinator.herokuapp.com/generate
```


## Create a program

The program should use the api to generate a password and score the password complexity.

Rules:

* If the generated password is one of `12345`, `qwerty`, `password` or `asdf` its complexity is `0.0`.
* The base complexity is `0.0`. In a criteria is met it's complexity increases:
  * Has a letter(upper or lower) -> +0.25 complexity
  * Has one of `?`, `!`, `*`, `%`, `$` or `@`  -> +0.25 complexity
  * Has more than 8 characters -> +0.5 complexity

Examples:

|password|complexity|description|
|---|---|---|
|`password` | `0.0`| password matches list |
|`elsys` | `0.25`| has letter |
|`el$y$` | `0.50`| has letter + special |
|`elsyselsys` | `0.75`| has letter +  more than 8 |
|`el$y$el$y$` | `1.0`| has letter + special + more than 8 |

## Unit tests

Create needed unit tests to confirm that your evaluation logic works. Unit tests should cover all 5 cases listed above.

## Upload

Create a pull request and merge it into /tasks/xx_firstname_lastname/

Example: 
 *  05_ivan_ivanov/
    ** password.py
    ** test_password.py
