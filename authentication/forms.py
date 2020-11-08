from django.contrib.auth.forms import AuthenticationForm

class FormLogin(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(FormLogin,self).__init__(request=request, *args, **kwargs)