test_list = ['abc', 'def', 'ghi', 'abc', 'abc']

print("The original list is : ", test_list)

oc_set = set()
res = []
for idx, val in enumerate(test_list):
    if val not in oc_set:
        oc_set.add(val)
    else:
        res.append(idx)

print("The list of duplicate elements is :  ", res)
