import pytest
from math_operations import add, get_value, check_age_of_user


@pytest.fixture
def user():
    return {
        "name": "Michal",
        "age": 30,
        "city": "Szczecin"
    }


# @pytest.mark.parametrize(
#     "first_number, second_number, result",
#     [
#         (1, 1, 2),
#         (2, 2, 4),
#         (3, 3, 6),
#         (3, 3, 7)
#     ]
# )
# def test_add(first_number, second_number, result):
#     assert add(first_number, second_number) == result

# def test_add_2():
#     assert add(1, 1) == 2
#     assert add(1, 1) == 2
#     assert add(1, 1) == 5


def test_get_value(user):
    assert get_value(user, "name") == "Michal"


def test_check_age_of_user(user):
    assert check_age_of_user(user) == 30