import pickle
def write_record():#Writes Fresh data and erases all previous data
    file_handler=open("binarytesting.dat","wb")
    flag="y"
    while flag=="y": #Let's you enter data till flag is y(asks the user to input flag later on)
        transaction_id=int(input("Enter the Transaction ID: "))
        if transaction_id<0:
            print("Invalid Transaction ID!!!")
            continue
        #-----------
        Date=int(input("Enter the date: ")) #Input date like XXXXXXXX and it will be split automatically
        Date_str=str(Date) #Strictly takes 8 digit dates only
        if len(Date_str)==7:
            Date_str="0"+Date_str
        if len(Date_str)>8 or len(Date_str)<8:
            print("Date is invalid!!")
            continue
        Date=int(Date_str)
        sub_month=Date//10000
        year=Date%10000
        days=sub_month//100
        month=sub_month%100
        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
        if (year%400==0) or (year%4==0 and year%100!=0):
            date_dict[2]=29
        if month not in date_dict:
            print("Wrong Month!!!")
            continue
        if days>date_dict[month]or days<1:
            print("Wrong Date!!!")
            continue
        if year<2026 or year>2027:
            print("Invalid Year!!!")
            continue
        Date = f"{days:02d}-{month:02d}-{year}"
        #-----------
        transaction_type=input("Enter the transaction type: ") #Input income or expense as Transaction Type
        if transaction_type=="Income"or transaction_type=="income":
            transaction_type="Income"
        elif transaction_type=="Expense"or transaction_type=="expense":
            transaction_type="Expense"
        else:
            print("Wrong Transaction type!!")
            continue #Let's you enter the data again all over from transaction id
        #-----------
        amount=int(input("Enter an amount: "))
        if amount<0:
            print("Invalid Amount!!!")
            continue
        #-----------
        category=input("Enter the category of Income or expense: ")
        rec=[transaction_id,Date,transaction_type,amount,category]
        pickle.dump(rec,file_handler)
        flag=input("Enter y to continue writing data: ")
        if flag=="y":
            pass
    file_handler.close()
    print("------DATA HAS BEEN SUCCESSFULLY WRITTEN------")
def read_record():#Reads the data present in the file
    file_handler=open("binarytesting.dat","rb")
    flag=False
    record=[]
    try:
        while True:
            rec=pickle.load(file_handler)
            record.append(rec)
            flag=True
    except EOFError:
        pass
    file_handler.close()
    if record!=[]:#Different ways to read data
        print("---How do you want to read data---")
        print("1-->Original Configuration")# Shows how user entered ther data without sorting
        print("2-->Arranged via ID")
        print("3-->Arranged via Date")
        print("4-->Arranged via Amount")
        print("5-->Arranged via Category")
        ch=int(input("Enter your choice: "))
        found=True
        if ch==1:
            pass
        elif ch==2: # Utilises lambda sorting 
            record.sort(key=lambda x:x[0])
        elif ch==3:
            record.sort(key=lambda x:(int(x[1][6:10]),int(x[1][3:5]),int(x[1][0:2])))
        elif ch==4:
            record.sort(key=lambda x:x[3])
        elif ch==5:
            record.sort(key=lambda x:x[4])
        else:
            print("Invalid Arrangement commanded !!!")
            found=False
        if found:
            for i in record:
                print(i)
    else:
        print("NO RECORD FOUND!!!")
def add_record():#Add new data to already existing data
    file_handler=open("binarytesting.dat","ab")
    flag="y"
    while flag=="y": #Let's you enter data till flag is y(asks the user to input flag later on)
        check=open("binarytesting.dat","rb")
        found=False
        transaction_id=int(input("Enter the Transaction ID: ")) #Doesn't allow duplicates IDS to exist
        if transaction_id<0:
            print("Invalid Transaction ID!!!")
            check.close()
            continue
        try:
            while True:
                rec=pickle.load(check)
                if rec[0]==transaction_id:
                    found=True
                    break
        except EOFError:
            pass
        check.close()
        if found:
            print("Transaction ID already exists")
            continue #Let's you enter a different transaction id again
        #-----------
        Date=int(input("Enter the date: ")) #Input date like XXXXXXXX
        Date_str=str(Date)
        if len(Date_str)==7:
            Date_str="0"+Date_str
        if len(Date_str)>8 or len(Date_str)<8:
            print("Date is invalid!!")
            continue
        Date=int(Date_str)
        sub_month=Date//10000
        year=Date%10000
        days=sub_month//100
        month=sub_month%100
        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
        if (year%400==0) or (year%4==0 and year%100!=0):
            date_dict[2]=29
        if month not in date_dict:
            print("Wrong Month!!!")
            continue
        if days>date_dict[month]or days<1:
            print("Wrong Date")
            continue
        if year<2026 or year>2027:
            print("Invalid Year!!!")
            continue
        Date = f"{days:02d}-{month:02d}-{year}"
        #-----------
        transaction_type=input("Enter the transaction type: ") #Only two types of transaction type:-income or expense
        if transaction_type=="Income"or transaction_type=="income":
            transaction_type="Income"
        elif transaction_type=="Expense"or transaction_type=="expense":
            transaction_type="Expense"
        else:
            print("Wrong Transaction type!!")
            continue
        #-----------
        amount=int(input("Enter an amount: "))
        if amount<0:
            print("Invalid Amount!!!")
            continue
        #-----------
        category=input("Enter the category of Income or expense: ") #Category could be anything-Food,education,Salary,Stocks,etc
        rec=[transaction_id,Date,transaction_type,amount,category]
        pickle.dump(rec,file_handler)
        flag=input("Enter y to continue writing data: ")
        if flag=="y":
            pass
    file_handler.close()
    print("------DATA HAS BEEN SUCCESSFULLY ADDED------")
def clear_record():  #If there are too many records just use this
    file_handler=open("binarytesting.dat","wb")
    file_handler.close()
    print("------YOUR FILE IS NOW EMPTY------")
def delete_record():
    file_handler=open("binarytesting.dat","rb")
    temp=open("temp.dat","wb")
    transaction_id=int(input("Enter Transaction ID of the record you want to delete: ")) #Checks transaction ID to delete  record
    Flag=False
    try:
        while True:
            rec=pickle.load(file_handler)
            if transaction_id!=rec[0]:
                pickle.dump(rec,temp)
            else:
                Flag=True
    except EOFError:
        pass
    file_handler.close()
    temp.close()
    #-------------------------------
    file_handler=open("binarytesting.dat","wb")
    temp=open("temp.dat","rb")
    try:
        while True:
            rec=pickle.load(temp)
            pickle.dump(rec,file_handler)
    except EOFError:
        pass
    file_handler.close()
    temp.close()
    if Flag:
        print("------DATA HAS BEEN SUCCESSFULLY DELETED------")
    else:
        print("------TRANSACTION ID NOT FOUND------")
def modify_record():
    file_handler=open("binarytesting.dat","rb")
    temp=open("temp.dat","wb")
    transaction_id=int(input("Enter Transaction ID to be modified: "))
    Flag=False
    try:
        while True:
            rec=pickle.load(file_handler)
            if transaction_id!=rec[0]:
                pickle.dump(rec,temp)
            else:
                Flag=True
                while True:  #Choose from a variety of options to modify
                    print("Choose:0 -->To modify Transaction ID")
                    print("Choose:1 -->To modify Date")
                    print("Choose:2 -->To modify Transaction Type")
                    print("Choose:3 -->To modify Amount")
                    print("Choose:4 -->To modify Category")
                    print("Choose:5 -->To modify Date and Transaction Type")
                    print("Choose:6 -->To modify Date and Amount")
                    print("Choose:7 -->To modify Date and category")
                    print("Choose:8 -->To modify Transaction type and Amount")
                    print("Choose:9 -->To modify Transaction type and category")
                    print("choose:10-->To modify Amount and category")
                    print("choose:11-->To modify Date,Transaction type,Amount and Category")
                    choice=int(input("Enter your choice from (0-11): "))
                    if 0<=choice<=11: #Works again if user inputs a wrong choice
                        break
                    else:
                        print("Invalid choice")
                if choice==1:
                    new_date=int(input("Enter new Date: "))
                    Date_str=str(new_date)
                    if len(Date_str)==7:
                        Date_str="0"+Date_str
                    if len(Date_str)!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    Date=int(Date_str)
                    sub_month=Date//10000
                    year=Date%10000
                    days=sub_month//100
                    month=sub_month%100
                    date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    if (year%400==0) or (year%4==0 and year%100!=0):
                        date_dict[2]=29
                    if month not in date_dict:
                        print("Wrong Month!!!")
                        pickle.dump(rec,temp)
                        continue
                    if days>date_dict[month]or days<1:
                        print("Wrong Date")
                        pickle.dump(rec,temp)
                        continue
                    if year<2026 or year>2027:
                        print("Invalid Year!!!")
                        pickle.dump(rec,temp)
                        continue
                    rec[1]=f"{days:02d}-{month:02d}-{year}"
                    pickle.dump(rec,temp)
                elif choice==2:
                    new_transaction_type=input("Enter new Transaction Type: ")
                    if new_transaction_type=="Income"or new_transaction_type=="income":
                        new_transaction_type="Income"
                    elif new_transaction_type=="Expense"or new_transaction_type=="expense":
                        new_transaction_type="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        pickle.dump(rec,temp)
                        continue
                    rec[2]=new_transaction_type
                    pickle.dump(rec,temp)
                elif choice==3:
                    new_amount=int(input("Enter new Amount: "))
                    if new_amount<0:
                        print("Invalid Amount!!!")
                        pickle.dump(rec,temp)
                        continue
                    rec[3]=new_amount
                    pickle.dump(rec,temp)
                elif choice==4:
                    new_category=input("Enter new Category: ")
                    rec[4]=new_category
                    pickle.dump(rec,temp)
                elif choice==5:
                    new_date=int(input("Enter new Date: "))
                    new_transaction_type=input("enter new Transaction Type: ")
                    Date_str=str(new_date)
                    if len(Date_str)==7:
                        Date_str="0"+Date_str
                    if len(Date_str)!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    Date=int(Date_str)
                    sub_month=Date//10000
                    year=Date%10000
                    days=sub_month//100
                    month=sub_month%100
                    date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    if (year%400==0) or (year%4==0 and year%100!=0):
                        date_dict[2]=29
                    if month not in date_dict:
                        print("Wrong Month!!!")
                        pickle.dump(rec,temp)
                        continue
                    if days>date_dict[month]or days<1:
                        print("Wrong Date")
                        pickle.dump(rec,temp)
                        continue
                    if year<2026 or year>2027:
                        print("Invalid Year!!!")
                        pickle.dump(rec,temp)
                        continue
                    if new_transaction_type=="Income"or new_transaction_type=="income":
                        new_transaction_type="Income"
                    elif new_transaction_type=="Expense"or new_transaction_type=="expense":
                        new_transaction_type="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        pickle.dump(rec,temp)
                        continue
                    rec[1]=f"{days:02d}-{month:02d}-{year}"
                    rec[2]=new_transaction_type
                    pickle.dump(rec,temp)
                elif choice==6:
                    new_date=int(input("Enter new Date: "))
                    Date_str=str(new_date)
                    if len(Date_str)==7:
                        Date_str="0"+Date_str
                    if len(Date_str)!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    Date=int(Date_str)
                    sub_month=Date//10000
                    year=Date%10000
                    days=sub_month//100
                    month=sub_month%100
                    date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    if (year%400==0) or (year%4==0 and year%100!=0):
                        date_dict[2]=29
                    if month not in date_dict:
                        print("Wrong Month!!!")
                        pickle.dump(rec,temp)
                        continue
                    if days>date_dict[month]or days<1:
                        print("Wrong Date")
                        pickle.dump(rec,temp)
                        continue
                    if year<2026 or year>2027:
                        print("Invalid Year!!!")
                        pickle.dump(rec,temp)
                        continue
                    new_amount=int(input("Enter new Amount: "))
                    if new_amount<0:
                        print("Invalid Amount!!!")
                        pickle.dump(rec,temp)
                        continue
                    rec[1]=f"{days:02d}-{month:02d}-{year}"
                    rec[3]=new_amount
                    pickle.dump(rec,temp)
                elif choice==7:
                    new_date=int(input("Enter new Date: "))
                    Date_str=str(new_date)
                    if len(Date_str)==7:
                        Date_str="0"+Date_str
                    if len(Date_str)!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    Date=int(Date_str)
                    sub_month=Date//10000
                    year=Date%10000
                    days=sub_month//100
                    month=sub_month%100
                    date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    if (year%400==0) or (year%4==0 and year%100!=0):
                        date_dict[2]=29
                    if month not in date_dict:
                        print("Wrong Month!!!")
                        pickle.dump(rec,temp)
                        continue
                    if days>date_dict[month]or days<1:
                        print("Wrong Date")
                        pickle.dump(rec,temp)
                        continue
                    if year<2026 or year>2027:
                        print("Invalid Year!!!")
                        pickle.dump(rec,temp)
                        continue
                    new_category=input("Enter new Category: ")
                    rec[1]=f"{days:02d}-{month:02d}-{year}"
                    rec[4]=new_category
                    pickle.dump(rec,temp)
                elif choice==8:
                    new_transaction_type=input("Enter new Transaction Type: ")
                    if new_transaction_type=="Income"or new_transaction_type=="income":
                        new_transaction_type="Income"
                    elif new_transaction_type=="Expense"or new_transaction_type=="expense":
                        new_transaction_type="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        pickle.dump(rec,temp)
                        continue
                    new_amount=int(input("Enter new Amount: "))
                    if new_amount<0:
                        print("Invalid Amount!!!")
                        pickle.dump(rec,temp)
                        continue
                    rec[2]=new_transaction_type
                    rec[3]=new_amount
                    pickle.dump(rec,temp)
                elif choice==9:
                    new_transaction_type=input("Enter new Transaction Type: ")
                    if new_transaction_type=="Income"or new_transaction_type=="income":
                        new_transaction_type="Income"
                    elif new_transaction_type=="Expense"or new_transaction_type=="expense":
                        new_transaction_type="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        pickle.dump(rec,temp)
                        continue
                    new_category=input("Enter new Category: ")
                    rec[2]=new_transaction_type
                    rec[4]=new_category
                    pickle.dump(rec,temp)
                elif choice==10:
                    new_amount=int(input("Enter new Amount: "))
                    if new_amount<0:
                        print("Invalid Amount!!!")
                        pickle.dump(rec,temp)
                        continue
                    new_category=input("Enter new Category: ")
                    rec[3]=new_amount
                    rec[4]=new_category
                    pickle.dump(rec,temp)
                elif choice==11:
                    new_date=int(input("Enter new Date: "))
                    Date_str=str(new_date)
                    if len(Date_str)==7:
                        Date_str="0"+Date_str
                    if len(Date_str)!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    Date=int(Date_str)
                    sub_month=Date//10000
                    year=Date%10000
                    days=sub_month//100
                    month=sub_month%100
                    date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    if (year%400==0) or (year%4==0 and year%100!=0):
                        date_dict[2]=29
                    if month not in date_dict:
                        print("Wrong Month!!!")
                        pickle.dump(rec,temp)
                        continue
                    if days>date_dict[month]or days<1:
                        print("Wrong Date")
                        pickle.dump(rec,temp)
                        continue
                    if year<2026 or year>2027:
                        print("Invalid Year!!!")
                        pickle.dump(rec,temp)
                        continue
                    new_transaction_type=input("Enter new Transaction Type: ")
                    if new_transaction_type=="Income"or new_transaction_type=="income":
                        new_transaction_type="Income"
                    elif new_transaction_type=="Expense"or new_transaction_type=="expense":
                        new_transaction_type="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        pickle.dump(rec,temp)
                        continue
                    new_amount=int(input("Enter new Amount: "))
                    if new_amount<0:
                        print("Invalid Amount!!!")
                        pickle.dump(rec,temp)
                        continue
                    new_category=input("Enter new Category: ")
                    rec[1]=f"{days:02d}-{month:02d}-{year}"
                    rec[2]=new_transaction_type
                    rec[3]=new_amount
                    rec[4]=new_category
                    pickle.dump(rec,temp)
                elif choice==0:
                    while True: #Let's you enter data till flag is y(asks the user to input flag later on)
                        check=open("binarytesting.dat","rb")
                        found=False
                        new_transaction_id=int(input("Enter the Transaction ID: ")) #Doesn't allow duplicates IDS to exist
                        if new_transaction_id<0:
                            print("Invalid Transaction ID!!!")
                            check.close()
                            continue
                        try:
                            while True:
                                check_rec=pickle.load(check)
                                if check_rec[0]==new_transaction_id and check_rec[0]!=rec[0]:
                                    found=True
                                    break
                        except EOFError:
                            pass
                        check.close()
                        if found:
                            print("Transaction ID already exists")
                        else:
                            rec[0]=new_transaction_id
                            break #Let's you enter a different transaction id
                    pickle.dump(rec,temp)
    except EOFError:
        pass
    file_handler.close()
    temp.close()
    #----------------------------------------
    file_handler=open("binarytesting.dat","wb")
    Temp=open("temp.dat","rb")
    try:
        while True:
            rec=pickle.load(Temp)
            pickle.dump(rec,file_handler)
    except EOFError:
        pass
    file_handler.close()
    Temp.close()
    if Flag:
        print("------DATA HAS BEEN SUCCESSFULLY MODIFIED------")
    else:
        print("------TRANSACTION ID NOT FOUND------")
def Search_Record(): # Searches via Transaction ID
    file_handler=open("binarytesting.dat","rb")
    transaction_id=int(input("Enter Transaction ID which you want to search: "))
    flag=False
    try:
        while True:
            rec=pickle.load(file_handler)
            if transaction_id==rec[0]:
                print(rec)
                flag=True
                break
    except EOFError:
        pass
    if not flag:
        print("------RECORD NOT FOUND------")
    file_handler.close()
def Current_Balance(): # Calculates the amount of money you currently have
    file_handler=open("binarytesting.dat","rb")
    income_balance=0
    expense_balance=0
    try:
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Income"or rec[2]=="income":
                income_balance+=rec[3]
            elif rec[2]=="Expense"or rec[2]=="expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    file_handler.close()
    balance=income_balance-expense_balance
    print("You earned:", income_balance)
    print("--------------------------")
    print("You spent:", expense_balance)
    print("--------------------------")
    if balance>0:
        print("Congrats you're doing well!!!")
        print("Your Current Balance is:", "₹",balance)
        print("--------------------------")
    elif balance==0:
        print("Congrats!!! you're...broke😂🫵","₹",balance)
        print("--------------------------")
    else:
        print("Too bad you're broke AND in debt of:","₹",abs(balance))#Just in case if your expense>income
        print("--------------------------")
def Income_Analysis():#Calculates how much you earned
    file_handler=open("binarytesting.dat","rb")
    Income_analysis={}
    try :
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Income":
                if rec[4] in Income_analysis:
                    Income_analysis[rec[4]]+=rec[3]
                else:
                    Income_analysis[rec[4]]=rec[3]
    except EOFError:
        pass
    file_handler.close()
    for i in Income_analysis:
        print(i,":","₹",Income_analysis[i])
        print("------------")
    file_handler=open("binarytesting.dat","rb")
    income_balance=0
    try:
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Income":
                income_balance+=rec[3]
    except EOFError:
        pass
    print("Your Total Income comes out to be:","₹", income_balance)
    print("--------------------------------------------")
    file_handler.close()
def Expense_Analysis():#Calculates how much you spent
    file_handler=open("binarytesting.dat","rb")
    expense_analysis={}
    try :
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Expense":
                if rec[4] in expense_analysis:
                    expense_analysis[rec[4]]+=rec[3]
                else:
                    expense_analysis[rec[4]]=rec[3]
    except EOFError:
        pass
    file_handler.close()
    for i in expense_analysis:
        print(i,":","₹",expense_analysis[i])
        print("------------")
    file_handler=open("binarytesting.dat","rb")
    expense_balance=0
    try:
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    print("Your Total Expense comes out to be:","₹", expense_balance)
    print("--------------------------------------------")
    file_handler.close()
def Monthly_Report():#Lets you see all the transactions made in a specific month
    file_handler=open("binarytesting.dat","rb")
    flag=False
    month=int(input("Enter the Month: "))
    if month<1 or month>12:
        print("Invalid Month!!!")
        return
    try:
        while True:
            rec=pickle.load(file_handler)
            if int(rec[1][3:5])==month:
                print("The Monthly report is:",rec)
                flag=True
    except EOFError:
        if not flag:
            print("Report Not Found!!!")
    file_handler.close()
def Saving_Goal_Tracker():# Asks for your financial goals and tell you how far you are from it
    file_handler=open("binarytesting.dat","rb")
    savings_goal=int(input("Enter your Saving Goals: "))
    income_balance=0
    expense_balance=0
    try:
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Income"or rec[2]=="income":
                income_balance+=rec[3]
            elif rec[2]=="Expense"or rec[2]=="expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    file_handler.close()
    balance=income_balance-expense_balance
    remaining=savings_goal-balance
    if remaining<0:
        print("Congrats!! You've already surpassed your goals by:","₹",abs(remaining))
    elif remaining==0:
        print("Congrats!! You've already reached your goals")
    else:
        print("-----------------------------")
        print("Your Saving Goals are:","₹",savings_goal)
        print("-----------------------------")
        print("Your Current Balance is :","₹",balance)
        print("-----------------------------")
        print("Remaining:","₹",remaining)
        print("-----------------------------")
def Highest_Income(): #Displays your highest Income
    file_handler=open("binarytesting.dat","rb")
    highest=0
    highest_category=None
    try:
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Income"or rec[2]=="income":
                if rec[3]>highest:
                    highest=rec[3]
                    highest_category=rec[4]
    except EOFError:
        pass
    file_handler.close()
    if highest_category==None:
        print("No record found")
    else:
        print("Your Highest Income is",highest_category,":","₹",highest)
def Highest_Expense(): #Displays your highest expense
    file_handler=open("binarytesting.dat","rb")
    highest=0
    highest_category=None
    try:
        while True:
            rec=pickle.load(file_handler)
            if rec[2]=="Expense"or rec[2]=="expense":
                if rec[3]>highest:
                    highest=rec[3]
                    highest_category=rec[4]
    except EOFError:
        pass
    file_handler.close()
    if highest_category==None:
        print("No record found")
    else:
        print("Your Highest expense is",highest_category,":","₹",highest)
def Tax_Calculator(): # Calculates how much tax you have to pay according to your income
    file_handler=open("binarytesting.dat","rb")
    income_balance=0 
    expense_balance=0
    c=0
    record=[]
    try:
        while True:
            rec=pickle.load(file_handler)
            record.append(rec)
            if rec[2]=="Income"or rec[2]=="income":
                income_balance+=rec[3]
                c+=1
            elif rec[2]=="Expense"or rec[2]=="expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    file_handler.close()
    if not record:
        print("No records found.")
        return
    balance=income_balance-expense_balance
    if balance>0:
        print("Congrats you're doing well!!!")
        print("Your Current Balance is: ","₹ ",balance)
    elif balance==0:
        print("Congrats!!! you're...broke😂🫵","₹",balance)
    else:
        print("Too bad you're broke AND in debt of:","₹",abs(balance))
    #------------------------------------------
    # TAX CALCULATION
    #------------------------------------------
    tax=0
    if income_balance<=400000:
        tax=0
    elif income_balance<=800000:
        tax=(income_balance-400000)*0.05
    elif income_balance<=1200000:
        tax=20000+(income_balance-800000)*0.10
    elif income_balance<=1600000:
        tax=60000+(income_balance-1200000)*0.15
    elif income_balance<=2000000:
        tax=120000+(income_balance-1600000)*0.20
    elif income_balance<=2400000:
        tax=200000+(income_balance-2000000)*0.25
    else:
        tax=300000+(income_balance-2400000)*0.30
    # Section 87A rebate
    if income_balance<=1200000:
        tax=0
    print("-------------------------------------")
    print("Your Total Income is: ","₹ ",income_balance)
    print("-------------------------------------")
    print("Your Calculated Tax is: ","₹ ",tax)
    print("-------------------------------------")
    final_balance=balance-tax #Your tax affects your balance
    print("Your Balance after Tax is: ","₹ ",final_balance)
    print("--------------------------------------")
    choice=input("Do you want to pay tax: ")
    if choice.title()=="Yes":
        # Check whether tax has already been paid
        already_paid=False
        check=open("binarytesting.dat","rb")
        try:
            while True:
                rec=pickle.load(check)
                if rec[2]=="Expense" and rec[4].lower()=="tax":
                    already_paid=True
        except EOFError:
            pass
        check.close()
        if already_paid:
            print("Tax has already been paid.")
            print("You cannot pay the same tax again.")
        elif tax==0:
            print("Your calculated tax is ₹0.")
            print("No tax payment is required.")
        else:
            # Find the highest Transaction ID
            highest_id=0
            check=open("binarytesting.dat","rb")
            try:
                while True:
                    rec=pickle.load(check)
                    if rec[0]>highest_id:
                        highest_id=rec[0]
            except EOFError:
                pass
            check.close()
            new_transaction_id=highest_id+1
            date=record[-1][1]#Puts the date of the last transaction in the records
            # Add tax as a separate expense transaction
            file_handler=open("binarytesting.dat","ab")
            tax_record=[new_transaction_id,date,"Expense",tax, "Tax" ]
            pickle.dump(tax_record,file_handler)
            file_handler.close()
            print("----------TAX HAS BEEN PAID----------")
            print("Tax Amount: ","₹",tax)
            print("Transaction ID: ",new_transaction_id)
            print("-------------------------------------")
while True:
    print("===== PERSONAL FINANCE MANAGER =====")
    print("1 --> Write Transaction in file")
    print("2 --> Read Transaction in file")
    print("3 --> Add Transaction in file")
    print("4 --> Clear all Transactions in file")
    print("5 --> Modify Transaction in file")
    print("6 --> Delete Transaction in file")
    print("7 --> Search Transaction in file")
    print("8 --> Current Balance")
    print("9 --> Income Analysis")
    print("10--> Expense Analysis")
    print("11--> Monthly Report")
    print("12--> Savings Goal Tracker")
    print("13--> Highest Income")
    print("14--> Highest Expense")
    print("15--> Tax Calculator")
    print("0 --> Exit")
    choice=int(input("Enter your choice from (0-15): "))
    if choice==1:
        write_record()
    elif choice==2:
        read_record()
    elif choice==3:
        add_record()
    elif choice==4:
        clear_record()
    elif choice==5:
        modify_record()
    elif choice==6:
        delete_record()
    elif choice==7:
        Search_Record()
    elif choice==8:
        Current_Balance()
    elif choice==9:
        Income_Analysis()
    elif choice==10:
        Expense_Analysis()
    elif choice==11:
        Monthly_Report()
    elif choice==12:
        Saving_Goal_Tracker()
    elif choice==13:
        Highest_Income()
    elif choice==14:
        Highest_Expense()
    elif choice==15:
        Tax_Calculator()
    elif choice==0:
        print("----Program has been terminated----")
        break
    else:
        print("Invalid choice!!!")
