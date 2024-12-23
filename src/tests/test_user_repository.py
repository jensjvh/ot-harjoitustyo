import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test1 = User('test1', 'test1234')

    def tearDown(self):
        user_repository.delete_all()

    def test_create(self):
        user_repository.create(self.user_test1)
        users = user_repository.find_all()

        self.assertEqual(users[0].username, self.user_test1.username)

    def test_create_returns_user(self):
        user = user_repository.create(self.user_test1)

        self.assertEqual(user, self.user_test1)

    def test_delete_all_users(self):
        user_repository.create(self.user_test1)
        user_repository.delete_all()
        users = user_repository.find_all()

        self.assertEqual(users, [])

    def test_find_user(self):
        user = user_repository.create(self.user_test1)
        found_user = user_repository.find_user('test1')

        self.assertEqual(user.username, found_user.username)

    def test_find_user_if_not_found(self):
        user = user_repository.create(self.user_test1)
        found_user = user_repository.find_user('test2')

        self.assertEqual(None, found_user)
