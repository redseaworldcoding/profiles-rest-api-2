from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""

        if not email:
            raise ValueError('Users must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)  # creates a new models that the user manager is representing....

        user.set_password(password)   # puts the password into hash incryption....
        user.safe(using=self._db)    # standard procedure in djange of saving user information

        return user

    def create_superuser(self, email, name, password):
        """create and save a new superuser with given details"""
        user = self.create_user(email, name, password)     # create a new user objects

        user.is_superuser = True    # is_superuser is autoatically created in our UserProfile model
        user.is_staff = True
        user.save(using=self._db)

        return user






class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for: Databse model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()  # We are going to define UserProfileManager class ClassName(object):

    USERNAME_FIELD = 'email'  # We are overriding default username field to EmailField
    REQUIRED_FIELDS = ['name'] # we are sysing the user must provide email and NAME

    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of the user"""
        return self.NAME

# Finally, we need  to specify string specification of our user profiles_api
def __str__(self):
    """Return string representation of our user"""
    return self.email
