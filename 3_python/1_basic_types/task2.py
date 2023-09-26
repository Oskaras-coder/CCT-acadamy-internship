def create_a_dic(p):
    new_dic = {
        "name": p.get("name", "Unknown"),
        "karma": p.get("karma", "Unknown")
    }
    return new_dic


p1 = {'name': 'Foo', 'karma': 123, 'value': -1}
p2 = {'karma': 123, 'value': -1}
p3 = {'name': 'Foo', 'value': -1}

print(create_a_dic(p1))
print(create_a_dic(p2))
print(create_a_dic(p3))