from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Show,Category,Actor

class ShowTest(TestCase):
    @classmethod
    def setUp_test_data(cls):
        Category.objects.create(
            title = 'ctg1',
            image = SimpleUploadedFile(name='testImage',content=open('\Users\omarm\Pictures\New folder\Screenshot 2024-01-08 154625.png','rb').read(),content_type='image/png')
        )
        Actor.objects.create(
            name = 'actor1',
            age = 25,
            gender = 'Female', 
            image = SimpleUploadedFile(name='TestImage', content=open('\Users\omarm\Pictures\New folder\Screenshot 2024-01-08 154625.png','rb').read(), content_type='image/png')
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
            image = SimpleUploadedFile(name='TestImage', content=open('\Users\omarm\Pictures\New folder\Screenshot 2024-01-08 154625.png','rb').read(), content_type='image/png')
        )

    # Test Models
    def check_title_max_length(self):
        show = Show.objects.get(id=1)
        field = show._meta.get_field('title').max_length
        TestCase.assertEqual(field,100)

    def check_description_max_length(self):
        show = Show.objects.get(id=1)
        field = show._meta.get_field('description').max_length
        TestCase.assertEqual(field,5000)

    # Test Views
    def check_view_url_exists_at_desired_location(self):
        url = self.client.get('/movie/viewSet/')
        TestCase.assertEqual(url.status_code, 200)
        