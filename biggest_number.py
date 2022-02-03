def main():
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_1 == 0 or num_2 == 0:
            exit(0)
    except ValueError:
        print("You entered something that isn't a number, please try again.")
        main()
    if num_2 > num_1:
        print(f"{num_2} is bigger")
        main()
    elif num_1 > num_2:
        print(f"{num_1} is bigger")
        main()
    else:
        print("Both are equal")
        main()


if __name__ == '__main__':
    main()
