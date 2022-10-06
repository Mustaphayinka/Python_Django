# Function based api views
# Function based api views
# Function based api views
# Function based api views

# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from .serializer import ArticleSerializer
# from .models import Article
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # Create your views here.

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True) #when you serialize a query set, you add many = True
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article) 
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)





# Class based view 
# Class based view 
# Class based view 

from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializer import ArticleSerializer
from .models import Article

# Generic views 
# Generic views 
# Generic views 
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Generic viewset
# Generic viewset
# Generic viewset

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

# Modal viewset
# Modal viewset
# Modal viewset
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()





# View set
# View set
# View set


# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True) #when you serialize a query set, you add many = True
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    # specify serializer class
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id= None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
            # Note : This post method does not work unless the path is modified in the url.py
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request, id)



class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) #when you serialize a query set, you add many = True
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # except AttributeError:
        #     return Response({
        #         'error':'Book does not exist'
        #     }, status = status.HTTP_404_NOT_FOUND)

        # except:
        #     return Response({
        #         'error':'Book does not exist'
        #     }, status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article=self.get_object(id)
        serializer = ArticleSerializer(article) 
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    