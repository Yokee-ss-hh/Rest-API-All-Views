from django.db import models


class Market(models.Model):

    market_name = models.CharField(max_length=200)
    market_place = models.CharField(max_length=200)

    def __str__(self):

        return self.market_name

    class Meta:

        verbose_name = "market data"
        db_table = "markettable"


# ----------------------------------------------------------------------------------------------------------------
# ---------------One To One relationship-----------------
# ---------------A person can have only 1 aadhar number , 1 aadhar number is related to 1 person-----------------

class Person(models.Model):

    person_name = models.CharField(max_length=300)
    person_age = models.IntegerField()

    def __str__(self):
        return self.person_name

    class Meta:

        db_table = 'persontable'


class Aadhar(models.Model):

    aadhar_number = models.IntegerField(unique=True)
    person = models.OneToOneField(to=Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.aadhar_number)

    class Meta:

        db_table = 'aadhartable'

# ----------------------------------------------------------------------------------------------------------------
# ---------------One To Many relationship-----------------
# -----A artist can write / sing many songs, each song is related to that particular artist
# -------------Unlike above example, Even though foriegnkey present in songs model,
# we are using songs serializer in artist serializer, so that particular artist can
# get all his songs when user access them-------------


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:

        db_table = "artisttable"


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:

        db_table = "songtable"


# --------------------many to many relationship---------------------------------
# 1 student can take many courses, 1 course can be taken by many students


class Student(models.Model):

    stu_name = models.CharField(max_length=300)
    stu_age = models.IntegerField()

    def __str__(self):
        return self.stu_name

    class Meta:

        db_table = "studenttable"


class Course(models.Model):

    course_name = models.CharField(max_length=300)
    student = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.course_name

    class Meta:

        db_table = "coursetable"

# -------------------------------------------------------------------------------
# -----------Simple model for viewsets.ViewSet ---------------------


class House(models.Model):

    house_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    banner_name = models.CharField(max_length=300)

    def __str__(self):
        return self.house_name

    class Meta:

        db_table = 'housemodel'

# -----------------------------------------------------------------------------------
# -----------Simple model for viewsets.GenericViewSet ---------------------


class Movie(models.Model):

    movie_name = models.CharField(max_length=300)
    movie_type = models.CharField(max_length=300)

    def __str__(self):
        return self.movie_name

    class Meta:

        db_table = 'movietable'


# -----------------------------------------------------------------------------------
# -----------Simple model for viewsets.ModelViewSet ---------------------


class Game(models.Model):

    game_name = models.CharField(max_length=200)
    game_rating = models.IntegerField(max_length=5)

    def __str__(self):
        return self.game_name

    class Meta:

        db_table = 'gametable'

# -----------------------------------------------------------------------------------
# -----------Simple model for viewsets.ReadOnlyViewSet ---------------------


class Phone(models.Model):

    phone_company = models.CharField(max_length=200)
    phone_color = models.CharField(max_length=200)

    def __str__(self):
        return self.phone_company

    class Meta:

        db_table = 'phonemodel'

# --------------------- model for GenericApiView ----------------------
# ---------Overriding methods in GenericApiView --------------


class Forest(models.Model):

    forest_name = models.CharField(max_length=100)
    forest_country = models.CharField(max_length=100)

    def __str__(self):
        return self.forest_name

    class Meta:

        db_table = 'foresttable'

