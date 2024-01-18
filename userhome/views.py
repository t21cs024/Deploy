from django.views.generic import ListView
from .models import User,Item,Cart,CartItem
from superuserhome.models import BuyHistory
from superuserhome.models import Item as SuperuserItem
from django.views.generic.base import TemplateView,View
from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import ItemIdForm,ItemForm,ItemBuy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class UserHomeView(TemplateView):
    model = User
    template_name = 'user_home.html'
    
# カメラキャプチャ用のクラス
class CameraView(TemplateView):
    model = Item
    template_name = 'Order/buy_item.html'
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
           
class BuyHistoryView(ListView):
    template_name = 'Order/buy_history.html'
    model = BuyHistory
    context_object_name = 'object_list'

    def get_queryset(self):
        # ログインしているユーザを参照
        user = self.request.user
        # 日付で降順に並べてリストを表示
        return BuyHistory.objects.filter(user=user).order_by('-buy_date')

class CartContentsView(ListView):
    model = Item
    template_name = 'Order/cart/cart_contents.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # カートの内容を取得
        
        cart = self.request.user.cart
        cart_items = cart.cartitem_set.all()
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        
        if not cart_items:
            context['cart_is_empty'] = True
        else:
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            context['cart_items'] = cart_items
            context['total_price'] = total_price

        return context


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # セッションの再認証
            messages.success(request, 'パスワードが変更されました。')
            return redirect('/userhome')
            messages.error(request, 'パスワードの変更にエラーがあります。')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Order/change_pass.html', {'form': form})
    
    
@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    template_name = 'Order/cart/add_to_cart.html'
    form_class = ItemBuy
    success_url = reverse_lazy('buyitem')

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('item_id')
        item = get_object_or_404(SuperuserItem, pk=item_id)

        form = ItemBuy(initial={'item_id': item.id, 'item_status': 0, 'quantity': 1})

        return render(request, self.template_name, {'item': item, 'form': form})

    def form_valid(self, form):
        item_id = form.cleaned_data['item_id']
        item = get_object_or_404(SuperuserItem, pk=item_id)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, item=item)

        if not item_created:
            cart_item.quantity += form.cleaned_data['quantity']
            cart_item.save()

        return redirect(self.success_url)