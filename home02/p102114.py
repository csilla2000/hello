n=int(input())
for i in range(1,n+1):
    n = int(input())
    if n>0 and n<50:
        print("elegtelen")
    elif n>50 and n<60:
        print("elegseges")
    elif n>60 and n<70:
        print("kozepes")
    elif n>70 and n<80:
        print("jo")
    if n>80 and n<=100:
        print("jeles")



