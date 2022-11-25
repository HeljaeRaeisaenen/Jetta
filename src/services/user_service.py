from repositories.user_repository import UserRepository

class UserService:

    def __init__(self, database):
        self.user_repository = UserRepository(database)
    
    def _check_if_user_exists(self, username):
        """Checks if there are users with the username

        Args:
            username (str): Username of the user searched

        Returns:
            Booelan: True if there are already a user, False if not
        """
        if self.user_repository.search_user(username=username):
            return True
        return False
    
    def create_user(self, username, password):
        """User creation

        Args:
            username (str): Username for user
            password (str): Password for user

        Returns:
            Boolean: False if there is already a user with the username
        """
        if self._check_if_user_exists(username=username):
            return False
        self.user_repository.create_user(username=username, password=password)

    def sign_in(self, username, password):
        """Sign in function

        Args:
            username (str): Username for user
            password (str): Password for user

        Returns:
            Boolean: True if sign in is succesful, False if not
        """
        return self.user_repository.sign_in(username=username, password=password)
