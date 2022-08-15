from  datetime import date
class student:
  
  def __init__(self,name,gender,city,dob,job):
    self.name=name
    self.gender=gender
    self.city=city
    self.dob=dob
    self.job=job
    
  @classmethod
  def stu_data(cls,data):
      name,gender,city,dob,job=data.split(",")
      return cls(name,gender,city,dob,job)
  @staticmethod
  def student(job):
  	available_job=['teacher,typist']
  	if job in available_job:
  	   return True
  	return False

stu1=student("Santhosh","Male","Thiruvannamalai",2007,"teacher")
stu2=student("Pavi","Female","Chennai",2003,"typist")

data='Archana,Female,coimbatore,2005,typist'
stu3=student.stu_data(data)
print(stu3.name)
print(stu3.gender)
print(stu3.city)
print(stu3.dob)
print(stu1.student('teacher'))
print(stu2.student('typist'))
