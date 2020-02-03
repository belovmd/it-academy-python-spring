def namelist(names):
    """Instructions

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'
    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'
    namelist([])
    # returns ''
    """
    name_list = [name['name'] + ',' if i != len(names) - 2
                 else name['name'] + ' &' for i, name in enumerate(names)]
    return ' '.join(name_list)[:-1]


if __name__ == '__main__':
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
