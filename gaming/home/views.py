import xboxapi

from django.shortcuts import render
from xboxapi import XboxApi


# Create your views here.
def index(request):
    api = XboxApi(api_key="4cb573c13bc4fc40224d449e4dc3d92f44e930aa")

    get_profile = api.get_profile
    get_user_gamercard = api.get_user_gamercard
    get_user_friends = api.get_user_friends

    context = {
        'profile': get_profile,
        'gamercard_info': get_user_gamercard,
        'user_friends': get_user_friends,
    }

    return render(request, "home.html", context)
