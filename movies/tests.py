from django.test import TestCase
from .models import Show,Category,Actor

class ShowTest(TestCase):
    @classmethod
    def setUp_test_data(cls):
        Category.objects.create(
            title = 'ctg1',
            image = ''
        )
        Actor.objects.create(
            name = 'actor1',
            age = 25,
            gender = 'Female', 
            image = ''
        )
        Show.objects.create(
            user = 'admin',
            title = 'movie 1 ',
            description = 'descriptiondescriptiondescription', 
            rating = '2',
            type = 'Movie',
            category = 'ctg1',
            main_actor = 'actor1',
            sub_actor = 'actor1',
            image = ''
        )

    def check_title_max_length(self):
        show = Show.objects.get(id=1)
        field = show._meta.get_field('title').max_length
        TestCase.assertEqual(field,100)

    def check_description_max_length(self):
        show = Show.objects.get(id=1)
        field = show._meta.get_field('description').max_length
        TestCase.assertEqual(field,5000)