class Patient:
    def __init__(self,patient_id,name,Age,phone_number,medical_history):
        self.__patient_id=patient_id
        self.__name=name
        self.__Age=Age
        self.__phone_number=phone_number
        self.__medical_history=medical_history
    def validate(self):
        if self.__name =="":
               print("Name should not be empty")
        elif self.__Age <0:
             print("Age should be positive")
        elif self.__phone_number=="":
             print("Phone number should not be empty")
        else:
             print("Patient information valid") 
#2
class Doctor():
    def  calculate_bill(self):
         pass
class GeneralDoctor(Doctor):
    def calculate_bill(self):
         return 500
class SpeciallistDoctor(Doctor):
     def calculate_bill(self):
          return 1000
         
#3   
class Appointment():
     def book_appoitment(self,date,time):
          self.date=date
    
          self.time=time
          self.status="Booked"

     def  Cancel_appointment(self):
          self.status="Cancalled"
          print("appoinment cancelled")

     def  view_appointment(self):
           print("date:",self.date)
           print("time:",self.time)
           print("status:",self.status)

     def update_appoinment(self,status):
          if status in ("Booked","Confirmed","Cancelled","Completed"):
              self.status=status
              print("status update :",status)
          else:
               print("invalid")
         
#4
from abc import ABC,abstractmethod
class Payment(ABC):

     @abstractmethod
     def make_payment(sellf):
          pass 
class CashPayment(Payment):
     def make_payment(self):
          print("payment is completed cash")

class OnlinePayment(Payment):
     def make_payment(self):
          print("payment is completed online")





          

        
        
Patient1=Patient(1001,"rajesh",23,1234567891,"no medical history") 
Patient1.validate()

print("Patient ID:", Patient1._Patient__patient_id)
print("Name:", Patient1._Patient__name)
print("Age:", Patient1._Patient__Age)
print("Phone:", Patient1._Patient__phone_number)
print("Medical History:", Patient1._Patient__medical_history)

Patient2=Patient(1002,"raja",23,1234567091,"no medical history")        
Patient2.validate()


print("Patient ID:", Patient2._Patient__patient_id)
print("Name:", Patient2._Patient__name)
print("Age:", Patient2._Patient__Age)
print("Phone:", Patient2._Patient__phone_number)
print("Medical History:", Patient2._Patient__medical_history)

doctor1=GeneralDoctor()
print("general doctor fee:",doctor1.calculate_bill())
doctor2=SpeciallistDoctor()
print("specaillistDoctor:",doctor2.calculate_bill())

appointment=Appointment()
appointment.book_appoitment("07-10-26","12:02")
appointment.view_appointment()
appointment.update_appoinment("Confirmed")
#appointment.Cancel_appointment()

online=OnlinePayment()
#online.make_payment()
cash=CashPayment()
#cash.make_payment()
Payment=[CashPayment(),OnlinePayment()]

for payment in Payment:
    payment.make_payment()  
