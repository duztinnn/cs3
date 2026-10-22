class Patient:
    def __init__(self, name: str, bill_amount: float):

        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_bill_amount(self) -> float:
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount

    def calculate_bill(self) -> float:
        return self.__bill_amount

class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self) -> float:
        original_bill = self.get_bill_amount()
        return original_bill * 0.80

class PhilHealthPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self) -> float:
        original_bill = self.get_bill_amount()
        return original_bill * 0.85

if __name__ == "__main__":

    regular_patient = Patient("Juan Dela Cruz", 15000.0)

    senior_patient = SeniorPatient("Maria Santos", 20000.0)

    philhealth_patient = PhilHealthPatient("Antonio Luna", 18500.0)

    print("=== HOSPITAL BILLING SYSTEM ===")
    print(f"Patient Name: {regular_patient.get_name()}")
    print(f"Original Bill: ₱{regular_patient.get_bill_amount():,.2f}")
    print(f"Final Computed Bill: ₱{regular_patient.calculate_bill():,.2f}")
    print("-" * 35)

    print(f"Patient Name: {senior_patient.get_name()} (Senior Citizen)")
    print(f"Original Bill: ₱{senior_patient.get_bill_amount():,.2f}")
    print(f"Final Computed Bill (20% Discount): ₱{senior_patient.calculate_bill():,.2f}")
    print("-" * 35)

    print(f"Patient Name: {philhealth_patient.get_name()} (PhilHealth)")
    print(f"Original Bill: ₱{philhealth_patient.get_bill_amount():,.2f}")
    print(f"Final Computed Bill (15% Discount): ₱{philhealth_patient.calculate_bill():,.2f}")
    print("=" * 35)
