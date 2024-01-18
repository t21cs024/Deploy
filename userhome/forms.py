'''
Created on 2024/01/10

@author: t21cs011
'''
from django import forms
from superuserhome.models import Item as SuperuserItem
from django.core.exceptions import ValidationError

class ItemBuy(forms.Form):
    count = forms.IntegerField(label='購入個数', min_value=1)
    price = forms.DecimalField(label='価格', required=False, widget=forms.NumberInput(attrs={'readonly': True}))

    
    class Meta:
        model = SuperuserItem
        fields = ['item_id', 'item_status', 'count', 'price']
        widgets = {
            'item_id': forms.HiddenInput(),
            'price': forms.NumberInput(attrs={'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemBuy, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        initial['count'] = 1  # count フィールドの初期値を1に設定
        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        item_status = cleaned_data.get('item_status')

        if item_status != 0:
            raise ValidationError('購入可能な状態ではありません。')

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