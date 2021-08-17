from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

from jungledevs.users.api.views import CreateUserView

app_name = "api"
urlpatterns = [
    path("sign-up/", CreateUserView.as_view(), name="sign-up"),
    path("admin/", include(("jungledevs.authors.api.urls", "admin"), namespace="admin-authors")),
    path("admin/", include(("jungledevs.articles.api.admin_urls", "admin"), namespace="admin-articles")),
    path("articles/", include(("jungledevs.articles.api.urls", "articles"), namespace="articles")),
    # DRF Auth Token
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
