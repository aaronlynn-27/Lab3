import employee_info

print("Testing the employee info")

def test_get_employees_by_age_range():
    arr_test = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}
    ]

    test_result = employee_info.get_employees_by_age_range(24,31)
    assert(arr_test == test_result)

def test_calculate_average_salary():
    result = 60166.67
    test_result = employee_info.calculate_average_salary()

    assert abs(test_result - result) < 1e-6

def test_get_employee_dept():
    arr_test = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    test_result = employee_info.get_employees_by_dept("Sales")

    assert(test_result == arr_test)