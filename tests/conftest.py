import pytest
import tests.test_model as tm

@pytest.fixture
def test_instance():
    instance = tm.TestClass()
    instance.setup_method(test_cases_file='data/sample_test_cases/class1/lite_class1_test_cases1.json')
    return instance
