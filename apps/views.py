from django.contrib import auth
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import login
from apps.forms import UsersCreationForm, LoginForm, MessageForm
from apps.models import Food, My_User, Menu, Contact, Category, Message, News, Message1, Newss
from django.views.generic import CreateView
from .tasks import send_email_customer


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = My_User.objects.get(username=username)
            if user:
                login(request, user)
                return redirect('index')

    return render(request, 'login.html')


def register(request):
    context = {
        'form': UsersCreationForm()
    }
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        context['form'] = form
    return render(request, 'auth_page.html', context)


class IndexView(TemplateView):
    template_name = "index.html"
    model = Food

    def get_context_data(self, **kwargs):
        context = {}
        context["foods"] = Food.objects.all()
        return context


class HomeView(TemplateView):
    template_name = "about.html"
    model = My_User

    def get_context_data(self, **kwargs):
        context = {}
        context["users"] = My_User.objects.all()
        return context


class SendEmailView(View):
    success_url = '/'
    template_name = 'contact.html'

    def get(self, request):
        form = MessageForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        is_reservation = request.POST.get("is_reservation")
        if int(is_reservation):
            full_name = request.POST.get('full_name', None)
            email = request.POST.get('email', None)
            phone_Number = request.POST.get('subject', None)
            people = request.POST.get('people', None)
            date = request.POST.get('date', None)
            time = request.POST.get('time', None)
            message = request.POST.get('message', None)
            message = f'{full_name}\n{email}\n{phone_Number}\n{people}'
            send_email_customer.delay(email, message)


        else:
            full_name = request.POST.get('full_name', None)
            email = request.POST.get('email', None)
            subject = request.POST.get('subject', None)
            message = request.POST.get('message', None)
            message = f'{full_name}\n{email}\n{subject}\n{message}'
            send_email_customer.delay(email, message)
        return redirect(self.success_url)


class SendEmailNewsView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = '/'
    template_name = 'news-detail.html'

    def form_invalid(self, form):
        send_email_customer.delay(form.instance.email, form.instance.message)
        return super().form_invalid(form)


class Email(CreateView):
    model = Message1
    form_class = MessageForm
    success_url = '/'
    template_name = 'base.html'

    def form_invalid(self, form):
        print("Invalid")
        send_email_customer.delay(form.instance.email, form.instance.message)
        return super().form_invalid(form)


class CategoryView(TemplateView):
    template_name = "menu.html"
    model = Contact

    def get_context_data(self, **kwargs):
        context = {}
        context["categories"] = Category.objects.all()
        return context


class MenuView(TemplateView):
    template_name = "menu.html"
    model = Menu

    def get_context_data(self, **kwargs):
        context = {}
        foods = Food.objects.all()
        context["categories"] = Category.objects.all()
        if self.request.GET.get('q'):
            foods = Food.objects.filter(name__icontains=self.request.GET['q'])
        context["foods"] = foods
        return context


class NewsView(TemplateView):
    template_name = "news.html"
    model = News

    def get_context_data(self, **kwargs):
        context = {}
        context["news"] = News.objects.all()
        return context


class NewsdetailView(DetailView):
    model = Newss
    template_name = 'news-detail.html'


def logout(request):
    auth.logout(request)
    return redirect('index')
