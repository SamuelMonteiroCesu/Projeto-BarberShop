from django.test import TestCase
import unittest
from validate_docbr import CPF
from rest_framework.response import Response
from models import Client
from geradores import create
import pytest

class test_cliente(unittest.TestCase):

def test_cadastro() :   
    create() 
    self.assertEqual(self.create,'200: CLIENT CREATED')

