from django.views.generic import ListView
from .models import User,Item
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignUpForm,UserIdForm

# Create your views here.
class SuperUserHomeView(TemplateView):
    model = User
    template_name = 'superuser_home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
class UserEditView(TemplateView):
    model = User
    template_name = "Edit/useredit.html"
    success_url=reverse_lazy('superuserhome')
    
class OrderEditView(TemplateView):
    model = Item
    template_name = "Edit/orderedit.html"
    
class NewItemView(TemplateView):
    model = Item
    template_name = "Edit/Item/newitem.html"
    
class SignUpView(TemplateView):
    model = User
    fields = ('user_id', 'name','user_menu', 'user_pass', 'user_mail','user_authority')
    template_name = "Edit/signup.html"
    success_url=reverse_lazy('superuserhome')

    def get(self, request, *args, **kwargs):
        form = SignUpForm()  # YourFormは適切なフォームのクラスに置き換えてください
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)  # YourFormは適切なフォームのクラスに置き換えてください
        if form.is_valid():
            # フォームのデータを使って新しいUserオブジェクトを作成
            new_user = User(
                user_id=form.cleaned_data['id'],
                name=form.cleaned_data['full_name'],
                user_pass=form.cleaned_data['password'],
                user_mail=form.cleaned_data['email'],
                user_authority=form.cleaned_data['authority'],
                # 他のフィールドも適切に追加
            )
            new_user.save()  # データベースに保存
            return redirect('superuserhome:useredit')  # 成功したら指定のURLにリダイレクト

        # フォームが無効な場合は再度入力を促す
        return render(request, self.template_name, {'form': form})

class UserInformationView(TemplateView):
    model = User
    template_name = "Edit/userinformation.html"

    def post(self, request, *args, **kwargs):
        user_id = self.request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        context = super().get_context_data(**kwargs)
        context['form_id'] = UserIdForm()
        context['user'] = user
        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = UserIdForm()
        return context



class TestView(TemplateView):
    model = User
    fields = ('user_id', 'name')
    template_name = "Edit/test.html"
    success_url = reverse_lazy('superuserhome')

    def get(self, request, *args, **kwargs):
        data_from_database = User.objects.all()
        return render(request, self.template_name, {'data_from_database': data_from_database})
    

class OldItemView(TemplateView):
    model = Item
    template_name = "Edit/Item/olditem.html"
    
    