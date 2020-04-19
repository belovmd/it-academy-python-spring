## Homework5 review

### Homework5 evaluation
- Maximum score is +10 minimum is 0.
- Completed tasks 1, 2, 3, 5(with binary logic), 6(with binary logic) are scored
as +1 for each.
- Completed tasks 4 scores as +2.
- +1 for Task 4 has O(n) solution. 
- +1 if tasks 1 doesn't depend on func names, and can run any functions.
- +1 for good namings, code structure, overall impression.
- PR that doesn't pass any of PR checklist checks takes -0,5.
- PR that doesn't pass any 2 of PR checklist checks takes -3.
- All review comments should be addressed (either fixes or 
substantiation of your position) . Missed comments causes score 
penalties.

### PR checklist
Please make sure you've passed PR checklist
- [ ] my PR passes CI checks (flake8 and pycodestyle)
- [ ] my PR named according guidelines: `Homework5: Name Surname`
- [ ] my PR contains complete tasks descriptions for all tasks
- [ ] my PR made from fork feature brunch to Maxim master branch.
- [ ] my PR don't contain only code that solves Homework4 tasks.
Redundant files (configs, etc. ) are put to .gitignore


### Review notes:
1. Please add imdb results - histograms. 
2. Please remove ratings.list file from PR.
3. Task 1. What if our attribute not a function and can't be run.
4. Task 1. Your code doesn't call function. 
5. Task 2. We can also add function name, datetime.
6. Task 3. Looks like O(n**2). Can be solved with O(n).
7. Task 4. Missed histograms.
8. Redundant files in PR. 
9. Task 4. It looks not like histograms. 
10. Task 1. We have isinstance(open, types.FunctionType).
11. Task 1. It wouldn't work for functions w/o parameters. 
12. Unclear naming.
13. Redundant comments.
14. Task 2. Your code doesn't solve task.
15. Task 1. It can have other attributes. 
16. Task 1. Solution is not generic - works only with your class. 
17. Task 2. What if decorated functions have parameters? 
18. Task 4. Looks like O(n**2). Can be solved with O(n)
19. Please don't use '\\'.
20. Task 6. Redundant operations in solution (with `log`)