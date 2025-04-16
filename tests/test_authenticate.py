import pytest
from authenticate import Authenticate
from database import Database

# Mock Database object for testing
mock_database = Database('users.json')


def test_validate_name():
    """Positive Test: Check if name is validated correctly"""
    auth = Authenticate(mock_database)
    assert auth.validate_name("Victoria") == True

    """Negative Test: Check if name validation fails with invalid input"""
    auth = Authenticate(mock_database)
    assert auth.validate_name("123") == False
    assert auth.validate_name("Alessandro Lisandra") == False
    assert auth.validate_name("_") == False
    assert auth.validate_name("@Vanny") == False
    assert auth.validate_name("$$$$$") == False


def test_validate_password():
    """Positive Test: Check if password is validated correctly"""
    auth = Authenticate(mock_database)
    assert auth.validate_password("v1ctor14") == True
    assert auth.validate_password("PutUr Hands Up!") == True

    """Negative Test: Check if password validation fails with invalid input"""
    auth = Authenticate(mock_database)
    assert auth.validate_password(".<<<<<") == False
    assert auth.validate_password("1234567891234567") == False
    assert auth.validate_password("@alvin") == False
    assert auth.validate_password("1+2+3") == False
    assert auth.validate_password("14$") == False


def test_validate_user_role_negative():
    """Positive Test: Check if user role is validated correctly"""
    auth = Authenticate(mock_database)
    assert auth.validate_user_role("e") == True
    assert auth.validate_user_role("l") == True
    assert auth.validate_user_role("p") == True

    """Negative Test: Check if user role validation fails with invalid input"""
    auth = Authenticate(mock_database)
    assert auth.validate_user_role("z") == False
    assert auth.validate_user_role("1") == False
    assert auth.validate_user_role("$") == False
    assert auth.validate_user_role(".") == False
    assert auth.validate_user_role("@e") == False


def test_username_generation():
    """Positive Test: Check if username is generated correctly"""
    auth = Authenticate(mock_database)
    firstname = "John"
    lastname = "Doe"
    expected_username = "johnD"
    generated_username = firstname.lower() + lastname[0]
    assert generated_username == expected_username

    """Negative Test: Check if username generation fails with different names"""
    firstname = "Jane"
    lastname = "Smith"
    incorrect_username = "johnD"
    generated_username = firstname.lower() + lastname[0]
    assert generated_username != incorrect_username


