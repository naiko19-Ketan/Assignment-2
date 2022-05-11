print ("Can a Triangle be Formed?")
Side1 = int(input("Enter First Side :"))
Side2 = int(input("Enter Second Side :"))
Side3 = int(input("Enter Third side :"))
if Side1 <(Side2 + Side3) and Side2 <(Side3 + Side1) and Side3 <(Side1 + Side2) :
    print ("Yes")
else :
    print ("No")
