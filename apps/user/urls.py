from django.urls import path
from .views.basic import RegisterView, LoginView, LogoutView
from .views.dashboard import ProductsView, CategoriesView, AddEditCartView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# import requests

# url = 'http://127.0.0.1:8000/user/login/'
# payload = {'email': 'user@gmail.com', 'password': '123'}

# response = requests.post(url, json=payload)

# print(response.status_code)
# print(response.text)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user_products/', ProductsView.as_view(), name='productsforuser'),
    path('categories/', CategoriesView.as_view(), name='categoriesforuser'),

    path('add_edit_cart/', AddEditCartView.as_view(), name='addeditcart'),

    


    # path('signup/', signup, name='signup'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
