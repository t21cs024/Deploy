from django.test import TestCase
import unittest
from .models import User
from .models import Item
from .models import Cart
from .models import CartItem
from secretstorage import item
from datetime import datetime
from django.urls import reverse
from django.test import Client

# Create your tests here.
class UserTests(TestCase):
    def setUp(self):
        # テストに使用するユーザーデータを準備する
        self.test_user_data = {
            'name': 'test_name',
            'user_menu': 'test_user_menu',
            # 他の必要なフィールドがあればここに追加
        }

    def test_user(self):
        test_user = User(**self.test_user_data)
        self.assertEqual(test_user.name, self.test_user_data['name'])
        self.assertEqual(test_user.user_menu, self.test_user_data['user_menu'])

class ItemTests(TestCase):
    def setUp(self):
        self.test_item_data = {
            'name': 'test_name',
            'item_url': 'test_item_url',
            'count': 0,
            'buy_date': 'test_buy_date',
            'price': 100,
            'buy': False,
            # 他の必要なフィールドがあればここに追加
        }

    def test_item(self):
        test_item = Item(**self.test_item_data)
        self.assertEqual(test_item.name, self.test_item_data['name'])
        self.assertEqual(test_item.item_url, self.test_item_data['item_url'])
        self.assertGreaterEqual(test_item.count, 0)
        self.assertEqual(test_item.buy_date, self.test_item_data['buy_date'])
        self.assertGreaterEqual(test_item.price, 0)
        self.assertFalse(test_item.buy)






class TestCart(unittest.TestCase):

    def setUp(self):
        # テストに使用するユーザーデータを準備する
        self.test_user_data = {
            'name': 'test_name',
            'user_menu': 'test_user_menu',
            # 他の必要なフィールドがあればここに追加
        }

        # テストに使用する商品データを準備する
        self.test_item_data = {
            'name': 'test_name',
            'item_url': 'test_item_url',
            'count': 0,
            'buy_date': datetime.now().strftime("%Y-%m-%d"),  # 有効な日付形式に変更
            'price': 100,
            'buy': False,
            # 他の必要なフィールドがあればここに追加
        }

        # テストに使用するカートデータを準備する
        self.test_cart_data = {
            'user': User(**self.test_user_data),
            'items': [self.test_item_data],  # アイテムデータをモデルのインスタンスに変更
        }

    def test_cart(self):
        # ユーザーを保存
        self.test_cart_data['user'].save()

        # テストカートを作成
        test_cart = Cart(user=self.test_cart_data['user'])
        test_cart.save()

        # カートにアイテムを追加
        for item_data in self.test_cart_data['items']:
            item_data['buy_date'] = datetime.strptime(item_data['buy_date'], "%Y-%m-%d").date()
            item = Item.objects.create(**item_data)
            test_cart.items.add(item)

        # テストデータと実際のデータを比較する際に、辞書からアイテムの属性に変更
        expected_items = [f"{item['name']}({item['buy_date']})" for item in self.test_cart_data['items']]
        actual_items = [f"{item.name}({item.buy_date})" for item in test_cart.items.all()]

        self.assertEqual(actual_items, expected_items)
        self.assertEqual(test_cart.user, self.test_cart_data['user'])



class CartItemTests(TestCase):
    def setUp(self):
        # テストに使用するユーザーデータを準備する
        self.test_user_data = {
            'name': 'test_name',
            'user_menu': 'test_user_menu',
        }

        # テストに使用する商品データを準備する
        self.test_item_data = {
            'name': 'test_name',
            'item_url': 'test_item_url',
            'count': 0,
            'buy_date': datetime.now().strftime("%Y-%m-%d"),
            'price': 100,
            'buy': False,
        }

        # テストに使用するユーザーを作成
        self.test_user = User.objects.create(**self.test_user_data)

        # テストに使用するカートを作成
        self.test_cart = Cart.objects.create(user=self.test_user)

        # テストに使用する商品を作成
        self.test_item = Item.objects.create(**self.test_item_data)

        # テストに使用するカートアイテムデータを準備する
        self.test_cart_item_data = {
            'cart': self.test_cart,
            'item': self.test_item,
            'quantity': 1,
        }

    def test_cartitem(self):
        # カートアイテムを作成
        test_cartitem = CartItem.objects.create(**self.test_cart_item_data)

        self.assertEqual(test_cartitem.cart, self.test_cart_item_data['cart'])
        self.assertEqual(test_cartitem.item, self.test_cart_item_data['item'])
        self.assertEqual(test_cartitem.quantity, self.test_cart_item_data['quantity'])





#viewのテスト

class UserHomeViewTest(TestCase):


    def setUp(self):
        from django.contrib.auth.models import User
        # テストに必要なオブジェクトやデータをセットアップする
        self.user = User.objects.create_superuser(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')


    def test_buy_item_view(self):
        # ビューのURLを取得
        url = reverse('userhome:buyitem')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

    def test_buy_history_view(self):
        # ビューのURLを取得
        url = reverse('userhome:buyhistory')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

    def test_change_pass_view(self):
        # ビューのURLを取得
        url = reverse('userhome:changepass')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

    def test_cart_contents_view(self):
        # ビューのURLを取得
        url = reverse('userhome:cartcontents')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)
        '''   
    def test_sendor_dermail_view(self):
        # ビューのURLを取得
        url = reverse('userhome:sendordermail')  # 'AutoOrder'はプロジェクト名
        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)
        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)
        '''
