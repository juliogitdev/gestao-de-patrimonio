from django import forms
from .models import Categoria, Fornecedor, Departamento, Bem, Movimentacao
import re

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da categoria'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Digite a descrição...'}),
        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'endereco', 'telefone', 'email']

    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '[0-9]*'}),
        max_length=15,  # Limite de caracteres para o telefone
        error_messages={
            'invalid': 'Por favor, insira um número de telefone válido (somente números).'
        }
    )

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        # Verifica se o telefone contém apenas números
        if not re.match(r'^[0-9]+$', telefone):
            raise forms.ValidationError('O telefone deve conter apenas números.')
        return telefone

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'descricao']

class BemForm(forms.ModelForm):
    class Meta:
        model = Bem
        fields = ['nome', 'descricao', 'categoria', 'fornecedor', 'departamento', 'rfid', 'valor', 'data_aquisicao', 'status']

    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    data_aquisicao = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.SelectDateWidget(years=range(1900, 2100)))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=True)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=True)

    




class MovimentacaoForm(forms.ModelForm):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída')
    ]

    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tipo de Movimentação"
    )

    class Meta:
        model = Movimentacao
        fields = ['rfid', 'tipo']
        widgets = {
            'rfid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o código RFID'}),
        }


    def clean_rfid(self):
        rfid = self.cleaned_data['rfid']
        try:
            # Verifica se o RFID existe no banco de dados
            bem = Bem.objects.get(rfid=rfid)
        except Bem.DoesNotExist:
            raise forms.ValidationError('RFID não encontrado.')

        # Associando o objeto Bem ao campo 'bem'
        self.instance.bem = bem
        return rfid