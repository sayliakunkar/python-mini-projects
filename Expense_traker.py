expense = []
print("Welcome to Expense Tracker : plz dont wast your money")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = input("please enter your choise =")

    if(choice == '1'):
        date = input("enter the date when you spend money.: ")
        category = input("which type is this spend: ")
        discription = input("plz add some details about your cost: ")
        amount = float(input("enter total amount: "))

        Expenses = {
            "date": date,
            "category": category,
            "discription": discription,
            "amount": amount,
        }

        expense.append(Expenses)
        print("\n  Done bro.Expenses added sucessfully")

    elif(choice == '2'):
        if(len(expense) == 0):
            print("No Expenses added. joa pehle kharcha kro")
        else:
            print("=== ye y apka sara expenes ===")
            count = 1
            for eachkarcha in expense:
                print(f"{count} : {eachkarcha['date']}, {eachkarcha['category']}, {eachkarcha['discription']} ")
                count = count + 1

    elif(choice == '3'):
        total = 0
        for eachkarcha in expense:
            total = total + eachkarcha["amount"]
        print("\n Total kharcha =", total)

    elif(choice == '4'):
        print("Thank You so much for use our system ..")
        break
    else:
        print("invalid choice. try again")

    




    