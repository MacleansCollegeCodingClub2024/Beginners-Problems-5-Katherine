numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
print("The biggest numer is ",max(numsList))
print("The smallest number is ",min(numsList))
print("The average is ",sum(numsList)/len(numsList))


stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

def count_same_start_end(strings):
    count = 0
    for s in strings:
        if s[0].lower() == s[-1].lower():
            count += 1
    return count

print(" the number of strings that have the same character at the start and end is ",count_same_start_end(stringsList))


count = 0
foodList = []

for num in range (0,8):
    food = input("What's your favourite food?").lower()
    if food == "pesto":
        count += 1
else:
        foodList.append(food)
        
print(count, "people like pesto")
for num in range (0, count):
    print("I like pesto")

cerealList = []

while True:
    cereal = input("Enter Cereal: ")
    if cereal.lower() == 'sultana and bran' or cereal.lower() == 'weetbix':
        break
    else:
        cerealList.append(cereal)

print(cerealList)
