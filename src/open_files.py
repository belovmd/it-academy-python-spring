# 9 lines: Opening files
# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print(f'     -------{file_name}')

    with open(file_name) as f:
        for line in f:
            print(f'     {line.rstrip()}')

    print()
