
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Menu import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('recipe/<slug:category>', views.recipe, name="recipe"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('login-form', views.loginForm, name="login-form"),
    path('logout', views.logout, name="logout"),
    path('menu', views.menu, name="menu"),
    path('add-menu', views.addMenu, name="add-menu"),
    path('add-menu-store', views.addMenuStore, name="add-menu-store"),
    path('edit-menu/<int:menu_id>', views.menuEdit, name="edit-menu"),
    path('edit-menu-update', views.updateMenu, name="edit-menu-update"),
    path('delete-menu/<int:menu_id>', views.menuDelete, name="delete-menu"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
