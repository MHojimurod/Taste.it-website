from django.shortcuts import render, redirect
from .models import Booking, User, Chef, Blog, Category, Product, Commentary
from .forms import BookingForm, UserForm, CommentaryForm
from django.core.paginator import Paginator, EmptyPage


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    blog = Blog.objects.all()
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
    blog = Blog.objects.all()
    p = Paginator(blog, 4)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    total = len(blog)
    total_num = 0
    if total < 2 or total > 2:
        if total < 2:
            total_num += 1
        else:
            if total % 2 < 2:
                total_num += (total // 2 + 1)
            elif total % 2 == 0:
                total_num += (total // 2)

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
