account_dic = { 
            "Joe": 100,
            "Dan": 1000
          }

attempt_counter = 0
while True:
    user_input = input("Enter action: create_user / deposit / withdraw / total_balance / user_balance / delete_user / quit: ").strip()

    if user_input == "create_user":
        name = input("Enter Account Holder Name: ")
        if name in account_dic.keys():                              #No duplicate accounts
            print (f"{name} already has an account")
        else:
            account_dic[name] = 0
    
    elif user_input == "deposit":
        name = input("Enter Account Holder Name: ")
        if name not in account_dic:                                 #Can't deposit if account doesnt exist
            print("No account with that name!!")
        else:
            try:
                amount = int(input("Enter amount to deposit: "))
                account_dic[name] += amount
            except Exception as e:                                  #Exception for dumb users not typing an integer
                print(e)
            
    elif user_input == "withdraw":
        name = input("Enter Account Holder Name: ")
        amount = int(input("Enter amount to withdraw: "))
        if name not in account_dic:                                 # Can't withdraw if account doesnt exist
            print("No account with that name!!")
        else:
            if amount > account_dic[name]:
                print("Insufficient funds!!")
            else:
                try:
                    account_dic[name] -= amount
                except Exception as e:                              #Exception for dumb users not typing an integer again
                    print(e)
    
    elif user_input == "total_balance":                                   #Shows all accounts (easier to check issues)
        print(account_dic)

    elif user_input == "user_balance":
        name = input("Enter Account Holder Name: ")
        if name not in account_dic.keys():
            print("No account with that name!!")
        else:
            print(f"{name} has ${account_dic[name]}")
    
    elif user_input == "delete_user":
        name = input ("Enter Account Holder Name to close account: ")
        account_dic.pop(name, None)
        
    elif user_input == "quit":
        break

    else:
        print("Invalid command... please try again")
        attempt_counter += 1
        if attempt_counter >= 5:
            print("Max attempts reached... please try again later...")
            break


