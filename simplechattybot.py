def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.\n')


def remind_name():
    print('Please, remind me your name.')
    name = input('Name: ')
    print('\nWhat a great name you have, ' + name + '!')
    print()


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input('\nYour remainder of your age by 3: '))
    rem5 = int(input('Your remainder of your age by 3: '))
    rem7 = int(input('Your remainder of your age by 3: '))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print('\nCalculating.........')
    print('Just one more moment........')
    print('Not long now...')
    print("Did I tell you that I'm a super computer with ifinite cores?")
    print('... Ah, finally got it!\n')
    print("Your age is " + str(age) + "; that's a good time to start programming!\n")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input('\nPlease enter your number in digits: '))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("\nLet's test your programming knowledge.")
    print('Why do we use methods?\n')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')

    ans = int(input('\nPlease make your selection: '))

    while True:
        if ans != 2:
            print('Sorry. ' + str(ans) + ' is incorrect. Please try again: ')
            ans = int(input())
        else:
            print('\n' + str(ans) + ' is correct! Here, have a cookie :)')
            break


def end():
    print("\nIt has been nice chatting with you. I'm going to shut down now. Goodbye!")
    exit()


greet('Hal', '2001')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
