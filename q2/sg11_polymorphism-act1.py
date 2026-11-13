# Parent Class - Patient
class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount

    def display_patient_type(self):
        print("Regular Patient")

# Child Class 1 - Senior Patient
class Senior_Patient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self._bill_amount - 0.20*self._bill_amount  # adds the discount

    def display_patient_type(self):
        print("Senior Citizen")

# Child Class 2 - PhilHealth Patient
class PhilHealth_Patient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self._bill_amount - 0.15*self._bill_amount  # adds the discount

    def display_patient_type(self):
        print("PhilHealth Member")

# Execution
def main():
    patient1 = Patient("Juan Dela Cruz", 15000)
    patient2 = Senior_Patient("Maria Santos", 15000)
    patient3 = PhilHealth_Patient("Pedro Reyes", 15000)
    print("Hospital Billing System \n-----------------------")
    print("Patient Name:", patient1.get_name())
    print("Patient Type:", patient1.display_patient_type())
    print(f"Original Bill: ₱{patient1.get_bill_amount():,.2f}")  # adds the two decimal places and comma in the money value
    print(f"Final Bill: ₱{patient1.calculate_bill():,.2f}")
    print("")
    print("Patient Name:", patient2.get_name())
    print("Patient Type:", patient2.display_patient_type())
    print(f"Original Bill: ₱{patient2.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient2.calculate_bill():,.2f}")
    print("")
    print("Patient Name:", patient3.get_name())
    print("Patient Type:", patient3.display_patient_type())
    print(f"Original Bill: ₱{patient3.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient3.calculate_bill():,.2f}")

main()