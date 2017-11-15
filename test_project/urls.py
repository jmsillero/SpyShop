"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from rest_framework import viewsets, routers


from test_app.views.Category import CategoryViewSet
from test_app.views.Product import *
from test_app.views.Promotion import PromotionViewSet
from test_project import settings

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'promotion', PromotionViewSet)

api_url = [
    url(r'^product/category/(?P<categoryId>[^/.]+)/$', products_by_category, name='product-by-category'),
    url(r'^product/(?P<productId>[^/.]+)/relastets/$', relastets_product, name='relastets-products'),
    url(r'^', include(router.urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #api
    url(r'^api/v1/', include(api_url)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
