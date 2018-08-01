from django.db import models


class Categorias(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class Movel(models.Model):
    titulo = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='moveis/', default='http://foo')
    criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'Movel(titulo={self.titulo!r}, preco={self.preco!r}, descricao={self.descricao!r})'
