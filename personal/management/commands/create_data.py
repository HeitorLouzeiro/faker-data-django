# create_data.py
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from personal.models import Person
from personal.utils.progress_bar import progressbar

local = ['pt_BR']
fake = Faker(local)


def gen_email(first_name: str, last_name: str):
    first_name = slugify(first_name)
    last_name = slugify(last_name)
    email = f'{first_name}.{last_name}@email.com'
    return email


def get_person():
    first_name = fake.first_name()
    last_name = fake.first_name()
    email = gen_email(first_name, last_name)
    bio = fake.paragraph(nb_sentences=5)
    birthday = fake.date()
    data = dict(
        first_name=first_name,
        last_name=last_name,
        email=email,
        bio=bio,
        birthday=birthday,
    )
    return data


def create_persons():
    aux_list = []
    for _ in progressbar(range(10), 'Persons'):
        data = get_person()
        obj = Person(**data)
        aux_list.append(obj)
    Person.objects.bulk_create(aux_list)


class Command(BaseCommand):
    help = 'Create data.'

    def handle(self, *args, **options):
        create_persons()
