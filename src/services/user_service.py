from src.models.user import User


class UserService:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_one(email):
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            raise ValueError(f"User with email {email} not found")
        return existing_user
