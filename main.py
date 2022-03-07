

x:int = 42  # this comment
y = 4.42
text = "Test"
text2 = "Another Test"
bool1 = False

z = str(x)
print(type(z))

result = 10

def sum_numbers(num1, num2):
    result = num1 + num2
    return result


sum_numbers(x,y)
print(result)

def check_number(number):
    if number < 10 and number > 2:
        return number

def loop_test(number):
    for i in range(number):
        if i != 3:
            print(i, end = " ")
        else:
            continue

loop_test(6)
print(" ")

