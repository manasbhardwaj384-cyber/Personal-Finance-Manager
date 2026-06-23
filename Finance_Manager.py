import pickle
import random
def write_record():#Writes Fresh data
    myfile=open("binarytesting.dat","wb")
    flag="y"
    while flag=="y": #Let's you enter data till flag is y(asks the user to input flag later on)
        transaction_id=int(input("Enter the Transaction ID:"))
        #-----------
        Date=int(input("Enter the date:")) #Write data like-XXXXXXXX
        if len(str(Date))>8 or len(str(Date))<8:
            print("Date is invalid!!")
            continue #Let's you enter the data again all over from transaction id
        else:
            sub_month=Date//10000
            year=Date%10000
            days=sub_month//100
            month=sub_month%100
            date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
            if (year%400==0) or (year%4==0 and year%100!=0):
                date_dict[2]=29
            if month not in date_dict:
                print("Wrong Month!!!")
                continue #Let's you enter the data again all over from transaction id
            if days>date_dict[month]or days<1:
                print("Wrong Date")
                continue #Let's you enter the data again all over from transaction id
            date = f"{days:02d}-{month:02d}-{year}"
            #-----------
        transaction_type=input("Enter the transaction type") #Input income or expense as Type
        if transaction_type=="Income"or transaction_type=="income":
            transaction_type="Income"
        elif transaction_type=="Expense"or transaction_type=="expense":
            transaction_type="Expense"
        else:
            print("Wrong Transaction type!!")
            continue #Let's you enter the data again all over from transaction id
        #-----------
        amount=int(input("Enter an amount:"))
        #-----------
        category=input("Enter the category of Income or expense")
        rec=[transaction_id,date,transaction_type,amount,category]
        pickle.dump(rec,myfile)
        flag=input("Enter y to continue writing data:") 
        if flag=="y":
            pass
    myfile.close()
    print("------DATA HAS BEEN SUCCESSFULLY WRITTEN------")
def read_record():
    myfile=open("binarytesting.dat","rb")
    flag=False
    try:
        while True:
            a=pickle.load(myfile)
            flag=True
            print(a)
    except EOFError:
        pass
    if not Flag:
         print("NO RECORD FOUND!!!")
    myfile.close()
def add_record():#Add new data to already existing data
    myfile=open("binarytesting.dat","ab")
    flag="y"
    while flag=="y": #Let's you enter data till flag is y(asks the user to input flag later on)
        check=open("binarytesting.dat","rb")
        found=False
        transaction_id=int(input("Enter the Transaction ID:")) #Doesn't allow duplicates IDS to exist
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
            continue #Let's you enter a differnt transaction id again
        #-----------
        Date=int(input("Enter the date:")) #Input date like XXXXXXXX
        if len(str(Date))>8 or len(str(Date))<8:
            print("Date is invalid!!")
            continue
        else:
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
            date = f"{days:02d}-{month:02d}-{year}"
            #-----------
        transaction_type=input("Enter the transaction type") #Only two types income or expense
        if transaction_type=="Income"or transaction_type=="income":
            transaction_type="Income"
        elif transaction_type=="Expense"or transaction_type=="expense":
            transaction_type="Expense"
        else:
            print("Wrong Transaction type!!")
            continue
        #-----------
        amount=int(input("Enter an amount:"))
        #-----------
        category=input("Enter the category of Income or expense")
        rec=[transaction_id,date,transaction_type,amount,category]
        pickle.dump(rec,myfile)
        flag=input("Enter y to continue writing data:")
        if flag=="y":
            pass
    myfile.close()
    print("------DATA HAS BEEN SUCCESSFULLY ADDED------")
def clear_record():
    myfile=open("binarytesting.dat","wb")
    myfile.close()
    print("------YOUR FILE IS NOW EMPTY------") #If there are too many records just use this
def delete_record():
    stud=open("binarytesting.dat","rb")
    temp=open("temp.dat","wb")
    transaction_id=int(input("Enter which record do you want to delete:"))
    Flag=False
    try:
        while True:
            rec=pickle.load(stud)
            if transaction_id!=rec[0]:
                pickle.dump(rec,temp)
            else:
                Flag=True
    except EOFError:
        pass
    stud.close()
    temp.close()
    #-------------------------------
    stud=open("binarytesting.dat","wb")
    temp=open("temp.dat","rb")
    try:
        while True:
            rec=pickle.load(temp)
            pickle.dump(rec,stud)
    except EOFError:
        pass
    stud.close()
    temp.close()
    if Flag:
        print("------DATA HAS BEEN SUCCESSFULLY DELETED------")
    else:
        print("------TRANSACTION ID NOT FOUND------")
def modify_record():
    stud=open("binarytesting.dat","rb")
    temp=open("temp.dat","wb")
    transaction_id=int(input("Enter Transaction ID to be modified:"))
    Flag=False
    try:
        while True:
            rec=pickle.load(stud)
            if transaction_id!=rec[0]:
                pickle.dump(rec,temp)
            else:
                Flag=True
                while True:
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
                    choice=int(input("Enter your choice from (0-11)"))
                    if 0<=choice<=11: #Works again if user inputs a wrong choice
                        break
                    else:
                        print("Invalid choice")
                if choice==1:
                    rec[1]=int(input("Enter new Date:"))
                    if len(str(rec[1]))!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    else:
                        sub_month=rec[1]//10000
                        year=rec[1]%10000
                        days=sub_month//100
                        month=sub_month%100
                        month=sub_month%100
                        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
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
                        rec[1] = f"{days:02d}-{month:02d}-{year}"
                elif choice==2:
                    rec[2]=input("Enter new Transaction Type:")
                    if rec[2]=="Income"or rec[2]=="income":
                        rec[2]="Income"
                    elif rec[2]=="Expense"or rec[2]=="expense":
                        rec[2]="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        continue
                elif choice==3:
                    rec[3]=int(input("Enter new Amount:"))
                elif choice==4:
                    rec[4]=input("Enter new Category")
                elif choice==5:
                    rec[1]=int(input("Enter new Date:"))
                    rec[2]=input("enter new Transaction Type:")
                    if len(str(rec[1]))!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    else:
                        sub_month=rec[1]//10000
                        year=rec[1]%10000
                        days=sub_month//100
                        month=sub_month%100
                        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
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
                        rec[1] = f"{days:02d}-{month:02d}-{year}"
                    if rec[2]=="Income"or rec[2]=="income":
                        rec[2]="Income"
                    elif rec[2]=="Expense"or rec[2]=="expense":
                        rec[2]="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        continue
                elif choice==6:
                    rec[1]=int(input("Enter new Date:"))
                    rec[3]=int(input("enter new Amount:"))
                    if len(str(rec[1]))!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    else:
                        sub_month=rec[1]//10000
                        year=rec[1]%10000
                        days=sub_month//100
                        month=sub_month%100
                        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
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
                        rec[1] = f"{days:02d}-{month:02d}-{year}"
                elif choice==7:
                    rec[1]=int(input("Enter new Date:"))
                    rec[4]=input("enter new Category:")
                    if len(str(rec[1]))!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    else:
                        sub_month=rec[1]//10000
                        year=rec[1]%10000
                        days=sub_month//100
                        month=sub_month%100
                        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
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
                        rec[1] = f"{days:02d}-{month:02d}-{year}"
                elif choice==8:
                    rec[2]=input("Enter new Transaction type")
                    rec[3]=int(input("enter new Amount:"))
                    if rec[2]=="Income"or rec[2]=="income":
                        rec[2]="Income"
                    elif rec[2]=="Expense"or rec[2]=="expense":
                        rec[2]="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        continue
                elif choice==9:
                    rec[2]=input("Enter new Transaction type")
                    rec[4]=input("enter new Category:")
                    if rec[2]=="Income"or rec[2]=="income":
                        rec[2]="Income"
                    elif rec[2]=="Expense"or rec[2]=="expense":
                        rec[2]="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        continue
                elif choice==10:
                    rec[3]=int(input("enter new Amount:"))
                    rec[4]=input("enter new Category:")
                elif choice==11:
                    rec[1]=int(input("Enter new Date:"))
                    rec[2]=input("enter new Transaction Type:")
                    rec[3]=int(input("enter new Amount:"))
                    rec[4]=input("enter new Category:")
                    if len(str(rec[1]))!=8:
                        print("Invalid Date!!")
                        pickle.dump(rec,temp)
                        continue
                    else:
                        sub_month=rec[1]//10000
                        year=rec[1]%10000
                        days=sub_month//100
                        month=sub_month%100
                        date_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #Accounts for the most accurate dates
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
                        rec[1] = f"{days:02d}-{month:02d}-{year}"
                    if rec[2]=="Income"or rec[2]=="income":
                        rec[2]="Income"
                    elif rec[2]=="Expense"or rec[2]=="expense":
                        rec[2]="Expense"
                    else:
                        print("Wrong Transaction type!!")
                        continue
                elif choice==0:
                    rec[0]=int(input("Enter new Transaction ID:"))
                pickle.dump(rec,temp)
    except EOFError:
        pass
    stud.close()
    temp.close()
    Stud=open("binarytesting.dat","wb")
    Temp=open("temp.dat","rb")
    try:
        while True:
            Rec=pickle.load(Temp)
            pickle.dump(Rec,Stud)
    except EOFError:
        pass
    Stud.close()
    Temp.close()
    if Flag:
        print("------DATA HAS BEEN MODIFIED------")
    else:
        print("------TRANSACTION ID NOT FOUND------")
def Search_Record():
    stud=open("binarytesting.dat","rb")
    transaction_id=int(input("Enter Transaction ID which you want to search:"))
    flag=False
    try:
        while True:
            rec=pickle.load(stud)
            if transaction_id==rec[0]:
                print(rec)
                flag=True
                break
    except EOFError:
        pass
    if not flag:
        print("------RECORD NOT FOUND------")
    stud.close()
def Current_Balance():
    myfile=open("binarytesting.dat","rb")
    income_balance=0
    expense_balance=0
    try:
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Income"or rec[2]=="income":
                income_balance+=rec[3]
            elif rec[2]=="Expense"or rec[2]=="expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    myfile.close()
    balance=income_balance-expense_balance
    if balance>0:
        print("Congrats you're doing well!!!")
        print("Your Current Balance is:","$",balance)
    elif balance==0:
        print("Congrats!!! you're...broke😂🫵","$",balance)
    else:
        print("Too bad you're broke AND in debt of:","$",abs(balance)) #Just in case if your expense>income
def Income_Analysis():
    myfile=open("binarytesting.dat","rb")
    Income_analysis={}
    try :
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Income":
                if rec[4] in Income_analysis:
                    Income_analysis[rec[4]]+=rec[3]
                else:
                    Income_analysis[rec[4]]=rec[3]
    except EOFError:
        pass
    myfile.close()
    for i in Income_analysis:
        print(i,":","$",Income_analysis[i])
        print("------------")
def Expense_Analysis():
    myfile=open("binarytesting.dat","rb")
    expense_analysis={}
    try :
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Expense":
                if rec[4] in expense_analysis:
                    expense_analysis[rec[4]]+=rec[3]
                else:
                    expense_analysis[rec[4]]=rec[3]
    except EOFError:
        pass
    myfile.close()
    for i in expense_analysis:
        print(i,":","$",expense_analysis[i])
        print("------------")
def Monthly_Report():
    myfile=open("binarytesting.dat","rb")
    flag=False
    month=int(input("Enter the whose Monthly Report you want to find:"))
    try:
        while True:
            rec=pickle.load(myfile)
            if int(rec[1][3:5])==month:
                print("The Monthly report is:",rec)
                flag=True
    except EOFError:
        if not flag:
            print("Report Not Found!!!")    
    myfile.close()
def Saving_Goal_Tracker():
    myfile=open("binarytesting.dat","rb")
    savings_goal=int(input("Enter your Saving Goals:"))
    income_balance=0
    expense_balance=0
    try:
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Income"or rec[2]=="income":
                income_balance+=rec[3]
            elif rec[2]=="Expense"or rec[2]=="expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    myfile.close()
    balance=income_balance-expense_balance
    remaining=savings_goal-balance
    print("-----------------------------")
    print("Your Saving Goals are:","$",savings_goal)
    print("-----------------------------")
    print("Your Current Balance is :","$",balance)
    print("-----------------------------")
    print("Remaining:","$",remaining)
    print("-----------------------------")
def Highest_Income():
    myfile=open("binarytesting.dat","rb")
    highest=0
    try:
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Income"or rec[2]=="income":
                if rec[3]>highest:
                    highest=rec[3]
    except EOFError:
        pass
    myfile.close()
    print("Your Highest expense is:","$",highest)
def Highest_Expense():
    myfile=open("binarytesting.dat","rb")
    highest=0
    try:
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Expense"or rec[2]=="expense":
                if rec[3]>highest:
                    highest=rec[3]
    except EOFError:
        pass
    myfile.close()
    print("Your Highest expense is:","$",highest)
def Tax_Calculator():
    myfile=open("binarytesting.dat","rb")
    income_balance=0
    expense_balance=0
    try:
        while True:
            rec=pickle.load(myfile)
            if rec[2]=="Income"or rec[2]=="income":
                income_balance+=rec[3]
            elif rec[2]=="Expense"or rec[2]=="expense":
                expense_balance+=rec[3]
    except EOFError:
        pass
    myfile.close()
    balance=income_balance-expense_balance
    if balance>0:
        print("Congrats you're doing well!!!")
        print("Your Current Balance is:","$",balance)
    elif balance==0:
        print("Congrats!!! you're...broke😂🫵","$",balance)
    else:
        print("Too bad you're broke AND in debt of:","$",abs(balance))
    if income_balance<100000:
        tax_limit=random.randint(5000,25000)
        tax_rate=random.randint(8,15)   
    elif income_balance>=100000:
        tax_limit=random.randint(50000,500000)
        tax_rate=random.randint(15,25)   
    print("Your Tax Limit is:","$",tax_limit)
    print("-------------------------")                
    print("The Tax Rate comes out to be:",tax_rate,"%",)
    print("-------------------------")                            
    if income_balance>tax_limit:
        tax=(income_balance-tax_limit)*tax_rate/100    #Tax is calculated on random basis everytime
    else:                                                   
        tax=0                                               
    print("You have to pay:","$",tax,"as tax")
    print("-----------------------------")      
    final_balance=balance-tax #Your tax affects your balance                        
    print("Your Balance after Tax is:","$",final_balance)
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
    choice=int(input("Enter your choice from (0-15)"))
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












                    
