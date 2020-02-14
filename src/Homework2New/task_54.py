"""Sum finder around every number of list"""

element_numbers = input()

nmb_list = [int(el) for el in element_numbers.split()]
result = []
if len(nmb_list) == 1:
    print(nmb_list[0])
else:
    for i, value in enumerate(nmb_list):
        if i == 0:
            result.append(str(nmb_list[1] + nmb_list[-1]))
        elif i == len(nmb_list) - 1:
            result.append(str(nmb_list[0] + nmb_list[-2]))
        else:
            result.append(str(nmb_list[i-1] + nmb_list[i + 1]))
    print(' '.join(result))
