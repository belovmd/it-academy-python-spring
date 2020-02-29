## Homework1 review

### Homework1 evaluation
- Maximum score is +1 minimum is 0.
- PR with 120+ rows evaluates as +1.
- PR with 80+ rows evaluates as +0,5.
- PR that doesn't pass any of PR checklist checks takes -0,5.
- PR that doesn't pass any 2 of PR checklist checks takes -1.
- All review comments should be addressed. Missed comments causes score 
penalties.

### PR checklist
Please make sure you've passed PR checklist
- [ ] my PR passes CI checks (flake8 and pycodestyle)
- [ ] my PR named according guidelines: `Homework1: Name Surname`
- [ ] my PR contains complete tasks descriptions for all tasks
- [ ] my PR made from fork feature brunch to maxim master branch.
- [ ] my PR don't contain only code that solves Homework1 tasks.
Redundant files (configs, etc. ) are put to .gitignore


### Review notes:
1. It looks much more clear if you task description stands closely to task and 
separated from other tasks with two blank lines: 
    ```python
   pass  # last line of previous task
    
 
   # next task docstring
   pass  # my next task first line  
    ```
2. Missed tasks descriptions (in our HW just tasks titles)
3. Contains code for HW2. 
4. Config files in PR
5. Redundant commented code in PR (PR should contain only comment for code, not
pieces of commented code)
6. Please don't put code to \_\_init__.py file - create your own. This files is
 needed just for packages.
7. Failed code style checks.
8. Please add additional tasks for bigger score
9. Tasks descriptions should be separated with either one or two blank lines 
everywhere (it's not accurate to separate it with one line in one files and with
 two in another)
10. PR should be named according to our guidelines.
11. Please don't remove \_\_init__.py file