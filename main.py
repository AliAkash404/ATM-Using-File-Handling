def register(i):
    global name
    global user
    if i == '1':
        print("Rigister Your Account!")
        name = input("Please input your name: ")
        username = input("Please input your desired account no: ")
        password = input("Please input your desired password: ")
        with open("account_file.txt", 'a') as file:
            file.write(username)
            file.write(" : ")
            file.write(password)
            file.write("\n")
        print("You have successfully registered your account")
        user = username + ".txt"
        new_user_file()


def log_in(i):
    global logged_in
    global user
    if i == '2':
        username = input("Please Enter Your Account number: ")
        password = input("Please Enter Your Password: ")
        with open("account_file.txt") as file:
            lines = file.readlines()
            for line in lines:
                log_in_info = line.rstrip()
                log_in_info = log_in_info.split(" : ")
                if username == log_in_info[0] and password == log_in_info[1]:
                    logged_in = True
                    user = log_in_info[0] + ".txt"
                    print("You are logged in!")
                    print(f"Welcome {account_info(user)[0]}")
                    return True
                else:
                    continue
        print("Incorect Username or Password!!! Please try again")


def new_user_file():
    with open(user, 'w') as file:
        file.write("Name")
        file.write(" : ")
        file.write(name)
        file.write('\n')
        file.write("Balance")
        file.write(" : ")
        file.write("0 Rs")
        file.write("\n")


def account_info(user):
    with open(user) as file:
        lines = file.readlines()
        for line in lines:
            info = line.rstrip()
            info = info.split(" : ")
            if info[0] == "Name":
                Name = info[1]
            if info[0] == "Balance":
                Balance = info[1]
        return (Name, Balance)


def deposit_funds(i):
    if i == '2':
        deposit_Rs = input("Enter Amount To Deposit in Your Account: ")
        with open(user, 'r+') as file:
            Name = account_info(user)[0]
            allready_exist_Rs = account_info(user)[1].split(" ")
            total_Rs = int(allready_exist_Rs[0]) + int(deposit_Rs)
            file.write("Name")
            file.write(" : ")
            file.write(Name)
            file.write('\n')
            file.write("Balance")
            file.write(" : ")
            file.write(str(total_Rs) + " Rs")
            file.write("\n")
        print("Funds Deposit Successful...Your New Balance is ", total_Rs, " Rs")


def withdraw_funds(i):
    if i == '3':
        withdraw_Rs = input("Enter Funds To Withdraw: ")
        if int(withdraw_Rs) >= 500:
            with open(user, 'r+') as file:
                Name = account_info(user)[0]
                allready_exist_Rs = account_info(user)[1].split(" ")
                total_Rs = int(allready_exist_Rs[0]) - int(withdraw_Rs)
                if int(allready_exist_Rs[0]) >= int(withdraw_Rs):
                    file.write("Name")
                    file.write(" : ")
                    file.write(Name)
                    file.write('\n')
                    file.write("Balance")
                    file.write(" : ")
                    file.write(str(total_Rs) + " Rs")
                    file.write("\n")
                    print("Funds Withdraw Successful...Your New Balance is ",
                          total_Rs, " Rs")
                    print("Session End!!!")
                    return True
                else:
                    print("Insuficient Balance!!! Please Try Again!")
                    return False
        else:
            print("The Minimum Amount To Withdraw Is 500 Rs. Please Try Again!")
            return False


def fast_cash(i):
    if i == '5':
        print("Press 1 To Withdraw 1000 Rs")
        print("Press 2 To Withdraw 2000 Rs")
        print("Press 3 To Withdraw 3000 Rs")
        print("Press 4 To Withdraw 4000 Rs")
        print("Press 5 To Withdraw 5000 Rs")
        command = input("Enter Your Choice: ")
        if command == "1":
            amount_Rs = 1000
        if command == "2":
            amount_Rs = 2000
        if command == "3":
            amount_Rs = 3000
        if command == "4":
            amount_Rs = 4000
        if command == "5":
            amount_Rs = 5000
        with open(user, 'r+') as file:
            Name = account_info(user)[0]
            allready_exist_Rs = account_info(user)[1].split(" ")
            total_Rs = int(allready_exist_Rs[0]) - amount_Rs
            if int(allready_exist_Rs[0]) >= amount_Rs:
                file.write("Name")
                file.write(" : ")
                file.write(Name)
                file.write('\n')
                file.write("Balance")
                file.write(" : ")
                file.write(str(total_Rs) + " Rs")
                file.write("\n")
                print("Amount Withdraw Successful...Your New Balance is ",
                      total_Rs, " Rs")
                print("Session End!!!")
                return True
            else:
                print("Insuficient Balance!!! Please Try Again!")
                return False


def transfer_funds(i):
    if i == '4':
        to_user = input("Enter Account No: ")
        to_user += ".txt"
        transfer_Rs = int(input("Enter Amount To Transfer: "))
        if transfer_Rs >= 500:
            with open(user, 'r+') as file:
                Name = account_info(user)[0]
                allready_exist_Rs = account_info(user)[1].split(" ")
                total_Rs = int(allready_exist_Rs[0]) - int(transfer_Rs)
                if int(allready_exist_Rs[0]) >= int(transfer_Rs):
                    file.write("Name")
                    file.write(" : ")
                    file.write(Name)
                    file.write('\n')
                    file.write("Balance")
                    file.write(" : ")
                    file.write(str(total_Rs) + " Rs")
                    file.write("\n")
                    print("Funds Transfer Successful...Your New Balance is ",
                          total_Rs, " Rs")
                    print("Session End!!!")
                    with open(to_user, 'r+') as file:
                        to_Name = account_info(to_user)[0]
                        to_allready_exist_Rs = account_info(to_user)[
                            1].split(" ")
                        to_total_Rs = int(
                            to_allready_exist_Rs[0]) + int(transfer_Rs)
                        file.write("Name")
                        file.write(" : ")
                        file.write(to_Name)
                        file.write('\n')
                        file.write("Balance")
                        file.write(" : ")
                        file.write(str(to_total_Rs) + " Rs")
                        file.write("\n")
                    return True
                else:
                    print("Insuficient Balance!!! Please Try Again!")
                    return False
        else:
            print("The Minimum Amount To Transfer Is 500 Rs. Please Try Again!")


def balance_check(i):
    if i == '1':
        print(f"Your Balance Is: {account_info(user)[1]}")


def log_out(i):
    if i.lower() == '6' or i.lower() == "logout":
        print("You are logged out!")
        return True


def main_option(i):
    options = ('1', '2')
    for y in options:
        if i == y:
            return True
    print("Incorect Choice!!! Please Try Again!")


def dashborad_option(i):
    options = ('1', '2', '3', '4', '5', '6', 'logout')
    for y in options:
        if i == y:
            return True
    print("Incorect Choice!!! Please Try Again!")


print("Welcome To ATM!")
while True:
    print("Press 1 to register new account")
    print("Press 2 to login")
    command = input("Enter Your Choice: ")
    if main_option(command):
        register(command)
        if log_in(command):
            break
        else:
            continue

while logged_in:
    print("Press 1 To Check Your Balance")
    print("Press 2 To Deposit Funds")
    print("Press 3 To Withdraw Funds")
    print("Press 4 To Transfer Funds")
    print("Press 5 For Fast Cash")
    print("Press 6 To Log Out")
    command = input("Enter Your Choice: ")
    if dashborad_option(command):
        balance_check(command)
        deposit_funds(command)
        if withdraw_funds(command):
            break
        if transfer_funds(command):
            break
        if fast_cash(command):
            break
        if log_out(command):
            break
