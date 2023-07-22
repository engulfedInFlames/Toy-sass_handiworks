from django.urls import path
from . import views
urlpatterns = [
    path("", views.renderIndex),
    path("pages/horror/",views.renderHorror ),
    path("pages/10x19/", views.render10x19),
    path("pages/tolv/", views.renderTolv),
    path("pages/rodic/", views.renderRodic),
    path("pages/paintbox/", views.renderPaintbox),
    path("pages/schwartz/", views.renderSchwartz),
    path("pages/beige/", views.renderBeige),
    path("pages/zoo/", views.renderZoo),
]
