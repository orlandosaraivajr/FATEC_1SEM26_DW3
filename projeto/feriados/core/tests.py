from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Feriados')
        

from core.models import FeriadoModel
from datetime import datetime
class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome=self.feriado,
            dia=self.dia,   
            mes=self.mes,
    )
        self.cadastro.save()
    
    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())
    
    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)
    
    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)
    
    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)
    
from core.forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='dia de são nunca')
        self.assertEqual('DIA DE SÃO NUNCA', form.cleaned_data['nome'])
    
    def test_wrong_day(self):
        form = self.make_validated_form(dia=39)
        msg_erro = form.errors.get('dia')[0]
        self.assertEqual(msg_erro, 'Dia precisa ser entre 1 e 31')
        
    def make_validated_form(self, **kwargs):
        valid = dict(
            nome='Tiradentes',
            dia=14,
            mes=4
        )
        data = dict(valid, **kwargs)
        form = FeriadoForm(data)
        form.is_valid()
        return form

from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from core.models import FeriadoModel

class FeriadoAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Cria um usuário e token (caso use autenticação)
        self.user = User.objects.create_user(username='admin', password='123')
        self.client.force_authenticate(user=self.user)
        self.feriado = FeriadoModel.objects.create(nome="Natal", dia=25, mes=12)

    def test_listar_feriados(self):
        url = reverse('api_feriados_list_create') # Ex: 'api/feriados/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)