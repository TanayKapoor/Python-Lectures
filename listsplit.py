# Declarations
ls_start = ['abc', 'acd', 'def', 'ghi']
ls_last = ['jkl', 'mol', 'abf', 'ghl']
search = input('Enter the first letter: ')
search_2 = input('Enter the first letter: ')
ls_st = []
ls_st_1 = []
ls_end = []
ls_end_1 = []

# Checking for beginning
print("\nChecking for starting...")
for i in range(len(ls_start)):
    if ls_start[i].startswith(search):
        ls_st.append(ls_start[i])

for i in ls_st:
    print(i, "length is", len(i))

print("Numbers containing", search, "are", ls_st)
print("Numbers not containing", search, "are", ls_end)


# Checking for ending
print("\nChecking for ending...")
for i in range(len(ls_last)):
    if ls_last[i].endswith(search_2):
        ls_st_1.append(ls_last[i])

for i in ls_st_1:
    print(i, "length is", len(i))

print("Numbers ending", search_2, "are", ls_st_1)
print("Numbers not ending", search_2, "are", ls_end_1)
