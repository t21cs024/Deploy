'''
Created on 2023/12/15

@author: t21cs011
'''
from django import forms
from .models import Item,ImageUpload
from datetime import date

class ItemBuy(forms.Form):
    status = (
            (0, '未購入'),
            (1, '購入済')
            )
    item_id = forms.IntegerField(label='ID')
    item_status = forms.ChoiceField(label='STATUS',widget=forms.Select, choices=status)


class ItemIdForm(forms.Form):
    item_id = forms.IntegerField(label='ID')

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'count', 'price','state']
        
class SignUpForm(forms.Form):
    id = forms.CharField(label='ID', required=True)
    full_name = forms.CharField(label='氏名', required=True)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='メールアドレス', required=True)
    authority = forms.BooleanField(label='権限', required=False)

    # 他のフィールドも適切に追加

class UserIdForm(forms.Form):
    emp_num = forms.IntegerField(label=False)

class MonthForm(forms.Form):
    buy_month = forms.IntegerField(label=False, min_value=1, max_value=12)
    
class CountForm(forms.Form):
    count = forms.IntegerField(label='個数', min_value=1)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"

class RetireDateForm(forms.Form):
    retire_date = forms.DateField(label=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フォームに初期データを設定
        self.fields['retire_date'].initial = date.today()