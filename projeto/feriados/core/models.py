from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado',max_length=50)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')
    modificado_em = models.DateTimeField( verbose_name='modificado em', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Feriado'
        verbose_name_plural = 'Feriados'
        ordering = ('mes', '-dia')