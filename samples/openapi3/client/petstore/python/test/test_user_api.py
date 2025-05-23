# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Create user
        """
        pass

    def test_create_users_with_array_input(self) -> None:
        """Test case for create_users_with_array_input

        Creates list of users with given input array
        """
        pass

    def test_create_users_with_list_input(self) -> None:
        """Test case for create_users_with_list_input

        Creates list of users with given input array
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete user
        """
        pass

    def test_get_user_by_name(self) -> None:
        """Test case for get_user_by_name

        Get user by user name
        """
        pass

    def test_login_user(self) -> None:
        """Test case for login_user

        Logs user into the system
        """
        pass

    def test_logout_user(self) -> None:
        """Test case for logout_user

        Logs out current logged in user session
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Updated user
        """
        pass


if __name__ == '__main__':
    unittest.main()
