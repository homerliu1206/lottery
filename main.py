import random

# Create random numbers
lottery_numbers = set()
for i in range(5):
    rdnum = random.randint(1, 25)
    lottery_numbers.add(rdnum)

# Player_1
name_1 = input("Enter the name of player_1: ")
num_1 = {}
num_1["Player"] = name_1
num_list_1 = set()
for i in range(5):
    type_num_1 = input("Enter 5 numbers of guess (1~25): ")
    num_list_1.add(int(type_num_1))
    num_1["numbers"] = num_list_1

# Player_2
name_2 = input("Enter the name of player_2: ")
num_2 = {}
num_2["Player"] = name_2
num_list_2 = set()
for i in range(5):
    type_num_2 = input("Enter 5 numbers of guess (1~25): ")
    num_list_2.add(int(type_num_2))
    num_2["numbers"] = num_list_2

# Intersection
inter_1 = len(lottery_numbers.intersection(num_1["numbers"]))
inter_2 = len(lottery_numbers.intersection(num_2["numbers"]))
print ("Player", num_1["Player"], "got", inter_1, "numbers right.")
print ("Player", num_2["Player"], "got", inter_2, "numbers right.")