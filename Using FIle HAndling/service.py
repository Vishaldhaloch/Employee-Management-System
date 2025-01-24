# Bussiness Logic Layer(Datasource + Database)
from employee import Employee
import csv
import os
class Service:

    data = "employee_data.csv"

    @classmethod
    def write_data(cls):
        with open(cls.data,"w",newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Salary', 'Contact'])
            for emp in cls.data:
                writer.writerow([emp.get_id(), emp.get_name(), emp.get_salary(), emp.get_contact()])
   
    @classmethod
    def read_data(cls):
        if os.path.exists(cls.data):
            with open(cls.data,'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
              

    # For insert Record only
    @classmethod
    def insert_record(cls,emp):
        cls.write_data
        if cls.search_by_id(emp.get_id()) == None:
            cls.data.append(emp)
            return True
        else:
            return False

    # For view record only
    @classmethod
    def view_record(cls):

        return cls.data

    # For search by id only
    @classmethod
    def search_by_id(cls,id):
        cls.read_data()
        for i in cls.data:
            if int(i['id']) == id:
                return i

    # For delete by id only
    @classmethod
    def delete_by_id(cls,id):
        Service.read_data()
        for i in cls.emp_data:
            if(i.get_id() == id):
                Service.write_data()
                cls.data.remove(i)
                return True
        return False        

     #For search by  name
    @classmethod
    def search_by_name(cls,name):
        Service.read_data()
        ls = []
        for i in cls.data:
            if name in i.get_name(): 
                ls.append(i)
        return ls      
    
    # For search by contact
    @classmethod        
    def search_by_contact(cls,contact):
        c = []
        for i in cls.emp_list:
           if contact in i.get_contact():
               c.append(i)
        return c
             
    # For search salary by range 
    @ classmethod
    def search_by_salary_range(cls,lower_sal,upper_sal):
        sal = []
        for i in  cls.emp_list:   # i considered as object of employee
            if i.get_salary() >= lower_sal and i.get_salary() <= upper_sal:
                sal.append(i)    

        return sal        

    # For search salary by ascending order
    @classmethod
    def search_salary_by_ascending_order(cls):
        # Service.read_data()
        a = []
        for i in cls.emp_list:
            a.append(i)
        b = len(a)

        for i in range(b):
            for j in range(0,b-i-1):
                if a[j].get_salary() > a[j+1].get_salary():
                    a[j],a[j+1] = a[j+1],a[j]
        return a
        
   

    # for Search salary by decending order
    @classmethod
    def search_salary_by_decending_order(cls):
        a = []
        for i in cls.emp_list:
            a.append(i)
        b = len(a)
        for i in range(b-1):
            for j in range(0,b-i-1):
                if a[j].get_salary() < a[j+1].get_salary():
                    a[j],a[j+1] = a[j+1],a[j]
        return a
       

    # # For search name by ascending order
    @classmethod
    def search_name_by_ascending_order(cls):
        a = []
        for i in cls.emp_list:
            a.append(i)
        b = len(a)
        for i in range(b-1):
            for j in range(0,b-i-1):
                if a[j].get_name() > a[j+1].get_name():
                    a[j],a[j+1] = a[j+1],a[j]
        return a
         
        
        
    # # For search name by decending order
    @classmethod
    def search_name_by_decending_order(cls):
        a = []
        for i in cls.emp_list:
            a.append(i)
        b = len(a)
        for i in range(b-1):
            for j in range(0,b-i-1):
                if a[j].get_name() < a[j+1].get_name():
                    a[j],a[j+1] = a[j+1],a[j]
        return a
       
        
