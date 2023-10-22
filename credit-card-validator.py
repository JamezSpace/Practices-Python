def valid_card_number():
    while True:
        card_number = input("Credit Card Number: ")

        if not card_number.isnumeric():
            print("Only digits should comprise your Credit Card Number")
            exit()
        
        if len(card_number) != 16:
            print("Credit Card Number should be 16 digits")
            continue
        else:
            return card_number

# Luhn formula
# reverse the number
card_number = valid_card_number()[::-1]

# multiply digits at even positions by 2
nums = []

for index, num in enumerate(card_number):
    if index % 2 == 0:
        nums.append(int(num))
    else:
        nums.append(int(num) * 2)

# subtract 9 from numbers higher than 9
func = lambda i: i if i < 10 else i - 9
nums = [func(i) for i in nums]

# remainder of the division of the sum of all numbers by 10 
# must be 0 to be valid
if sum(nums) % 10 == 0:
    print("VALID Credit Card Number")
else:
    print("INVALID Credit Card Number")
