#coding: utf-8

from django.core.management.base import BaseCommand
from streams.ws import start_tornado

class Command(BaseCommand):
    help = 'builds a category tree'

    def handle(self, *args, **options):
           start_tornado(9002)
