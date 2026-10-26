class Patient:

    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = 0.0
        self.set_bill_amount(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative")
        self.__bill_amount = float(bill_amount)

    def calculate_bill(self):
            discounted_amount = self.get_bill_amount() * 1.00
            print("\nPatient Name:" ,self.__name )
            print("Original Bill: ₱" , self.__bill_amount)
            print("Final Bill: ₱", discounted_amount)

class SeniorPatient(Patient):
    def calculate_bill(self):
        discounted_amount = self.get_bill_amount() * 0.80
        print("\nPatient Name:" ,super().get_name())
        print("Original Bill: ₱" , super().get_bill_amount())
        print("Final Bill: ₱", discounted_amount)


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        discounted_amount = self.get_bill_amount() * 0.85
        print("\nPatient Name:" ,super().get_name())
        print("Original Bill: ₱" , super().get_bill_amount())
        print("Final Bill: ₱", discounted_amount)

regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

for patient in patients:
    patient.calculate_bill()
