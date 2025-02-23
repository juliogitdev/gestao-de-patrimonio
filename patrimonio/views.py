from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Fornecedor, Departamento, Bem, Movimentacao
from .forms import CategoriaForm, FornecedorForm, DepartamentoForm, BemForm, MovimentacaoForm
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum


def inicio(request):
    total_bens = Bem.objects.count()

    patrimonio_total = Bem.objects.aggregate(Sum('valor'))['valor__sum'] or 0  # Calculando o total do patrimônio
    
    # Consultando bens em manutenção
    bens_em_manutencao = Bem.objects.filter(status='em manutenção').count()
    
    # Consultando bens recentemente movimentados (últimos 7 dias)
    movimentacoes_recent = Movimentacao.objects.filter(data__gte=timezone.now() - timedelta(days=7))
    
    # Consultando total de movimentações
    total_movimentacoes = Movimentacao.objects.count()
    
    # Consultando fornecedores cadastrados
    total_fornecedores = Fornecedor.objects.count()
    
    # Consultando categorias de bens
    total_categorias = Categoria.objects.count()

    contexto = {
        'patrimonio_total': patrimonio_total,
        'total_bens': total_bens,
        'bens_em_manutencao': bens_em_manutencao,
        'bens_movimentados_recentemente': len(movimentacoes_recent),
        'total_movimentacoes': total_movimentacoes,
        'total_fornecedores': total_fornecedores,
        'total_categorias': total_categorias,
        'movimentacoes_recent': movimentacoes_recent,
    }

    return render(request, 'inicio.html', contexto)

# Listar todos os bens
def listar_bens(request):
    bens = Bem.objects.all()
    return render(request, 'bens/listar_bens.html', {'bens': bens})

# Criar um novo bem
def criar_bem(request):
    if request.method == 'POST':
        form = BemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bens')
        else:
            print(form.errors)  # Imprime os erros no terminal
            return render(request, 'bens/criar_bem.html', {'form': form})
    else:
        form = BemForm()
    return render(request, 'bens/criar_bem.html', {'form': form})
    

# Detalhar um bem
def detalhar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)
    return render(request, 'bens/detalhar_bem.html', {'bem': bem})

# Atualizar um bem
def atualizar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)
    if request.method == 'POST':
        form = BemForm(request.POST, instance=bem)
        if form.is_valid():
            form.save()
            return redirect('bens')
    else:
        form = BemForm(instance=bem)
    return render(request, 'bens/atualizar_bem.html', {'form': form})

# Deletar um bem
def deletar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)
    if request.method == 'POST':
        bem.delete()
        return redirect('bens')
    return render(request, 'bens/deletar_bem.html', {'bem': bem})

def registrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a movimentação no banco de dados
            return redirect('inicio') 
    else:
        form = MovimentacaoForm()

    return render(request, 'bens/registrar_movimentacao.html', {'form': form})



def relatorio(request):
    bens = Bem.objects.all()
    return render(request, 'bens/relatorio.html', {'bens': bens})

def lista_movimentacoes(request):
       # Captura o RFID do parâmetro de consulta
    rfid = request.GET.get('rfid', '')

    # Filtra as movimentações com base no RFID (caso fornecido)
    if rfid:
        movimentacoes = Movimentacao.objects.filter(rfid__icontains=rfid)
    else:
        movimentacoes = Movimentacao.objects.all()

    return render(request, 'bens/listar_movimentacoes.html', {
        'movimentacoes': movimentacoes
    })

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/form_fornecedor.html', {'form': form})

def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/form_fornecedor.html', {'form': form})

def excluir_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('lista_fornecedores')
    return render(request, 'fornecedores/confirmar_exclusao_fornecedor.html', {'fornecedor': fornecedor})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/form_categoria.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/form_categoria.html', {'form': form})

def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias/confirmar_exclusao_categoria.html', {'categoria': categoria})

# Listar todos os departamentos
def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/listar_departamentos.html', {'departamentos': departamentos})

# Adicionar um novo departamento
def adicionar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'departamentos/form_departamento.html', {'form': form})

# Editar um departamento existente
def editar_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departamentos/form_departamento.html', {'form': form})

# Excluir um departamento
def excluir_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar_departamentos')
    return render(request, 'departamentos/confirmar_exclusao_departamento.html', {'departamento': departamento})