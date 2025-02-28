from django.shortcuts import redirect

def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrap