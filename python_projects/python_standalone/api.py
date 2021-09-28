# class FizzBuzz(object):

#     def _init_():

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num) + " is divisible by both 3 and 5")
        print("Fizzbuzz")
        continue
    elif num % 3 == 0:
        print(str(num) + " is divisible by 3")
        print("Fizz")

    elif num % 5 == 0:
        print(str(num) + " is divisible by 5")
        print("buzz")

    print(num)


# fizzbuzz = FizzBuzz()

    # another way
    # for i in range(1,101):
    # fizz = 'Fizz' if i%3==0 else ''
    # buzz = 'Buzz' if i%5==0 else ''
    # print(f'{fizz}{buzz}' or i)

            