set_1 = {"Toyota", "Daihatsu", "Honda"}
set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data set_1 adalah ", type (set_1))
print("Tipe data set_2 adalah ", type (set_2))
print("Data set_1: ", set_1)
print("Data set_2: ", set_2)
print("---------------------------------------------")

# Print every item of set_1
for x in set_1:
    print(x)
print("---------------------------------------------")

# Check if a key exist
if "Daihatsu" in set_1:
    print("Yes, Daihatsu is an item in set_1.")

# Add an item
set_1.add("Mitsubishi")
print(set_1)

# Add multiple items
set_1.update(["Suzuki","Mazda","Nissan"])
print(set_1)

# Part 2
# Remove an item (method 1)
set_1.remove("Honda")
print(set_1)

# Remove an item (method 2)
set_1.discard("Mazda")
print(set_1)

# Delete (pop) last inserted key
set_1.pop()
print(set_1)

# Clear the set
set_1.clear()
print(set_1)

# Delete the set
del set_1
print("---------------------------------------------")

# Union of two sets
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}
set_3 = set_1.union(set_2)
print(set_3)
print("---------------------------------------------")

# set_1 takes copies of all items of set 2
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}
set_1.update(set_2)
print(set_1)