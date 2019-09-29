from django.db import models
# below are required to extend the django user model while \
# making use of some of the features that come with the django \
# user model out of the box
from django.contrib.auth.models import AbstractBaseUser, \
                        BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extras_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('New user requires an email address.')
        user = self.model(email=self.normalize_email(email), **extras_fields)
        user.set_password(password)
        user.save(using=self._db)

        return(user)

    def create_superuser(self, email, password):
        """creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model that support email rather than username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
