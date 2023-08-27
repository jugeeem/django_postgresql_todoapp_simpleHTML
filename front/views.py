import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'front/index.html'

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
