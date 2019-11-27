from django.core.cache import cache

from common import stat
from libs.http import render_json
from user import logics
from user.models import User, Profile


# 获取短信验证码
def get_vcode(request):
    phonenum = request.GET.get('phonenum')
    status = logics.send_vcode(phonenum)
    if status:
        return render_json()
    else:
        return render_json(code=stat.SEND_SMS_ERR)

# 通过验证码登录、注册
def submit_vcode(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    cached_vcode = cache.get('Vcode-%s' % phonenum)  # 取出缓存的验证码

    # 检查验证码是否正确
    if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum)  # 创建用户

        # 执行登录过程
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(code=stat.VCODE_ERR)

# 获取个人资料
def get_profile(request):
    profile, _ = Profile.objects.get_or_create(id=request.uid)
    return render_json(profile.to_dict())

# 修改个人资料
def set_profile(request):
    return

# 头像上传
def upload_avatar(request):
    return
