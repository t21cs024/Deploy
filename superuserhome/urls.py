'''
Created on 2023/12/12

@author: t21cs011
'''
from django.urls import path,include
from .views import SuperUserHomeView ,UserEditView, OrderEditView, OldItemView, NewItemView, UserInformationView, UserInformationDetailView, SignUpView, TestView, PreDeductionOutputView, DeductionOutputView, CompanyManagementView, CompanyAddView, CompanyEditView, CompanyDeleteView, ItemEditView, ItemStockEditView, ItemInventoryControlView

app_name = 'superuserhome'
urlpatterns = [
    path('',SuperUserHomeView.as_view()),
    path('useredit/',UserEditView.as_view(), name='useredit'),
    path('orderedit/',OrderEditView.as_view(),name='orderedit'),
    path('userinformation/', UserInformationView.as_view(), name='userinformation'),
    path('userinformation/<int:user_id>/', UserInformationDetailView.as_view(), name='userinformation_detail'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('test/',TestView.as_view(), name='test'),
    path('deductionoutput/<int:user_id>/',PreDeductionOutputView.as_view(), name='deductionoutput'),
    path('deductionoutput/<int:user_id>/<int:buy_month>/',DeductionOutputView.as_view(), name='redeductionoutput'),
    path('orderedit/newitem/', NewItemView.as_view(), name='newitem'),
    path('orderedit/olditem/', OldItemView.as_view(), name='olditem'),
    path('orderedit/olditem/discardedit/<int:item_id>/', ItemEditView.as_view(), name='discardedit'),
    path('orderedit/olditem/stockedit/<int:item_id>/', ItemStockEditView.as_view(), name='stockedit'),
    path('orderedit/olditem/itemdiscard/<int:item_id>/', ItemInventoryControlView.as_view(), name='itemaddstock'),
    path('orderedit/olditem/itemaddstock/<int:item_id>/', ItemInventoryControlView.as_view(), name='itemdiscard'),
    path('companymanage/', CompanyManagementView.as_view(), name='companymanage'),
    path('companymanage/companyadd/', CompanyAddView.as_view(), name='companyadd'),
    path('companymanage/companyedit/<int:pk>/', CompanyEditView.as_view(), name='companyedit'),
    path('companymanage/companydelete/<int:pk>/', CompanyDeleteView.as_view(), name='companydelete'),
    ]
