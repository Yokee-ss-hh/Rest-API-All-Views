from django.urls import path, include
from .views import get_markets,get_market, add_new_market, update_market, update_market_partially, delete_market, PersonView, PersonDetailView, AadharView,AadharViewList, ArtistView,ArtistCreateView, SongView,SongCreateView, StudentView,StudentCreateView, CourseView, CourseCreateView, HouseViewSet, HouseDetailViewSet, MovieViewSet, MovieDetailViewSet, GameViewSet, PhoneViewSet, ForestView, ForestDetailView
from rest_framework.routers import DefaultRouter,SimpleRouter

# -------Hectic way of routing for House model and ViewSet--------
house_list = HouseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
house_detail = HouseDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
# --------Simple way using DefaultRouter for House model and ViewSet----------------------------------
default_router = DefaultRouter(trailing_slash=True)
default_router.register(r'got-houses', HouseViewSet, basename='houses_all')
default_router.register(r'got-detail_houses', HouseDetailViewSet, basename='houses_detail')
# --------- Simple way using SimpleRouter for House model and ViewSet ---------------------------------------
simple_router = SimpleRouter(trailing_slash=True)
simple_router.register(r'all-houses',HouseViewSet, basename='all_houses')
simple_router.register(r'detail-houses',HouseDetailViewSet, basename='detail_houses')
# --------------------DefaultRouter for Movie model and GenericViewSet----------------------------
movie_default_router = DefaultRouter(trailing_slash=True)
movie_default_router.register(r'movies',MovieViewSet, basename='all_movies')
movie_default_router.register(r'detail-movies',MovieDetailViewSet, basename='detail_movies')
# ----------------------------DefaultRouter for Game model and ModelViewSet----------------------
game_default_router = DefaultRouter(trailing_slash=True)
game_default_router.register(r'games',GameViewSet,basename='all_and_detail_games')
# ----------------------------DefaultRouter for Phone model and ReadOnlyModelViewSet----------------------
phone_default_router = DefaultRouter(trailing_slash=True)
phone_default_router.register(r'phones',PhoneViewSet,basename='all_and_detail_phones')

urlpatterns = [
    path('houses/', house_list, name='house-list'),
    path('houses/<int:pk>/', house_detail, name='house-detail'),
    path('got-d/',include(default_router.urls)),
    path('got-s/',include(simple_router.urls)),
    path('mov/',include(movie_default_router.urls)),
    path('ga/',include(game_default_router.urls)),
    path('ph/',include(phone_default_router.urls)),
    path('markets/',get_markets, name="markets"),
    path('market/<int:pk>/',get_market, name="market_detail"),
    path('new_market/',add_new_market, name="new_market"),
    path('update_market/<int:pk>/',update_market, name="update_market"),
    path('update_market_partially/<int:pk>/',update_market_partially, name="update_market_partially"),
    path('delete_market/<int:pk>/',delete_market, name="delete_market"),
    path('persons/',PersonView.as_view(),name="all_persons"),
    path('persons_detail/<int:pk>/',PersonDetailView.as_view(),name="detail_persons"),
    path('aadhar/<int:pk>/',AadharView.as_view(),name="aadhar_data"),
    path('aadhar/',AadharViewList.as_view(),name="aadhar_all_data"),
    path('artist/<int:pk>/',ArtistView.as_view(),name='artists'),
    path('artist_create/<int:pk>/',ArtistCreateView.as_view(),name='artist-create'),
    path('song/<int:pk>/',SongView.as_view(),name='songs'),
    path('song_create/',SongCreateView.as_view(),name='song-create'),
    path('student/<int:pk>/',StudentView.as_view(),name="student"),
    path('student_create/',StudentCreateView.as_view(),name="student-create"),
    path('course/<int:pk>/',CourseView.as_view(),name="course"),
    path('course_create/',CourseCreateView.as_view(),name="course-create"),
    path('forests/',ForestView.as_view(),name="all-forests"),
    path('forests-detail/<int:pk>/',ForestDetailView.as_view(),name="detail-forests"),
]
