from django.views.generic import ListView
#from .models import User,Item,Cart,CartItem
from .models import Cart,CartItem
from superuserhome.models import Item as SuperuserItem
from django.views.generic.base import TemplateView,View
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ItemBuy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from superuserhome.models import BuyHistory

# Create your views here.

class UserHomeView(TemplateView):
    template_name = 'user_home.html'
    
# カメラキャプチャ用のクラス
class CameraView(TemplateView):
    model = SuperuserItem
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

class CartContentsView(TemplateView):
    model = SuperuserItem
    template_name = 'Order/cart/cart_contents.html'

    def get(self, request, *args, **kwargs):
        # ログインしているユーザを取得
        user = self.request.user
        # ユーザからカートを取得　無ければ作る
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart(user = user)
        # カートからCartItemの取得
        cart_item = CartItem.objects.filter(cart=cart)
        context = self.get_context_data()
        context['object_list'] = cart_item
        return self.render_to_response(context)


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
    success_url = '/userhome/buyitem'

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('item_id')
        item = get_object_or_404(SuperuserItem, pk=item_id)

        form = ItemBuy(initial={'item_id': item.id, 'item_status': item.state})

        return render(request, self.template_name, {'item': item, 'form': form})

    def post(self, request, *args, **kwargs):
        form = ItemBuy(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']
            item = get_object_or_404(SuperuserItem, pk=item_id)
            cart, created = Cart.objects.get_or_create(user=self.request.user)
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, item=item)
            cart_item.total = item.price * cart_item.quantity
            if item.count < form.cleaned_data['count']:
                cart_item.quantity = item.count
            else:
                if cart_item.quantity+form.cleaned_data['count'] > item.count:
                    cart_item.quantity = item.count
                else:
                    cart_item.quantity += form.cleaned_data['count'] 
            cart_item.total = item.price * cart_item.quantity
            cart_item.save()

            return redirect(self.success_url)

        # フォームがバリデーションエラーの場合も item を取得
        item_id = kwargs.get('item_id')
        item = get_object_or_404(SuperuserItem, pk=item_id)

        return render(request, self.template_name, {'item': item, 'form': form})
    