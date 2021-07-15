from django.shortcuts import render, redirect
from .models import Booking, User, Chef, Blog, Category, Product, Commentary
from .forms import BookingForm, UserForm, CommentaryForm
from django.core.paginator import Paginator, EmptyPage


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    blog = Blog.objects.all().order_by('-created_at')[:6]
    model = Booking()
    form = BookingForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        'h_active': 'active',
        'form': form,
        'blog': blog,
        'category': category,
        'products': products
    }
    return render(request, 'main/index.html', ctx)


def about(request):
    ctx = {
        'a_active': 'active'
    }
    return render(request, 'main/about.html', ctx)


def chef(request):
    chef = Chef.objects.all()
    ctx = {
        'ch_active': 'active',
        'chef': chef
    }
    return render(request, 'main/chef.html', ctx)


def menu(request):
    category = Category.objects.all()
    products = Product.objects.all()

    ctx = {
        'm_active': 'active',
        'category': category,
        'products': products
    }
    return render(request, 'main/menu.html', ctx)


def reservation(request):
    model = Booking()
    form = BookingForm(request.POST, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')
        else:
            print(form.errors)
    ctx = {
        'r_active': 'active',
        'form': form
    }
    return render(request, 'main/reservation.html', ctx)


def blogs(request):
    blog = Blog.objects.all().order_by('-created_at')
    p = Paginator(blog, 6)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    total = len(blog)
    total_num = 0
    if total < 6 or total > 6:
        if total < 6:
            total_num += 1
        else:
            if total % 6 < 6:
                total_num += (total // 6 + 1)
            elif total % 6 == 0:
                total_num += (total // 6)

    ctx = {
        'b_active': 'active',
        'page': page,
        'page_num': page_num,
        'total_num': total_num,
        'page_number': page.number
    }
    return render(request, 'main/blog.html', ctx)


def blog_single(request, pk):
    blogg = Blog.objects.filter(pk=pk)
    model = Commentary()
    form = CommentaryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
    comment = Commentary.objects.filter(blog_id=pk)
    length_comment = len(comment)
    ctx = {
        "blogg": blogg,
        'form': form,
        'comment': comment,
        'length': length_comment
    }
    return render(request, 'main/blog-single.html', ctx)


def contact(request):
    model = User()
    form = UserForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    ctx = {
        'c_active': 'active',
        'form': form
    }
    return render(request, 'main/contact.html', ctx)


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     print(subject,message,from_email)
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['cool.hojimurod2001@gmail.com'])
#         except BadHeaderError:
#             print(BadHeaderError)
#         #     return HttpResponse('Invalid header found.')
#         # return HttpResponseRedirect('/contact/thanks/')
#     # else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         # return HttpResponse('Make sure all fields are entered and valid.')
#     return render(request,'main/send_email.html')