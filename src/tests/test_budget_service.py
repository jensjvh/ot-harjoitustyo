import unittest
from services.budget_service import budget_service, InvalidCredentialsError
from repositories.user_repository import user_repository
from entities.user import User


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test1 = User('test1', 'test1234')

    def tearDown(self):
        user_repository.delete_all()

    def test_invalid_register_credentials(self):
        with self.assertRaises(InvalidCredentialsError) as context:
            budget_service.create_user('test_invalid', 'short')

        self.assertEqual(str(context.exception),
                         "Password should be at least 8 characters long")

    def test_invalid_login_credentials(self):
        with self.assertRaises(InvalidCredentialsError) as context:
            budget_service.login('test_invalid', 'unknownuser')

        self.assertEqual(str(context.exception),
                         "Invalid username or password")
