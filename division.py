def main():
    a = eval(input("Enter first num: "))
    b = eval(input("Enter second num: "))
    print(divide(a, b))


def divide(a,b):
    try:    
        if b != 0:
            return a / b
    except ZeroDivisionError:
        print('Cannot Divide by Zero')

if __name__ == '__main__':
    main()