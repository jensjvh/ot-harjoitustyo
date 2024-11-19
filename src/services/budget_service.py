from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class BudgetService:
    """
    A class representing the application logic of the app.
    """

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):
        """
        Create a new user and log in by default.
        """
        existing_user = self._user_repository.find_user(username)

        if existing_user:
            return "Error"

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):
        """
        Log the user in.
        """
        user = self._user_repository.find_user(username)

        if not user or user.password != password:
            return "Error"

        self._user = user

        return user

    def logout(self):
        """
        Log the user out.
        """
        pass

    def get_current_user(self):
        return self._user


budget_service = BudgetService()