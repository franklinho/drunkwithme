import facebook

from mobile.models import UserProfile


def create_user_profile(strategy, user,response, details,
                         is_new=False,*args,**kwargs):
    if not is_new:
        return

    UserProfile(user=user,
                first_name = details.get("first_name"),
                last_name = details.get("last_name")).save()
