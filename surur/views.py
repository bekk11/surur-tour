from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'index.html'

    def get(self, request):
        return Response({'page': "Home"})


class AboutUs(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'generic.html'

    def get(self, request):
        return Response({'page': "About Us"})


class Reservation(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'elements.html'

    def get(self, request):
        return Response({'page': "Reservation"})
