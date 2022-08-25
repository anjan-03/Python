import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists parking_system")
mycursor.execute("use parking_system")
mycursor.execute("create table if not exists parking(Vehicle_no varchar(20) primary key,Vehicle_type varchar(10),Owner_name varchar(100),Date_Time varchar(29))")
mydb.commit()
bikes=100
cars=250
bicycles=80
x=datetime.datetime.now()
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
def main():
    global bikes,cars,bicycles
    try:
        while True:
            print("--------------------------------------------------------------------------------")
            print("\t\tParking Management System")
            print("--------------------------------------------------------------------------------")
            print("********************************************************************************")
            print("   1.Vehicle Entry")                
            print("   2.Remove Entry")
            print("   3.View Parked Vehicle")  
            print("   4.View Left Parking Space")
            print("   5.Amount Details")
            print("   6.Bill")
            print("   7.Close Program")
            print("********************************************************************************")
            ch=int(input("   Select option:"))
            if ch==1:
                no=True
                while no==True:
                    print("########### ALL INFORMATION ARE MANDATORY TO BE FILLED #################")
                    Vno=input("\tEnter vehicle number (XX-XX-XX-XXXX) - ").upper()
                    if (Vno[0] in alphabet) and (Vno[1] in alphabet) and (Vno[6] in alphabet) and (Vno[7] in alphabet) and (Vno[3] in numbers) and (Vno[4] in numbers) and (Vno[9] in numbers) and (Vno[10] in numbers) and (Vno[11] in numbers) and (Vno[12] in numbers):
                        no=not True
                    elif Vno=="":
                        print("\tEnter Vehicle No.")
                    elif len(Vno)!=13:
                        print("\tEnter Valid Vehicle Number")
                    elif Vno in Vehicle_Number:
                        print("\tVehicle Number Already Exists")
                    else:
                        print("\tEnter Valid Vehicle Number")
                typee=True
                while typee==True:
                    Vtype=str(input("\tEnter vehicle type(Bicycle=A/Bike=B/Car=C): ")).lower()
                    if Vtype=="":
                        print("\tEnter Vehicle Type: ")
                    elif Vtype=="a":
                        Vehitype="Bicycle"
                        bicycles-=1
                        typee=not True
                    elif Vtype=="b":
                        Vehitype="Bike"
                        bikes-=1
                        typee=not True
                    elif Vtype=="c":
                        Vehitype="Car"
                        cars-=1
                        typee=not True
                    else:
                        print("\tPlease Enter Valid Option ")
                o=True
                while o==True:
                    OName=input("\tEnter owner name - ")
                    if OName=="":
                        print("\tPlease Enter Owner Name ")
                    else:
                        o=not True
                mycursor.execute("insert into parking values('"+str(Vno)+"','"+str(Vehitype)+"','"+str(OName)+"','"+str(x)+"')")
                mydb.commit()
                print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ RECORD DETAIL SAVED ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
            elif ch==2:
                no=True
                while no==True:
                    Vehi_no=input("\tEnter vehicle number to Delete(XX-XX-XX-XXXX) - ").upper()
                    if Vehi_no=="":
                        print("\tEnter Vehicle No. ")
                    elif len(Vehi_no)==13:
                        mycursor.execute("delete from parking where Vehicle_no='"+Vehi_no+"'")
                        mydb.commit()
                        print("\n✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔ REMOVED SUCCESSFULLY ✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
                        no=not True
                    else:
                        print("\tEnter Valid Vehicle Number ")
            elif ch==3:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\t\t\tParked Vehicle")
                mycursor.execute("select * from parking")
                myrecords=mycursor.fetchall()
                if myrecords==[]:
                    print("\t\t     No vehicles parked")
                for t in myrecords:
                    print(t)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif ch==4:
                print("--------------------------------------------------------------------")
                print("\t\t\t\tSpaces Left For Parking")
                print("--------------------------------------------------------------------")
                print("\tSpaces Available for Bicycle - ",bicycles)
                print("\tSpaces Available for Bike - ",bikes)
                print("\tSpaces Available for Car - ",cars)
                print("--------------------------------------------------------------------")
            elif ch==5:
                print("....................................................................")
                print("\t\t\t\tParking Rate")
                print("....................................................................")
                print("*1.Bicycle      Rs10 / Hour")
                print("*2.Bike         Rs40/ Hour")
                print("*3.Car          Rs60/ Hour")
                print("--------------------------------------------------------------------")
            elif ch==6:
                print(".................... Generating Bill ...............................")
                lot=True
                while lot==True:
                    Veno=input("\tEnter vehicle number(XXXX-XX-XXXX) - ").upper()
                    if Veno=="":
                        print("\tEnter Vehicle No. ")
                    elif len(Veno)==13:
                        mycursor.execute("select*from parking where Vehicle_no='"+Veno+"'")
                        for l in mycursor:
                            print(l)
                        lot=not True
                    else:
                        print("\tEnter Valid Vehicle Number ")
                mycursor.execute("select Date_Time from parking where Vehicle_no='"+Veno+"'")
                for w in mycursor:
                    print("\tVehicle Check in Date and Time - ",w)
                mycursor.execute("select Vehicle_Type from parking where Vehicle_no='"+Veno+"'")
                for e in mycursor:
                    print("\tVehicle Type - ",e)
                inp=True
                amt=0
                while inp==True:
                    print("\t☀☀☀☀ TODAY IS YOUR LUCKY DAY!! ☀☀☀☀")
                    print("  ▶▶NO NEED TO PAY FOR YOUR MINUTES AND WE WILL CONSIDER ONLY THE PASSED HOUR")
                    hr=input("\tEnter No. of Hours Vehicle Parked - ").lower()
                    if hr=="":
                        print("\tPlease Enter Hours ")
                    elif int(hr)==0 and Vehitype=="Bicycle":
                        amt=10
                        inp=not True
                    elif int(hr)==0 and Vehitype=="Bike":
                        amt=40
                        inp=not True
                    elif int(hr)==0 and Vehitype=="Car":
                        amt=60
                        inp=not True
                    elif int(hr)>=1:
                        if Vehitype=="Bicycle":
                            amt=int(hr)*int(10)
                            inp=not True
                        elif Vehitype=="Bike":
                            amt=int(hr)*int(40)
                            inp=not True
                        elif Vehitype=="Car":
                            amt=int(hr)*int(60)
                            inp=not True
                print("\t Parking Charge - ",amt)
                ac=18/100*int(amt)
                print("\tAdd. charge 18 % - ",ac)
                print("\tTotal Charge - ",int(amt)+int(ac))
                print("^_^ ^_^ ^_^ ^_^ ^_^ ^_^ Thank you for using our service ^_^ ^_^ ^_^ ^_^ ^_^ ^_^ ")
                a=input("\tPress Any Key to Proceed - ")
            elif ch==7:
                print("^_^ ^_^ ^_^ ^_^ ^_^ ^_^ Thank you for using our service ^_^ ^_^ ^_^ ^_^ ^_^ ^_^ ")
                print("\t\t BYE BYE!! \n \t  ***HAVE A SAFE JOURNERY AHEAD*** ")
                break
                quit
    except:
        main()
main()
