'''
Created on 2024/01/10

@author: t21cs011
'''
from django import forms
from superuserhome.models import Item as SuperuserItem
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class ItemBuy(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput())
    count = forms.IntegerField(label='購入個数', min_value=1)
    # 他のフィールドの定義...

    class Meta:
        model = SuperuserItem
        fields = ['item_id', 'price']
        widgets = {
            'item_id': forms.HiddenInput(),
            'price': forms.NumberInput(attrs={'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemBuy, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)

        # フォームの初期データから item_id を取得して設定
        item_id = self.initial.get('item_id', None)
        if item_id is not None:
            self.fields['item_id'].initial = item_id
            

    def clean(self):
        cleaned_data = super().clean()
        
        # item_id を取得して SuperuserItem を取得し、その price を cleaned_data に設定
        item_id = cleaned_data.get('item_id')
        if item_id:
            item = get_object_or_404(SuperuserItem, pk=item_id)
            cleaned_data['price'] = item.price

        return cleaned_data


class ItemIdForm(forms.Form):
    item_id = forms.IntegerField(label='ID')

class ItemForm(forms.ModelForm):
    class Meta:
        model = SuperuserItem
        fields = ['name', 'count', 'price','state']