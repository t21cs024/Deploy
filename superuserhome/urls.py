'''
Created on 2023/12/12

@author: t21cs011
'''
from django.urls import path
from .views import QrCodeView,ImageUploadView,SuperUserHomeView ,UserEditView, OrderEditView, OldItemView, NewItemView, UserInformationView, UserInformationDetailView, TestView, PreDeductionOutputView, DeductionOutputView, CompanyManagementView, CompanyAddView, CompanyEditView, CompanyDeleteView, ItemDiscardView, ItemStockEditView, ItemInventoryControlView,ItemEditView,ItemDeleteView,UserDeleteView, ItemHalfView
from login.views import SignUpView
from . import views

app_name = 'superuserhome'
urlpatterns = [
    path('',SuperUserHomeView.as_view(), name="home"),
    path('useredit/',UserEditView.as_view(), name='useredit'),
    path('orderedit/',OrderEditView.as_view(),name='orderedit'),
    path('userinformation/', UserInformationView.as_view(), name='userinformation'),
    path('userinformation/<int:emp_num>/', UserInformationDetailView.as_view(), name='userinformation_detail'),
    path("userinformation/userdelete/<int:emp_num>/", UserDeleteView.as_view(), name="userdelete"),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('test/',TestView.as_view(), name='test'),
    path('deductionoutput/<int:emp_num>/',PreDeductionOutputView.as_view(), name='deductionoutput'),
    path('deductionoutput/<int:emp_num>/<int:buy_month>/',DeductionOutputView.as_view(), name='redeductionoutput'),
    path('orderedit/newitem/', NewItemView.as_view(), name='newitem'),
    path('orderedit/olditem/', OldItemView.as_view(), name='olditem'),
    path('orderedit/olditem/<int:item_id>/',QrCodeView.as_view(),name='qrcode'),
    path('orderedit/olditem/discardedit/<int:item_id>/', ItemDiscardView.as_view(), name='discardedit'),
    path('orderedit/olditem/stockedit/<int:item_id>/', ItemStockEditView.as_view(), name='stockedit'),
    path('orderedit/olditem/itemdiscard/<int:item_id>/', ItemInventoryControlView.as_view(), name='itemaddstock'),
    path('orderedit/olditem/itemaddstock/<int:item_id>/', ItemInventoryControlView.as_view(), name='itemdiscard'),
    path('orderedit/olditem/itemedit/<int:pk>/', ItemEditView.as_view(), name='itemedit'),
    path('orderedit/olditem/itemdelete/<int:pk>/', ItemDeleteView.as_view(), name='itemdelete'),
    path('orderedit/olditem/itemhalf/<int:item_id>/', ItemHalfView.as_view(), name='itemhalf'),
    path('orderedit/olditem/imagedelete/<int:image_title>/', views.delete_image, name='imagedelete'),
    path('companymanage/', CompanyManagementView.as_view(), name='companymanage'),
    path('companymanage/companyadd/', CompanyAddView.as_view(), name='companyadd'),
    path('companymanage/companyedit/<int:pk>/', CompanyEditView.as_view(), name='companyedit'),
    path('companymanage/companydelete/<int:pk>/', CompanyDeleteView.as_view(), name='companydelete'),
    path("orderedit/image_upload/", ImageUploadView.as_view(), name="image-upload"),
    ]
