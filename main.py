from employee2 import VacationDaysShortageError
from employee2 import Role
from employee2 import Employee
from employee2 import HourlyEmployee
from employee2 import SalariedEmployee
from employee2 import Company

def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    print(company.find_employees(role=Role.VICEPRESIDENT))
    print(company.find_employees(role=Role.MANAGER))
    print(company.find_employees(role=Role.INTERN))
    company.employees[0].pay()
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()