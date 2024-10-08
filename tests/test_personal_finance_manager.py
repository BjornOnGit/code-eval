test_cases_finance = [
    {"input": {"income": 3000, "expenses": 2000}, "expected_output": "Net savings: 1000"},
    {"input": {"income": 2500, "expenses": 2500}, "expected_output": "Net savings: 0"}
]

def test_personal_finance_manager(student_module):
    assert student_module.calculate(3000, 2000) == "Net savings: 1000"
    assert student_module.alculate(2500, 2500) == "Net savings: 0"
