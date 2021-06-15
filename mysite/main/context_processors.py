from .forms import EmailForm
from .models import Subscribe , Instagram

def email_post(request):
    model = Subscribe()
    form = EmailForm(request.POST,instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    ctx = {
        'email_form': form
    }
    return ctx


def instagram(request):
    ins = Instagram.objects.all().order_by('-created_at')[:3]
    ins2 = Instagram.objects.all().order_by('-created_at')[3:6]
    ctx = {
        'ins': ins,
        'ins2':ins2
    }
    return ctx
