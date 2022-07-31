stack = {}
request = {}
user_register = []

class user_type:
    user_name:str

    def __init__(self,User:str):
        self.user_name = User

    def getUser(self):
        return self.user_name


class Portal:
    list_of_members = []
    user = {}
    user_choice : int
    def list_of_persons(self):
        self.list_of_members.append(user_type("Tenant"))
        self.list_of_members.append(user_type("Owner"))
        self.list_of_members.append(user_type("Admin"))
        print("\nWelcome to Online House Renting Portal\nHappy to help you")
        print("\nList of Users:")

    def show_list_of_users(self):
        if len(self.list_of_members)>0:
            count = 1
            for user in self.list_of_members:
                print(count,".",user.getUser())
                count+=1
    def store(self):
        user = {}
        user["UserId"] = input("Enter Userid:")
        user["Name"] = input("Enter name:")
        user["age"] = input("Enter age:")
        user["address"] = input("Enter address:")
        user["phone"] = input("Enter phone number:")
        user["typeOfUser"] = input("Enter typeOfUser:")
        user_register.append(user)
        print("\nUser registered Successfully!!")
        #stack.append(int(user["UserId"]))
        stack["UserId"] = user["UserId"]
        #print(stack)

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


#list_of_houses = []
class Tenant:
    list_of_houses = []
    house_no : int
    own_id : int
    def houses(self):
        self.list_of_houses.append(HouseDetails("Kodambakkam","Chennai",798,"2BHK","Rs.6000/Month",1))
        self.list_of_houses.append(HouseDetails("Goripalayam","Madurai",560,"1BHK","Rs.5500/Month",1))
        self.list_of_houses.append(HouseDetails("Anna nagar","Chennai",1200,"3BHK","Rs.15000/Month",2))

    def show_houses(self):
        print("                 -----List of Houses Available-----")
        sno = 1
        for num in self.list_of_houses:
            print(sno,".",num.getcity()," ",num.getRent())
            sno+=1
    def show_house_details(self):
        no = 1
        print("\nEnter House number to view full details of the house:")
        house_no = int(input())
        self.house_no = house_no
        for num in self.list_of_houses:
            if no==house_no:
                print(num.getlocality()," ",num.getcity()," ",num.getsquareFt()," ",num.gettype()," ",num.getRent()," ",num.getOwnerId())
            no+=1
        stack["HouseNo"] = house_no

    def makerequest(self):
        own_id = int(input("Enter Owner id to make a request:"))
        self.own_id = own_id
        house_no = int(input("Enter house number to make a request:"))
        self.house_no = house_no
        request["tenantid"] = stack["UserId"]
        request["ownid"] = own_id
        request["houseNo"] = house_no
        request["status"] = "Requested"
        print("\nYour request has been sent to the owner!!\nWe'll contact you soon!!")


class Owner(Tenant):
    own_id : int
    def addHouseDetails(self):
        self.list_of_houses.append(HouseDetails(input("Enter locality:\n"),input("Enter city:\n"),int(input("Enter squareFeet:\n")),input("Enter housetype:\n"),input("Enter rent:\n"),int(input("Enter Ownerid:"))))

    def RemoveHouses(self):
        own_id = int(input("Enter your id to remove your house from portal:"))
        self.own_id = own_id
        self.list_of_houses.pop(-1)

    def logout(self):
        print("\nLogged Out Successfully")


class History(Owner):
    #history_of_users = []
    user_id : int
    house_id : int
    def history(self):
        print("\nHistory of users:")
        for user_id,house_id in stack.items():
            print(user_id,":",house_id)

class Request():
    approve : int
    def requests(self):
        print("The requests are:")
        for i,j in request.items():
            print(i ,":",j)

    def approval(self):
        print("1 .Approved\n2. Declined")
        approved = int(input("Enter your status:"))
        self.approved = approved
        if approved==1:
            request["status"] = "Approved"
        elif approved==2:
            request["status"] = "Declined"


def loginagain(check_User_Choice):
    ownobj = Owner()
    req = Request()
    if check_User_Choice == 1:
        tenobj = Tenant()
        print("\nTenant Options:")
        print("1.View houses")
        print("2.Make request")
        print("3.View approval status:")
        print("4.Log out")
        option = int(input("Enter your preference:"))
        if option == 1:
            tenobj.houses()
            tenobj.show_houses()
            tenobj.show_house_details()
            check_User_Choice = obj.ask_user_choice()
            loginagain(check_User_Choice)

        elif option == 2:
            tenobj.makerequest()
            check_User_Choice = obj.ask_user_choice()
            loginagain(check_User_Choice)

        elif option == 3:
            req.requests()
            check_User_Choice = obj.ask_user_choice()
            loginagain(check_User_Choice)
        else:
            ownobj.logout()

    elif check_User_Choice == 2:
        print("\nOwner Options:")
        print("1. Add house")
        print("2. Remove house")
        print("3. View Requests/approval")
        print("4. Logout")
        option = int(input("Enter your preference:"))
        if option == 1:
            ownobj.addHouseDetails()
            ownobj.houses()
            ownobj.show_houses()
            print("\nHouse has been added successfully!!")
            check_User_Choice = obj.ask_user_choice()
            loginagain(check_User_Choice)

        elif option == 2:
            ownobj.houses()
            ownobj.RemoveHouses()
            ownobj.show_houses()
            print("\nHouse has been removed successfully!!")
            check_User_Choice = obj.ask_user_choice()
            loginagain(check_User_Choice)

        elif option == 3:
            req.requests()
            req.approval()
            check_User_Choice = obj.ask_user_choice()
            loginagain(check_User_Choice)

        elif option == 4:
            ownobj.logout()


    elif check_User_Choice == 3:
        pass

    else:
        print("Sorry:))!!\nThere is no such type of user...")
        print("Please Enter a correct option to process your request")
        obj.show_list_of_users()
        check_User_Choice = obj.ask_user_choice()
        loginagain(check_User_Choice)


obj = Portal()
obj.list_of_persons()
obj.show_list_of_users()
#obj.store()
check_User_Choice = obj.ask_user_choice()
obj.store()
loginagain(check_User_Choice)
his = History()
his.history()

