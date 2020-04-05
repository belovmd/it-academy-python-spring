## Homework4 review

### Homework4 evaluation
- Maximum score is +10 minimum is 0.
- Completed tasks 1, 3, 4, 6 are scored as +5.
- Completed tasks 2, 5, 7 are scored as +1 each.
- +1 for Task 2 if you handle situation when Brest is in Belarus and France. 
- +1 for good namings, code structure, overall impression.
- PR that doesn't pass any of PR checklist checks takes -0,5.
- PR that doesn't pass any 2 of PR checklist checks takes -3.
- All review comments should be addressed (either fixes or 
substantiation of your position) . Missed comments causes score 
penalties.

### PR checklist
Please make sure you've passed PR checklist
- [ ] my PR passes CI checks (flake8 and pycodestyle)
- [ ] my PR named according guidelines: `Homework4: Name Surname`
- [ ] my PR contains complete tasks descriptions for all tasks
- [ ] my PR made from fork feature brunch to Maxim master branch.
- [ ] my PR don't contain only code that solves Homework4 tasks.
Redundant files (configs, etc. ) are put to .gitignore


### Review notes:
1. Task 2. It looks as a good idea to invert dict - {city:country}. It would 
allow not to have O(n**2) complexity. Please be aware that one city still can
be in different countries 
2. Task 5. Please use sets intersection for languages that knows every pupil.
3. Task 2. Magic numbers. 
4. Task 2. Too complex input. You can try `a, *b = input()`
5. Task 2. Output isn't consistent with one in task description. 
6. `for _ in ...` if you don't need this variable
7. Task 5. Unclear namings. 
8. Task 2. Unclear naming. 
9. Task 2. Input can be improved.
10. Task 4. Solution don't solve task in task description.
11. Task 5. Too many magic numbers.
12. Task 5. Symmetric difference don't solve task in description. 
13. Task 6. It has one-line solution. According to task description all non-space
symbols in sequence are word. 
14. Task 1. We can use one line return here without temporary variables.
15. Please done use `\` line break. 
16. Task 2. Dict would be more native here instead of list. 
17. Task 3. Too complex. Set should be used. 
18. Task 4. Too complex. Set should be used.
19. Task 5. Too complex. Set should be used.
20. Task 7. Euclid algorithm doesn't expect to have result in sum. it's just a
hack from your side not to figure out where `0` and where result. 
21. Task 4. It's task for symmetric difference.
22. Redundant files in PR
23. Task 1. Too complex
24. Task 5. Too complex solution for at least one pupil. Why do we need random at all? 
25. Missed sanity checks (redundant files in PR)
26. Please don't remove \_\_init__ file
27. Please put two empty lines between task. No empty lines between task number
and task description
28. Missed sanity checks (missed tasks descriptions)
29. Task 2. One of best solutions. But be aware Brest is in France and Belarus.
30. Missed Task 4
31. Task 3. Doesn't solve task in description.
