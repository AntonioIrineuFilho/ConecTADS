from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class Register:

    @staticmethod
    def registerUser(_first_name, _last_name, _username, _email, _password):
        errors = dict()
        try:
            user = User.objects.get(username=_username)
        except User.DoesNotExist:
            user = None  
        if (user):
            errors["username"] = "Username já cadastrado no sistema"
        try:
            user = User.objects.get(email=_email)
        except User.DoesNotExist:
            user = None
        if (user):
            errors["email"] = "Email já cadastrado no sistema"
        if (len(errors) > 0):
            raise ValidationError(errors)
        hashed_password = make_password(_password)
        user = User(first_name=_first_name, last_name=_last_name, username=_username, email=_email, password=hashed_password)
        user.save()
        return user
        
