from django.contrib.auth.base_user import BaseUserManager
import hashlib
#from .requests import Poster
#from .beneficts import Jobber

class AccountManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        
        
        #self.password = hashlib.sha256(str.encode(password)).hexdigest()
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_sex(sex)
        user.set_role(role)
        user.set_last_name(last_name)
        user.set_first_name(first_name)
        user.set_district(district)
        user.set_photo(photo)
        user.set_phone_number(phone_number)
        user.set_password(password)
        user.save(using=self._db)

        return user



    def create_user(self, username, email=None, **extra_fields):
        
        return self._create_user(username, email, **extra_fields)