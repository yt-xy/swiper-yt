from django.conf.urls import url

from user import apis as user_api

urlpatterns = [
    url(r'^api/user/get_vcode', user_api.get_vcode),
    url(r'^api/user/submit_vcode', user_api.submit_vcode),
    url(r'^api/user/get_profile', user_api.get_profile),
    url(r'^api/user/set_profile', user_api.set_profile),
    url(r'^api/user/upload_avatar', user_api.upload_avatar),
]
