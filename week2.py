#enter your name
#enter your age
#what is your favorite number
#display age - minor, adult, senior
#display favorite number - positive, zero, negative
#if fav number is even "Winner!"
#if fav number odd "didnt win contest message"

name = input('What is your name?: ')
age = int(input('How old are you?: '))
fav_number = int(input('What is your favorite number?: '))

#display name
print("Hello", name)

#display age category
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

#display fav number pos, neg, zero
if fav_number == 0:
    print('Your favorite number is zero!')
elif fav_number > 0:
    print('Your favorite number is positive!')
else:
    print('Yor favorite number is odd!')

#display fav number even/odd
if fav_number % 2 == 0:
    print("Your favorite number is even!")
else:
    print("Your favorite number is odd!")

#display even/odd extended messages
if fav_number in [100, 10, 1, 0, 1000]:
    print("YOU ARE THE WINNER!!!!")
else:
    print("*sorry you did not win the prize, please try again next time.")