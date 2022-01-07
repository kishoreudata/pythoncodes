
import pandas as pd
import numpy as np

import matplotlib.pyplot
# defining functions
def insert_row(alumni):
    print("Please Enter the following details of the new record: \n")
    a=input("enter alumni ID:  ")
    alu_id.append(a)
    n=input("enter name:  ")
    names.append(n)
    y=input("enter year:  ")
    year.append(y)
    s=input("enter stream:  ")
    stream.append(s)
    p=input("enter percentage:  ")
    percentage.append(p)
    #df = {"S.No":alumni.count(),"Alumni ID":a,"Name":n,"Year":y,"Stream":s,"Percentage":p}
    #alumni = alumni.append(df, ignore_index=True)
    alumni = pd.DataFrame({"Alumni ID": alu_id, "Name": names, "Year": year, "Stream": stream, "Percentage": percentage})
    print("record added succesfully")
    return alumni


def insert_column(alumni):
    cname=input("enter column name: ")
    c=[]
    print("enter column elements: ")
    n=alumni.shape[0]
    for i in range(0,n):
        ele=input()
        c.append(ele)
    alumni[cname]=c
    return alumni

def delete_row(alumni):
    alumni=alumni.drop(labels=None,axis=0,index=alumni.shape[0]-1,columns=None)
    print("last record deleted successfully")
    return alumni
def delete_column(alumni):
    #data.iloc[:, :-1]
    alumni=alumni.iloc[:,:-1]
    print("last column deleted succesfully")
    return alumni

def pd_to_csv(alumni):
    alumni.to_csv('file_name.csv',mode = 'w', index=False)
    print("Data saved successfully into a CSV file")

def read_csv():
    print("Enter csv filename")
    filename=input()
    DATA = pd.read_csv(filename+'.csv')

alu_id,names,year,stream,percentage=[],[],[],[],[]
alumni=pd.DataFrame({"Alumni ID":alu_id,"Name":names,"Year":year,"Stream":stream,"Percentage":percentage})


def main():
    # printing the starting line
    print("WELCOME TO A SIMPLE DATAFRAME PROGRAM")
    print("\n")
    global alumni
# creating options
    while True:
        print("\nMAIN MENU")
        print("1. Insert a record")
        print("2. Insert a column")
        print("3. Delete a row")
        print("4. Delete a column")
        print("5. Display the dataframe")
        print("6. Save Dataframe to CSV")
        print("7. Exit")
        choice = int(input("Enter the Choice:"))

        if choice == 1:alumni=insert_row(alumni)
        elif choice == 2:alumni=insert_column(alumni)
        elif choice == 3:alumni=delete_row(alumni)
        elif choice == 4:alumni=delete_column(alumni)
        elif choice == 5:print(alumni)
        elif choice == 6:pd_to_csv(alumni)
        elif choice == 7:
            break

        else:
            print("Oops! Incorrect Choice.")

if __name__ == "__main__":
    main()