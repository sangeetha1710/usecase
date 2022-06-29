
class user_type:
    user_name:str

    def __init__(self,User:str):
        self.user_name = User

    def getUser(self):
        return self.user_name



class Portal:
    list_of_members = []
    user_choice : int
    def list_of_persons(self):
        self.list_of_members.append(user_type("Tenant"))
        self.list_of_members.append(user_type("Owner"))
        self.list_of_members.append(user_type("Admin"))

    def show_list_of_users(self):
        print("\nWelcome to Online House Renting Portal\nHappy to help you")
        print("\nList of Users:")
        if len(self.list_of_members)>0:
            count = 1
            for user in self.list_of_members:
                print(count,".",user.getUser())
                count+=1
        else:
            print("\nThere is no such type of user")


    def ask_user_choice(self):
        return int(input("Enter what type of user you are:\n"))

class HouseDetails:
    locality_name : str
    city_name : str
    square_Feet : int
    house_type : str
    Rent_ : str
    Owner_Id : int
    def __init__(self,locality: str,city: str,squareFt: int,type: str,Rent: str,OwnerId: int):
        self.locality_name  = locality
        self.city_name = city
        self.square_Feet = squareFt
        self.house_type = type
        self.Rent_ = Rent
        self.Owner_Id = OwnerId
    def getlocality(self):
        return self.locality_name
    def getcity(self):
        return self.city_name
    def getsquareFt(self):
        return self.square_Feet
    def gettype(self):
        return self.house_type
    def getRent(self):
        return self.Rent_
    def getOwnerId(self):
        return self.Owner_Id



class Tenant:
    list_of_houses = []
    def houses(self):
        self.list_of_houses.append(HouseDetails("Kodambakkam","Chennai",798,"2BHK","Rs.6000/Month",1))
        self.list_of_houses.append(HouseDetails("Goripalayam","Madurai",560,"1BHK","Rs.5500/Month",1))
        self.list_of_houses.append(HouseDetails("Anna nagar","Chennai",1200,"3BHK","Rs.15000/Month",2))

    def show_houses(self):
        print("                 -----List of Houses Available-----")
        sno = 1
        for num in self.list_of_houses:
            print(sno,".",num.getlocality()," ",num.getcity()," ",num.getsquareFt()," ",num.gettype()," ",num.getRent()," ",num.getOwnerId())
            sno+=1


class Owner(Tenant):
    def addHouseDetails(self):
        self.list_of_houses.append(HouseDetails(input("Enter locality:\n"),input("Enter city:\n"),int(input("Enter squareFeet:\n")),input("Enter housetype:\n"),input("Enter rent:\n"),int(input("Enter Ownerid:"))))


obj = Portal()
obj.list_of_persons()
obj.show_list_of_users()
check_User_Choice = obj.ask_user_choice()

#ownobj = Owner()

if check_User_Choice==1:
    tenobj = Tenant()
    tenobj.houses()
    tenobj.show_houses()
    #ownobj.show_houses()


elif check_User_Choice==2:
    ownobj = Owner()
    ownobj.addHouseDetails()
    ownobj.houses()
    ownobj.show_houses()




