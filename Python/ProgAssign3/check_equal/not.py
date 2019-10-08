def are_all_members_same(list):
    return all(i == list[0] for i in list)
    print()

# Driver code

print(are_all_members_same([42,42,42,43,42]))
print(are_all_members_same([42,42,42,42]))