from django.db import models
from django.db import models
from django.utils import timezone



# Tabela Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


# Tabela Fornecedor
class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


# Tabela Departamento
class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


# Tabela Bem
class Bem(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    rfid = models.CharField(max_length=100, unique=True)  # RFID como o único identificador
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_aquisicao = models.DateField() 
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('em manutenção', 'Em Manutenção'), ('inativo', 'Inativo')], default='ativo')

    def __str__(self):
        return f'{self.nome} ({self.rfid})'  # Usando RFID no lugar do número de série
    

class Movimentacao(models.Model):
    TIPOS_MOVIMENTACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE)  # Relacionamento com Bem
    tipo = models.CharField(max_length=7, choices=TIPOS_MOVIMENTACAO)
    rfid = models.CharField(max_length=255)
    data = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Validação para garantir que o RFID da movimentação corresponda ao RFID do bem
        if self.bem.rfid != self.rfid:
            raise ValueError("O RFID da movimentação não corresponde ao RFID do bem.")
        super().save(*args, **kwargs)

