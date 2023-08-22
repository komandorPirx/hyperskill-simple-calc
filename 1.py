import random
cool = 0 
operator_list = ['+', '*', '-']
operator = random.choice(operator_list)
arithmetic = {'*': lambda x, y: x * y,
              '+': lambda x, y: x + y,
              '-': lambda x, y: x - y}
while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level = int(input())
    if 1 < level > 2:
        print("Incorrect format.")
        desc = "simple operations with numbers 2-9"
    else:
        desc = "integral squares of 11-29"
        break

for i in range(0, 5): 

    if level == 1:
        a = random.randint(2,9)
        b = random.randint(2,9)
        print(a, operator, b)
        comp_ans = arithmetic[operator](a,b)
    elif level == 2:
        a = random.randint(11, 29) 
        print(a)
        comp_ans = arithmetic['*'](a,a)

    while True:
        user_ans = input()
        try:
            answer = int(user_ans)
            if answer == comp_ans:
                print("Right!")
                cool += 1
                break
            else:
                print("Wrong!")
                break
        except:
            print("Wrong format! Try again.")

print("Your mark is {0}/5. Would you like to save the result? Enter yes or no.".format(cool))
file_save = input()
if file_save.lower() == 'yes' or file_save.lower() == 'y' :
    print("What is your name?")
    ame = input()
    ile_results = open("results.txt", 'a+')
    ile_results.write("--{0}: {1}/5 in level {2} ({3}).\n".format(name, cool, level, desc))
    ile_results.close()
    rint('The results are saved in "results.txt".')
