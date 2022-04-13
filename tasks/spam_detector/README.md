
# Email spam detection


## Email generator API endpoint

```
https://random-data-api.com/api/users/random_user
```

Sample response:
```
{
  ...
  "email": "luis.bernhard@email.com",
  ...
}
```

## Create a program

The program should use the api to generate a email and score the generated spam likelyhood.

Rules:

* If the generated email is one of `john@win-supp.com`, `windows.support@gmail.com` or `today@promo.com` it's spam likelyhood is `1.0`. (known bad)
* The base spam likelyhood is `0.0`. If a criteria is met it's likelyhood increases:
  * End in  `.cn`, `.in` or `.info` -> +0.25 spam likelyhood
  * Has a number (0-9) -> +0.25 spam likelyhood
  * Has two or more occurances of `.` and `-` in the domain  -> +0.50 spam likelyhood

Examples:

|email|spam likelyhood|description|
|---|---|---|
|`today@promo.com` | `1.0`| email matches list |
|`example@mail.cn` | `0.25`| ending |
|`example123@mail.cn` | `0.50`| ending + number |
|`example@mail123.cn` | `0.50`| ending + number |
|`example@ma.il.com` | `0.50`| two or more occurances (. or -) |
|`example@ma-il.com` | `0.50`| two or more occurances (. or -) |
|`example123@ma-il.cn` | `1.0`| ending + number + two or more occurances (. or -) |

## Unit tests

Create needed unit tests to confirm that your evaluation logic works. Unit tests should cover all cases listed above.

## Upload

Create a pull request and merge it into /tasks/xx_firstname_lastname/

Example: 

* 05_ivan_ivanov/
  * email.py
  * test_email.py
