
class AddressBook:

    def __init__(self):
        pass

    
    def selectOption(self):
        
        option = int(input("Enter option \n1:Add contact\n2:Update contact\n3:Delete contact\n3:Search contact\n4:Quit \n:"))
        
        option=int(input())
        
        if(option==1):
            book.addAddress()
        elif(option==2):
            book.updateAddress()
        elif(option==3):
            book.deleteAddress()
        else:
            print("Select Valid option")
            self.selectOption()  


        
    def addAddress(self):

        fname=str(input("enter first name: "))
        lname=str(input("enter last name: "))
        new_address=str(input("enter address: "))
        new_city=str(input("enter city: "))
        new_state=str(input("enter state: "))
        new_zipcode=str(input("enter zip: "))
        new_number=str(input("enter phone number: "))

        person_details = {
            first_name : fname,
            last_name  : lname,
            address   : new_address,
            city      : new_city,
            state     : new_state,
            zip       : new_zipcode,
            phone_number : new_number
        }

        self.addressdata = person_details

        print(self.addressdata)
        self.updateData(self.addressdata)

    
    def updateData(self,addressdata):
        try:
            with open("F:\Python\Object oriented programming\Addressbook\addressbook.json",'w') as addressbook:
                json.dump(addressdata,addressbook,indent=7)
        
        except Exception as e:
            print(e)
    
    def loadData(self):
        try:
            with open("F:\Python\Object oriented programming\Addressbook\addressbook.json",'r') as jsonfile:
                data =  json.load(jsonfile) 
                jsonfile.close()   
                return data
        except Exception as e : 

    def editAddress(self):

        option = int(input("Enter option to edit\n1: Address \n2:City \n3:State \n4: Phone number\n4)
        if(option==1):

        elif(option==2):
            
        elif(option==3):
            
        elif(option==4):
         

     
     
    def deleteAddress(self):

if _ _name__ == "__main__":

    book = AddressBook()
    book.selectOption()
      