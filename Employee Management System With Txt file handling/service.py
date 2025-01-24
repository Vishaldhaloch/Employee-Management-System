# Bussiness Logic Layer(Datasource + Database)
from employee import Employee

datafile = "data.txt"

class Service:
    @classmethod
    def save_file(cls,emp):
        with open(datafile , "a") as f:
            f.write(str(emp.get_id())+ ","+ emp.get_name()+ ","+ str(emp.get_salary()) + "," + emp.get_contact()+ "\n")

    @classmethod
    def load_file(cls):
        emp_list = []
        with open(datafile, 'r') as f:
            for i in f:
                id, name, salary, contact = i.strip().split(',')
                emp_list.append(Employee(int(id), name, float(salary), contact))
        return emp_list

        # cls.emplist = []
        # employee_data = []
        # with open(datafile, 'r') as file:
        #     for i in file:
        #         id, name, salary, contact = i.strip().split(',')
        #         dict = { 'id': int(id),'name': name,'salary': float(salary),'contact': contact}
        #         employee_data.append(dict)
        #         cls.emplist.append(Employee(int(id), name, float(salary), contact))
        # return employee_data

    # For search by id only
    @classmethod
    def search_by_id(cls,id):
        emp = cls.load_file()
        for i in emp:
            if i.get_id() == id:
                return i
        return None
            
     
    # For delete by id only
    @classmethod
    def delete_by_id(cls,id):
        emp_list = cls.load_file()
        for e in emp_list:
            if e.get_id() == id:
                emp_list.remove(e)
                return True
        return False     


     #For search by  name
    @classmethod
    def search_by_name(cls,name):
        emp_list = cls.load_file()
        ls = []
        for emp in emp_list:
            if name in emp.get_name(): 
                ls.append(emp)
        return ls      
            
    # For search by contact
    @classmethod        
    def search_by_contact(cls,contact):
        emp_list = cls.load_file()
        c = []
        for i in emp_list:
           if contact in i.get_contact():
               c.append(i)
        return c
  
    # For search salary by range 
    @ classmethod
    def search_by_salary_range(cls,lower_sal,upper_sal):
        emp_list = cls.load_file()
        sal = []
        for i in  emp_list:   # i considered as object of employee
            if i.get_salary() >= lower_sal and i.get_salary() <= upper_sal:
                sal.append(i)    
        return sal      

    # For search salary by ascending order
    @classmethod
    def search_salary_by_ascending_order(cls):
        emp_list = cls.load_file()
        a = []
        for i in emp_list:
            a.append(i)
        b = len(a)
        for i in range(b-1):
            for j in range(0,b-i-1):
                if a[j].get_salary() > a[j+1].get_salary():
                    a[j],a[j+1] = a[j+1],a[j]
        return a

    # for Search salary by decending order
    @classmethod
    def search_salary_by_descending_order(cls):
        emp_list = cls.load_file()
        a = []
        for i in emp_list:
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
        emp_list = cls.load_file()
        a = []
        for i in emp_list:
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
        emp_list = cls.load_file()
        a = []
        for i in emp_list:
            a.append(i)
        b = len(a)
        for i in range(b-1):
            for j in range(0,b-i-1):
                if a[j].get_name() < a[j+1].get_name():
                    a[j],a[j+1] = a[j+1],a[j]
        return a
       
        
