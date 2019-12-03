from django.core.exceptions import PermissionDenied
from chapter.models import ChapterUser


def user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        user = ChapterUser.objects.get(pk=request.user.id)
        if user.has_been_authenticated:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap