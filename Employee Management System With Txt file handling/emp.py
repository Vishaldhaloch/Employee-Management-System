# Presentation Layer
from service import Service
from employee import Employee
from os import sys
while True:
    print()
    print("1.Insert Record")
    print("2.View record")
    print("3.Search by id")
    print("4.delete by id")
    print("5.Search by name")
    print("6.Search by contact")
    print("7.Search salary by range")
    print("8.Search Salary by ascending order")
    print("9.Search Salary by decending order")
    print("10.Search Name by ascending order")
    print("11.Search Name by decending order")
    print("12.Exit")
    print()
    print()
   
    choice = int(input("Enter the choice number:"))

    if choice == 1:

      emp = Employee()
      
      emp.set_id(int(input("Enter id = ")))
      emp.set_name (input("Enter name = "))
      emp.set_salary(float(input("Enter salary = ")))
      emp.set_contact(input("Enter contact = "))

      if Service.save_file(emp):
            print("Not inserted successfully.")
      else:
            print("insert record successfully.")

   
    # For view record
    elif choice == 2:
      emp = Service.load_file()
      for e in emp: 
         print("name",e.get_name())
         print("id",e.get_id())
         print("salary",e.get_salary())
         print("contact",e.get_contact())
      
    # for search by id
    elif choice == 3:
      search = int(input("Enter the search id = "))
      e = Service.search_by_id(search)
      if e == None:
         print("No id found")
      else:
         print("id found")   
         # print(e)
         print("name",e.get_name())
         print("id",e.get_id())
         print("salary",e.get_salary())
         print("contact",e.get_contact())

    # for delete by id
    elif choice == 4:
      delete = int(input("Enter the delete id = ")) 
      if Service.delete_by_id(delete):
         print("delete")
      else:
         print(" no Record found..")   
      
    # for search by name
    elif choice == 5:
       name = (input("Enter the  search name = "))
       e = Service.search_by_name(name)
       if e == None:
         print("not found")
       else:
         print(" found") 
         for i in e:
            print("id",i.get_id())
            print("name",i.get_name())
            print("salary",i.get_salary())
            print("contact",i.get_contact())
        
   # Search by contact    
    elif choice == 6:
       contact = input("Enter the search contact number = ")
       e = Service.search_by_contact(contact)
       if e == None:
           print(" no contact found")
         #   for i in e:
         #       print("contact",i.get_contact())
         #       print("id",i.get_id())
         #       print("name",i.get_name())
         #       print("salary",i.get_salary())
       else:
          print("contact found")  
          for i in e:
            print("contact",i.get_contact())
            print("id",i.get_id())
            print("name",i.get_name())
            print("salary",i.get_salary())
              
   # Search salary by range
    elif choice == 7:
       
       lower_sal = int(input("Enter the lower salary = "))
       upper_sal = int(input("Enter the upper sal = "))          
       e = Service.search_by_salary_range(lower_sal,upper_sal)
       if e == None:
          print("no salary found ")
       else:
          print("search salary found")
          for i in e:
            print("salary",i.get_salary())
            print("id",i.get_id())
            print("name",i.get_name())
            print("contact",i.get_contact())

   # Search salary by ascending order
            
    elif choice == 8:
      # salary = float(input("Enter the salary: "))    
      sal = Service.search_salary_by_ascending_order()
      for i in sal:
         print("salary",i.get_salary())
         print("id",i.get_id())
         print("name",i.get_name())
         print("contact",i.get_contact())

   
   # Search salary by decending order  
               
    elif choice == 9:
   
      sal = Service.search_salary_by_descending_order()
      for i in sal:
         print("salary",i.get_salary())
         print("id",i.get_id())
         print("name",i.get_name())
         print("contact",i.get_contact())
      
       
    # Search name by ascending order
    elif choice == 10:

      n = Service.search_name_by_ascending_order()
      for i in n:
         print("name",i.get_name())
         print("id",i.get_id())
         print("salary",i.get_salary())
         print("contact",i.get_contact())
     
    
   # # Search name by decending order
    elif choice == 11:
      n = Service.search_name_by_decending_order()
      for i in n:
         print("name",i.get_name())
         print("id",i.get_id())
         print("salary",i.get_salary())
         print("contact",i.get_contact())
    
    # Exit
    elif choice == 12:
       sys.exit()

    else:
       print("Invalid option")   

