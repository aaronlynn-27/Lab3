import Lab2.bmi as bmi

def test_bmi_under_weight():
    test_output = -1
    result = bmi.calculate_bmi(1.8, 50)
    assert (result == test_output)

def test_bmi_normal_weight():
    test_output = 0
    result = bmi.calculate_bmi(1.75, 70)
    assert (result == test_output)

def test_bmi_over_weight():
    test_output = 1
    result = bmi.calculate_bmi(1.6, 80)
    assert (result == test_output)