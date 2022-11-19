from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Category, Photo, Team


def home(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            from aiogram import Dispatcher, Bot, executor, types
            from aiogram.dispatcher.filters import Command
            from asyncio import new_event_loop, set_event_loop
            set_event_loop(new_event_loop())
            bot = Bot(token='5605527086:AAHwmUtU5oPDGr-zniEvcCaOwZo54ciXeyk')

            dp = Dispatcher(bot)

            async def first(message: types.Message):
                chat_id = 452785654
                email_subject = f' {form.cleaned_data["email"]} nomerdan: {form.cleaned_data["subject"]} boticha'
                email_message = f'Ismi {form.cleaned_data["first_name"]} Familiyasi {form.cleaned_data["last_name"]} murojat {form.cleaned_data["message"]}'
                await bot.send_message(chat_id=chat_id, text=f'{email_message} {email_subject}')

            @dp.message_handler()
            async def send_photo(message: types.Message):
                # photo=await bot.send_photo(chat_id=-1001791330353,photo='https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80')
                # print(photo.photo[-1].file_unique_id)
                await bot.set_chat_title(chat_id=-1001791330353, title='New names')
                link = await bot.export_chat_invite_link(chat_id=-1001791330353)
                print(link)

            executor.start_polling(dp, on_startup=first)



    else:
        form = AuthenticationForm()
    return render(request, 'photos/gallery.html',
                  {'categories': categories, 'photos': photos, 'team': Team.objects.all(), 'form': form
                   })


def gallery(request):
    category = request.GET.get('category')
    team = Team.objects.all()
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    else:
        form = AuthenticationForm()
    context = {'categories': categories, 'photos': photos, 'team': team, 'form': form}
    return render(request, 'photos/gallery.html', context)


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )
        return redirect('home')
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)


def UpdatePhoto(request, pk):
    categories = Category.objects.all()
    photo = Photo.objects.get(id=pk)
    if request.method == "POST":
        data = request.POST
        if data['category'] != 'None' and data['category_new'] == '':
            category = Category.objects.get(name=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        if len(request.FILES) != 0:
            photo.image = request.FILES['images']
        photo.category = category
        photo.description = request.POST.get('description')
        photo.save()
        messages.success(request, "Photo Updated Successfully")
        return redirect('home')
    return render(request, 'photos/update.html', {'photo': photo, 'categories': categories})


def DeletePhoto(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=pk)
        photo.delete()
    return redirect('home')


def addTeam(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.getlist('member_image')
        for image in image:
            Team.objects.create(
                name=data['member_name'],
                description=data['description'],
                image=image,
                facebook_url=data['facebook'],
                youtube_url=data['youtube'],
                twitter_url=data['twitter'],
                linkedin_url=data['linkedin'],
                instagram_url=data['instagram'],
                whatsapp_url=data['whatsapp'],
            )
        return redirect('home')
    return render(request, 'photos/team.html')


def DeleteTeam(request, pk):
    if request.method == 'POST':
        team = Team.objects.get(id=pk)
        team.delete()
    return redirect('home')


def UpdateTeam(request, pk):
    team = Team.objects.get(id=pk)
    data = request.POST
    if request.method == "POST":
        if len(request.FILES) != 0:
            team.image = request.FILES['image']
        team.description = request.POST.get('description')

        team.facebook_url = request.POST.get('facebook_url')
        team.youtube_url = request.POST.get('youtube_url')
        team.twitter_url = request.POST.get('twitter_url')
        team.linkedin_url = request.POST.get('linkedin_url')
        team.instagram_url = request.POST.get('instagram_url')
        team.whatsapp_url = request.POST.get('whatsapp_url')
        team.save()
        messages.success(request, "team member Updated Successfully")
        return redirect('home')
    return render(request, 'photos/update_team.html', {'team': team, })


def DeleteCategory(request, pk):
    if request.method == 'POST':
        category = Category.objects.get(id=pk)
        category.delete()
    return redirect('home')



