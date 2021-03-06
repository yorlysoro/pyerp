from django.urls import path
from django.contrib.auth import views as auth_views
from ..base.views import CustomerListView, PartnerDetailView, PartnerCreateView, PartnerUpdateView, DeletePartner, ProviderListView
from ..base.views import CompanyListView
from ..base.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, DeleteProduct
from ..base.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, DeleteUser, ChangePasswordForm, DoChangePassword
from ..base.views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, DeleteEmployee
from ..base.views import DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DeleteDepartment

urlpatterns = [
    path('users', UserListView.as_view(), name='users'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', DeleteUser, name='user-delete'),
    path('user/change-password/<int:pk>', ChangePasswordForm, name='password-change'),
    path('user/change-password-confirm/<int:pk>', DoChangePassword, name='do-change-password'),

    path('products', ProductListView.as_view(), name='products'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('Product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('Product/<int:pk>/delete/', DeleteProduct, name='product-delete'),

    path('companies', CompanyListView.as_view(), name='companies'),

    path('partners', CustomerListView.as_view(), name='partners'),
    path('provider', ProviderListView.as_view(), name='provider'),

    path('partner/add/', PartnerCreateView.as_view(), name='partner-add'),
    path('partner/<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('partner/<int:pk>/update', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/<int:pk>/delete/', DeletePartner, name='partner-delete'),

    path('employee', EmployeeListView.as_view(), name='employee'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', DeleteEmployee, name='employee-delete'),

    path('department', DepartmentListView.as_view(), name='department'),
    path('department/add/', DepartmentCreateView.as_view(), name='department-add'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('department/<int:pk>/update', DepartmentUpdateView.as_view(), name='department-update'),
    path('department/<int:pk>/delete/', DeleteDepartment, name='department-delete'),
]
