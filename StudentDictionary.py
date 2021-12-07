userdata = {"data": []}


def fil_userdata(name, age, dept, phone):
    student = {"name": name, "age": age, "stream": dept, "contact_number": phone}
    add_user(student)


def add_user(student):
    userdata["data"].append(student)


fil_userdata('abc', '21', 'IT', '1234556789')
fil_userdata('def', '21', 'IT', '7854996523')
fil_userdata('ghi', '21', 'IT', '7453201563')
fil_userdata('jkl', '21', 'IT', '8520369874')

print(userdata)
