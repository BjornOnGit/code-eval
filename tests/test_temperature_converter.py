test_cases_temperature = [
    {"input": "32", "expected_output": "0 Celsius is 32 Fahrenheit"},
    {"input": "100", "expected_output": "100 Celsius is 212 Fahrenheit"}
]

def test_temperature_converter(student_module):
    assert student_module.convert(0) == "0 Celsius is 32 Fahrenheit"
    assert student_module.convert(100) == "100 Celsius is 212 Fahrenheit"
