import factory

class UserFactory(factory.django.DjangoModelFactory):
	first_name = "test",
	last_name = "test",
	username = "john",
	email = "j@test.ru",
	password = "12345",
	birth_date = factory.Faker('date_object')

	class Meta:
		model = "users.User"


class SelectionFactory(factory.django.DjangoModelFactory):
	name = "test_name"
	owner = factory.SubFactory(UserFactory)

	class Meta:
		model = "ads.Selection"

class AdFactory(factory.django.DjangoModelFactory):
	name = "Ad"
	author = factory.SubFactory(UserFactory)
	price = 1

	class Meta:
		model = "ads.Ad"
