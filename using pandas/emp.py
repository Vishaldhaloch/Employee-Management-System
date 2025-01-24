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
   
      if Service.insert_record(emp):
         Service.write_data()
         print("Record inserted successfully")
      else:
         print("Record already existed")   

   # For view record
   elif choice == 2:
      Service.read_data()
      Service.view_record()

   # for search by id
   elif choice == 3:
      search = int(input("Enter the search id = "))
      Service.read_data()
      Service.search_by_id(search)
      
   # for delete by id
   elif choice == 4:
      delete = int(input("Enter the delete id = "))
      Service.delete_by_id(delete)
      Service.write_data()
      print("delete")
   
   # for search by name
   elif choice == 5:
      # Service.read_data()
      name = (input("Enter the  search name = "))
      Service.read_data()
      Service.search_by_name(name)
   
   # Search by contact    
   elif choice == 6:
      contact = input("Enter the search contact number = ")
      Service.read_data()
      Service.search_by_contact('contact')
   
   # Search salary by range
   elif choice == 7:
      lower_sal = int(input("Enter the lower salary = "))
      upper_sal = int(input("Enter the upper sal = "))
      Service.read_data()          
      emp = Service.search_by_salary_range(lower_sal,upper_sal)
      print(emp)
      
   # Search salary by ascending order   
   elif choice == 8:
      Service.read_data()
      sal = Service.search_salary_by_ascending_order()
      print(sal)
      
   # Search salary by decending order          
   elif choice == 9:
      Service.read_data()
      sal = Service.search_salary_by_descending_order()
      print(sal)
      
   # Search name by ascending order
   elif choice == 10:
      Service.read_data()
      n = Service.search_name_by_ascending_order()
      print(n)

   # Search name by decending order
   elif choice == 11:
      Service.read_data()
      n = Service.search_name_by_decending_order()
      print(n)
      
   # Exit
   elif choice == 12:
      sys.exit()

   else:
      print("Invalid option")   
