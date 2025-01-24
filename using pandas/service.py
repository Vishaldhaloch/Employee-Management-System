# Bussiness Logic Layer(Datasource + Database)
from employee import Employee
import pandas as pd

class Service:
    data = "record.csv"
    emp_df = pd.DataFrame(columns=['ID', 'Name', 'Salary', 'Contact'])

    @classmethod
    def write_data(cls):
        cls.emp_df.to_csv(cls.data, index=False)

    @classmethod
    def read_data(cls):
        cls.emp_df = pd.read_csv(cls.data)
        print(cls.emp_df)
    
    
    # For insert Record only
    @classmethod
    def insert_record(cls,emp):
        if cls.search_by_id(emp.get_id()).empty:
            new= pd.DataFrame({'ID': [emp.get_id()], 'Name': [emp.get_name()], 'Salary': [emp.get_salary()], 'Contact': [emp.get_contact()]})
            cls.emp_df = pd.concat([cls.emp_df, new], ignore_index=True)
            return True
        else:
            return False
      
    # For view record only
    @classmethod
    def view_record(cls):
        return cls.emp_df

    # For search by id only
    @classmethod
    def search_by_id(cls, id):
        return cls.emp_df[cls.emp_df['ID'] == id]

    @classmethod
    def delete_by_id(cls, id):
        cls.emp_df = cls.emp_df[cls.emp_df['ID'] != id]
        return cls.emp_df

     #For search by  name
    @classmethod
    def search_by_name(cls,name):
        cls.emp_df = cls.emp_df[cls.emp_df['Name'] == name]
        return cls.emp_df

    # For search by contact
    @classmethod        
    def search_by_contact(cls,contact):
       cls.emp_df = cls.emp_df[cls.emp_df['Contact'] == contact]
       return cls.emp_df

    # For search salary by range 
    @ classmethod
    def search_by_salary_range(cls,lower_sal,upper_sal):
         cls.emp_df = cls.emp_df[(cls.emp_df['Salary'] >= lower_sal) & (cls.emp_df['Salary'] <= upper_sal)]
         return cls.emp_df

    # For search salary by ascending order
    @classmethod
    def search_salary_by_ascending_order(cls):
        return cls.emp_df.sort_values(by = ['Salary'])
   
    # for Search salary by decending order
    @classmethod
    def search_salary_by_descending_order(cls):
             return cls.emp_df.sort_values(by = ['Salary'],ascending = False)

    
    # # For search name by ascending order
    @classmethod
    def search_name_by_ascending_order(cls):
        return cls.emp_df.sort_values(by = ['Name'])
      
    # # For search name by decending order
    @classmethod
    def search_name_by_decending_order(cls):
        return cls.emp_df.sort_values(by = ['Name'],ascending = False)
    
    