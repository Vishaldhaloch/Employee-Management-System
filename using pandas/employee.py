# Backend Layer

class Employee:
    def __init__(self,id=0,name="",salary=0.0,contact=""):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__contact = contact

    def get_id(self):
        return self.__id    

    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def get_contact(self):
        return self.__contact
    
    def set_id(self,id):
        self.__id = id

    def set_name(self,name):
        self.__name = name

    def set_salary(self,salary):
        self.__salary = salary

    def set_contact(self,contact):
        self.__contact = contact


    def __str__(self):
        return str(self.__id)+" "+ str(self.__name)+" "+ str(self.__salary)+" "+str(self.__contact) 


    
    