set_1 = {"Scorpion", "Sub-Zero", "Liu Kang", "Kung Lao", "Raiden", "Fujin"}
set_2 = set(("Quan Chi", "Shinnok", "Shao Kahn"))

print("Tipe data set_1 adalah ", type (set_1))
print("Tipe data set_2 adalah ", type (set_2))
print("Team 1: ", set_1)
print("Team 2: ", set_2)
print("---------------------------------------------")

# Print every item of set_1
for x in set_1:
    print(x)
print("---------------------------------------------")

# Check if a key exist
if "Quan Chi" in set_1:
    print("No, Quan Chi is not in team 1.")

# Add an item
set_1.add("Johnny Cage")
print(set_1)

# Add multiple items
set_1.update(["Jacqui Briggs","Jaxton Briggs","Sonya Blade"])
print(set_1)

# Part 2
# Remove an item (method 1)
set_1.remove("Liu Kang")
print(set_1)
print("Liu Kang has died")

# Remove an item (method 2)
set_1.discard("Kung Lao")
print(set_1)
print("Kung Lao has left the team")

# Delete (pop) last inserted key
set_1.pop()
print(set_1)
print("Ultimate betrayal")

# Clear the set
set_1.clear()
print(set_1)
print("All team members has been wiped out!")

# Delete the set
del set_1
print("---------------------------------------------")

# Union of two sets
set_1 = {"Shang Tsung", "Quan Chi"}
set_2 = {1, 2}
set_3 = set_1.union(set_2)
print(set_3)
print("The deadly alliance have reborn")
print("---------------------------------------------")

# set_1 takes copies of all items of set 2
set_1 = {"Smoke", "Noob"}
set_2 = {1, 2}
set_1.update(set_2)
print(set_1)