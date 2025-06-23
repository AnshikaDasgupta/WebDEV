# friends = open("MyFriends.txt","w")
# friends.write("adib\n")
# friends.write("mita\n")
# friends.write("banica\n")
# friends.close()

# friends = open("MyFriends.txt","a")
# friends.write("Carlos\n")
# friends.close()

friends = open("MyFriends.txt","r")

# print(friends.read())
print(friends.readline())
print(friends.readlines())

friends.close()
