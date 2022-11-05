from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Market, Person, Aadhar, Song, Artist, Student, Course, House, Movie, Game, Phone, Forest


class MarketSerializer(ModelSerializer):

    class Meta:
        model = Market
        fields = "__all__"


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class AadharSerializer(ModelSerializer):

    person = PersonSerializer()

    class Meta:
        model = Aadhar
        fields = ('id','aadhar_number','person')


class SongSerializer(ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Song
        fields = ('id', 'name','artist')


class ArtistSerializer(ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'songs')


class CourseSerializer(ModelSerializer):

    student = serializers.SlugRelatedField(many=True, read_only=True, slug_field="stu_name")

    class Meta:
        model = Course
        fields = ('id','course_name','student')
        extra_kwargs = {'student': {'required': False}}


class StudentSerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id','stu_name','stu_age','courses')
        extra_kwargs = {'courses': {'required': False}}


class HouseSerializer(ModelSerializer):

    class Meta:
        model = House
        fields = "__all__"


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class GameSerializer(ModelSerializer):

    class Meta:
        model = Game
        fields = "__all__"


class PhoneSerializer(ModelSerializer):

    class Meta:
        model = Phone
        fields = "__all__"


class ForestSerializer(ModelSerializer):

    class Meta:
        model = Forest
        fields = "__all__"









