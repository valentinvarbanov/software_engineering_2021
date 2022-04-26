
# Continuous Integration

## Run `pylint`

Use the file `code.py` for this. Run `pylint` and resolve the found issues in order to achieve a score of 10.0

Note: You can suppress no more than **4** types of issues.

```
$ pylint code.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

## Create a GitHub Action

Create a GitHub Action that runs `pylint` over the updated code. 

Requirements:
* The action should trigger on pull request for main branch.
* The action should trigger only on changes in your folder (xx_firstname_lastname). 

## Upload

Create a pull request and merge it into main. Files should be uploaded to the following locations:
* `tasks/xx_firstname_lastname/`
* `.github/workflows/task_ci_xx_firstname_lastname.yaml`

Example: 
* .github/workflows/
  * task_ci_05_ivan_ivanov.yaml
* tasks/continuous_integration/05_ivan_ivanov/
  * code.py

