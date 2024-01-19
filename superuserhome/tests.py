from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date

from .models import Item, Order, PurchaseHistory, ImageUpload, Company
from login.models import CustomUser as User

from django.urls import reverse
from django.test import Client

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_id=1,
            name='a',
            user_name='a',
            user_pass='a',
            user_mail='a@gmail.com',
            user_authority=False
        )

    def test_user_str_method(self):
        self.assertEqual(str(self.user), 'a')

    # Add more tests for User model fields and methods as needed

class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name='apple',
            item_url='apple.png',
            count=10,
            price=100,
            state='in stock'
        )

    def test_item_str_method(self):
        self.assertEqual(str(self.item), 'apple(在庫あり)')

    # Add more tests for Item model fields and methods as needed

class OrderModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name='apple',
            item_url='apple.png',
            count=10,
            price=100,
            state='in stock'
        )
        self.order = Order.objects.create(
            item=self.item,
            order_weight=1.00,
            order_quantity=50,
            minimum_amount=10
        )

    def test_order_str_method(self):
        expected_str = 'apple(在庫あり) [発注重み:1.0] '
        actual_str = str(self.order)

        # 期待値と実際の結果を比較
        self.assertEqual(actual_str, expected_str)


    # Add more tests for Order model fields and methods as needed

class PurchaseHistoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_id=1,
            name='a',
            user_name='a',
            user_pass='a',
            user_mail='a@gmail.com',
            user_authority=False
        )
        self.purchase_history = PurchaseHistory.objects.create(
            user_id=self.user,
            buy_month=1,
            buy_amount=1000
        )

    def test_purchase_history_str_method(self):
        self.assertEqual(str(self.purchase_history), 'a : 1月')

    # Add more tests for PurchaseHistory model fields and methods as needed

class ImageUploadModelTest(TestCase):
    def setUp(self):
        self.image_upload = ImageUpload.objects.create(
            title='test_image',
            img='img/test_image.png'
        )

    def test_image_upload_str_method(self):
        self.assertEqual(str(self.image_upload), 'test_image')

    # Add more tests for ImageUpload model fields and methods as needed

class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_id=1,
            company_name='株式会社ワイ・シー・シー',
            company_address='111',
            company_mail='t21cs○○○@gmail.com',
            company_phone_number='111',
            manager_name='田中太郎',
            manager_phone_number='1111',
            manager_mail='tanaka@gmail.com'
        )

    def test_company_str_method(self):
        self.assertEqual(str(self.company), '株式会社ワイ・シー・シー')

    # Add more tests for Company model fields and methods as needed


    #viewのテスト





class SuperUserHomeViewTest(TestCase):


    def setUp(self):
        from django.contrib.auth.models import User
        # テストに必要なオブジェクトやデータをセットアップする
        self.user = User.objects.create_superuser(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')


    '''    
    def test_super_user_home_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:superuser_home')  # 'AutoOrder'はプロジェクト名
        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)
        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)
        # 正しいテンプレートが使用されていることを確認
        self.assertTemplateUsed(response, 'superuser_home.html')
        # レスポンスに必要なコンテキストが含まれているか確認
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'], self.user)
    '''



    def test_user_edit_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:useredit')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test_order_edit_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:orderedit')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test_new_item_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:newitem')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test_sign_up_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:signup')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test_user_information_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:userinformation')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    '''
    def test_user_information_detail_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:userinformation_detail')  # 'AutoOrder'はプロジェクト名
        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)
        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)
        # 他に必要なテストケースがあれば、同様に追加してください
    '''

    def test_old_item_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:olditem')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test__company_manage_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:companymanage')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test__company_add_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:companyadd')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください

    def test__image_upload_view(self):
        # ビューのURLを取得
        url = reverse('superuserhome:image-upload')  # 'AutoOrder'はプロジェクト名

        # ビューを呼び出し、レスポンスを取得
        response = self.client.get(url)

        # レスポンスのステータスコードが正しいことを確認
        self.assertEqual(response.status_code, 200)

        # 他に必要なテストケースがあれば、同様に追加してください
