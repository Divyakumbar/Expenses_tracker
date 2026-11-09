expences={}
def add_expence(i,j):
    expences[i]=j

def show_expence():
    print(expences)
while True:
 c=input("Enter your choice: ")
 if c=="1":
    i=input("enter name of expence: ")
    j=input("Enter cost: ")
    add_expence(i,j)
 elif c=="2":
    show_expence()
 else:
    print("Invalid")
    