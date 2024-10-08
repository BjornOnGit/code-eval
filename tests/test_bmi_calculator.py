test_cases_bmi = [
    {"input": [70, 1.75], "expected_output": "BMI: 22.86"},
    {"input": [90, 1.8], "expected_output": "BMI: 27.78"}
]

def test_bmi_calculator(student_module):
    assert student_module.calculate(70, 1.75) == "BMI: 22.86"
    assert student_module.calculate(90, 1.8) == "BMI: 27.78"
