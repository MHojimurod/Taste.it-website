from .forms import EmailForm
from .models import Subscribe, Instagram
from django.core.mail import send_mail
from django.conf import settings


def email_post(request):
    model = Subscribe()
    form = EmailForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            print(email)
            send_mail('contact',
                      'abc',
                      settings.EMAIL_HOST_USER,
                      [f"{email}"],
                      fail_silently=False
                      )
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
        'ins2': ins2
    }
    return ctx
