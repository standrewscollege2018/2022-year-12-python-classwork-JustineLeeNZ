# create list
client_list = [ ['John Smith', 16], ['Bob Roberts', 18], ['Tui Ramere', 25] ]

print(client_list)

# get 1st client's name
name= client_list[0][0]

print(name)

# get 2nd client's age
age = client_list[1][1]

print(age)


# for with temporary variable
for client in client_list:
    print("Name: ", {client[0]}, " Age: ", {client[1]})