#object oriented programming
#we use classes tha contains(name, description, start date, end date, total students)-objects/instance
#its like we are modelling
#class=student and objects can be your description
#methods are items of a class

#syntax of OOP
#1. creating a  as cohort class
#class name starts with capital letter and must be singular
# class  Cohort:
#     name
#     description
#     start date
#     end date

# add a constructor for cohort class 
# add a method to the class that prints the cohort name, ad the total number of students
# create a new instance of the cohort class    


#a)
class Cohort:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = (start_date)
        self.end_date = (end_date)

cohort = Cohort("Apio", "she loves the python programming.", "2024/8/20", "2024/12/3")
print(cohort.name)
print(cohort.description)
print(cohort.start_date) 
print(cohort.end_date)          


#b)
class Python_cohort:
 def __init__(self,name,student_number):
    self.name = name
    self.student_number = student_number

p1= Python_cohort("cohort4","75")
print(f"Cohort name: {p1.name}")
print(f"total number of students: {p1.student_number}") 

#c)
class Cohort:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = (start_date)
        self.end_date = (end_date)

cohort4 = Cohort("Sharon", "Diploma in computer science.", "20/8/2024", "3/12/2024")
print(cohort4.name)
print(cohort4.description)
print(cohort4.start_date) 
print(cohort4.end_date) 