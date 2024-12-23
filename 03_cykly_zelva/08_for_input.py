
total = 0
for i in range(10):
    number = int(input(f"Type {i+1}. number: "))
    total += number
if total > 1000:
    print("The sum of the numbers is more than 1000.")
else:
    print("The sum of the numbers is below 1000 or equal.")
