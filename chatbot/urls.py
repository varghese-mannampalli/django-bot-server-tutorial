from django.conf.urls import url
from .views import TelegramBotView

urlpatterns = [
    url(r'^$', TelegramBotView.as_view())
]

