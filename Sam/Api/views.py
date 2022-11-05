from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MarketSerializer, PersonSerializer, AadharSerializer, ArtistSerializer, SongSerializer, StudentSerializer, CourseSerializer, HouseSerializer, MovieSerializer, GameSerializer, PhoneSerializer, ForestSerializer
from .models import Market, Person, Aadhar, Artist, Song, Student, Course, House, Movie, Game, Phone, Forest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import mixins
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404

# -----------------------------------------Function based views----------------------------------------
# Here i am using Market model


@api_view(['GET'])
def get_markets(request):

    market = Market.objects.all()
    serializer = MarketSerializer(market, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_market(request,pk):

    market = Market.objects.get(pk=pk)
    serializer = MarketSerializer(market, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_new_market(request):

    serializer = MarketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_market(request,pk):

    market = Market.objects.get(id=pk)
    serializer = MarketSerializer(instance=market, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Market data updated successfully")
    else:
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def update_market_partially(request,pk):

    market = Market.objects.get(id=pk)
    serializer = MarketSerializer(instance=market, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response("Market data updated successfully")
    else:
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_market(request, pk):
    market = Market.objects.get(pk=pk)
    market.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------Class based views ---------------------------------------
# Here i am using Person and Aadhar models which are in OneToOne relationship with each other
# Class based view using APIView base class
# APIView class provides http handler methods such as get(), post(), put(), patch() and delete()
class PersonView(APIView):

    def get(self, request):
        students = Person.objects.all()
        serializer = PersonSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailView(APIView):

    def get(self,request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(instance=person, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------mixins + GenericAPIView----------------------------------------
# Class based view using GenericAPIView class
# GenericAPIView extends APIView class
# GenericAPIView class is a more loaded version of APIView class
# GenericAPIView and Mixins are used together
# GenericAPIView provides 2 important methods such as queryset and serializer_class
# We can either assign value to queryset or return the value from get_queryset() and get_object() method by
# overriding which is implemented in GenericAPIView class
# We can either assign value to serializer_class or return the value from get_serializer_class() and get_serializer()
# method by overriding which is implemented in GenericAPIView class
# Mixins provide 5 important mixins
# ListModelMixin has list() method
# CreateModelMixin has create() method
# RetrieveModelMixin has retrieve() method
# UpdateModelMixin have update() and partial_update() methods
# DestroyModelMixin has destroy() method


class AadharView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

    serializer_class = AadharSerializer
    queryset = Aadhar.objects.all()

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class AadharViewList(mixins.ListModelMixin, GenericAPIView):

    serializer_class = AadharSerializer
    queryset = Aadhar.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

# -------------------------Concrete views--------------------------------
# LINK : https://testdriven.io/blog/drf-views-part-2/
# Concrete views internally implements all methods that are in mixins and GenericAPIView
# So We don't need to write any method for any functionality
# Here, I am using Artist and Song table which as one-to-many relationship with each other
# There are 9 concrete views
# I am going to use 1 concrete view class i.e, RetrieveUpdateDestroyAPIView


class ArtistView(RetrieveUpdateDestroyAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistCreateView(CreateAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongView(RetrieveUpdateDestroyAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongCreateView(CreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class StudentView(RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(CreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseView(RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateView(CreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# --------------------------------------------------------------------------------------------------------
# ----------------------------------View sets-------------------------------------------------------------
# -------------------------1) ViewSet 2) GenericViewSet 3) ModelViewSet 4) ReadOnlyViewSet ----------------

class HouseViewSet(ViewSet):  # This view is for ViewSet using House model for all objects

    def list(self,request):
        queryset = House.objects.all()
        serializer = HouseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseDetailViewSet(ViewSet): # This view is for ViewSet using House model for detail objects

    def retrieve(self,request,pk=None):
        queryset = House.objects.all()
        house = get_object_or_404(queryset, pk=pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def update(self,request,pk=None):
        house = House.objects.get(pk=pk)
        serializer = HouseSerializer(instance=house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        house = House.objects.get(pk=pk)
        serializer = HouseSerializer(instance=house, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        house = House.objects.get(pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(GenericViewSet): # This view is for GenericViewSet using Movie model for all objects

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request):

        movie_serializer = self.serializer_class(self.queryset,many=True)
        return Response(movie_serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        movie_serializer = self.serializer_class(data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailViewSet(GenericViewSet): # This view is for GenericViewSet using Movie model for detail objects

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self,request, pk=None):
        movie_obj = self.queryset.get(pk=pk)
        movie_serializer = self.serializer_class(movie_obj)
        return Response(movie_serializer.data)

    def update(self,request,pk=None):
        movie_obj = self.queryset.get(pk=pk)
        movie_serializer = self.serializer_class(instance=movie_obj, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        movie_obj = self.queryset.get(pk=pk)
        movie_serializer = self.serializer_class(instance=movie_obj, data=request.data,partial=True)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        movie_obj = self.queryset.get(pk=pk)
        movie_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameViewSet(ModelViewSet): # This view is for ModelViewSet using Movie model

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PhoneViewSet(ReadOnlyModelViewSet): # This view is for ReadOnlyModelViewSet using Phone model

    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

# -----------------------------------------------------------------------------------
# -------- Views using GenericApiView by overriding some methods ----------
# I override get_queryset(), get_serializer(), get_serializer_class(), and  get_object() instead of using
# queryset and serializer_class attributes to pass the required data in GenericApiView class based views.


class ForestView(GenericAPIView):

    def get_queryset(self):
        return Forest.objects.all()

    def get_serializer_class(self):
        return ForestSerializer

    def get_serializer(self, *args, **kwargs):

        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get(self,request):

        forest_query_set = self.get_queryset()
        forest_serializer = self.get_serializer(forest_query_set, many=True)
        return Response(forest_serializer.data)

    def post(self,request):

        forest_serializer = self.get_serializer(data=request.data)
        if forest_serializer.is_valid():
            forest_serializer.save()
            return Response(forest_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(forest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForestDetailView(GenericAPIView):

    def get_queryset(self):
        return Forest.objects.all()

    def get_object(self):
        forest_id = self.kwargs['pk']
        forest_obj = self.get_queryset()
        return forest_obj.get(pk=forest_id)

    def get_serializer_class(self):
        return ForestSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get(self,request,pk):
        forest = self.get_object()
        forest_serializer = self.get_serializer(forest)
        return Response(forest_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        forest = self.get_object()
        forest_serializer = self.get_serializer(forest, data=request.data)
        if forest_serializer.is_valid():
            forest_serializer.save()
            return Response(forest_serializer.data)
        return Response(forest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        forest = self.get_object()
        forest_serializer = self.get_serializer(forest, data=request.data, partial=True)
        if forest_serializer.is_valid():
            forest_serializer.save()
            return Response(forest_serializer.data)
        return Response(forest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        forest = self.get_object()
        forest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------
