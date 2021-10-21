# --------------------------- WiFi Billings ---------------------------
"""
This program keeps the record of wifi billings
"""
import datetime

print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::: WiFi Billings :::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("----------------------------------------------------")
print("  Enter exit on both username and password to exit")
print("----------------------------------------------------")

while True:
    username = input("Enter Username : ")
    password = input("Enter Password : ")

    # noinspection PyBroadException
    try:
        if username.lower().__eq__("admin") and password.lower().__eq__("ashubiku11"):
            while True:
                print("\n")
                print("__________________________________________")
                print("____________ Welcome To Admin ____________")
                print("__________________________________________")

                # noinspection PyBroadException
                try:
                    print("1. Write")
                    print("2. Retrieve")
                    print("3. Exit")

                    print("__________________")
                    selection = input("Enter your choice : ")

                    if int(selection) == 1 or selection.lower().__eq__("Write"):
                        print("____________________________________")
                        print("_________ Fill The Details _________")
                        print("____________________________________")
                        client_name = input("Enter Client Name : ")
                        internet_package = input("Package (Mbps) : ")
                        amount = input("Amount (NPR) : ")
                        with open("wifi-billings", "a") as fl:
                            fl.write(
                                f'Client Name : {client_name}\nInternet Package : {internet_package}Mbps'
                                f'\nAmount : Rs. {amount}\nDate & Time : {datetime.datetime.now()}\n')
                            print("_______________________")
                            print("Successfully written !!")
                            print("-----------------------")
                            continue
                    elif int(selection) == 2 or selection.lower().__eq__("Retrieve"):
                        print("______________________________________________________")
                        print("___________________ Retrieved Data ___________________")
                        print("______________________________________________________")
                        with open("wifi-billings") as fl:
                            for line in fl:
                                print(line, end=" ")
                                continue
                    elif int(selection) == 3 or selection.lower().__eq__("Exit"):
                        print("_____________________")
                        print("Successfully Exited..")
                        print("---------------------")
                        break
                    else:
                        print("_______________________________")
                        print("Please provide a valid input !!")
                        print("-------------------------------")
                except Exception as e:
                    print("__________________________________")
                    print("Invalid input, Please try again !!")
                    print("----------------------------------")
        elif username.__eq__("exit") and password.__eq__("exit"):
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("Thank you for using Wifi Billings - Have a good time (from @ Author Bikal Dhimal)")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            break
        else:
            print("___________________________________________________")
            print("Incorrect username or password, Please try again !!")
            print("---------------------------------------------------")
    except Exception as e:
        print("_______________________________")
        print("Invalid username or password !!")
        print("-------------------------------")
