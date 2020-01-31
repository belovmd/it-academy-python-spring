# 9 lines: Opening files
# indent your Python code to put into an email
import glob
py_files = [py_file for py_file in glob.iglob(r'.\*.py')]
for file_name in sorted(py_files):
    print('    -------' + file_name)

    with open(file_name) as f:
        for line in f:
            print('     ' + line.rstrip())

    print()
