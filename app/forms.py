from django.forms import ModelForm
from app.models import Filmes

class FilmesForms(ModelForm):
    class Meta:
        model = Filmes
        fields = ['filme', 'genero', 'duracao', 'data_lancamento', 'diretor', 'principais_artistas']