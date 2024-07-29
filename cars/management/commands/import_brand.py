import csv
from django.core.management.base import BaseCommand

from cars.models import Brand


class Command(BaseCommand):
    help = 'Comando para importar lista de marcas.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Nome do arquivo CSV na raiz do projeto.')

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']

                self.stdout.write(self.style.NOTICE(name))

                Brand.objects.create(name=name)

            self.stdout.write(self.style.SUCCESS('MARCAS CADASTRADAS COM SUCESSO!!'))
