from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Fornecedor, Departamento, Bem, Movimentacao
from .forms import CategoriaForm, FornecedorForm, DepartamentoForm, BemForm, MovimentacaoForm
import datetime
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
            return redirect('listar_bens')
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
            return redirect('listar_bens')
    else:
        form = BemForm(instance=bem)
    return render(request, 'bens/atualizar_bem.html', {'form': form})

# Deletar um bem
def deletar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)
    if request.method == 'POST':
        bem.delete()
        return redirect('listar_bens')
    return render(request, 'bens/deletar_bem.html', {'bem': bem})

def registrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a movimentação no banco de dados
            return redirect('lista_movimentacoes')  # Redireciona para a lista de movimentações
    else:
        form = MovimentacaoForm()

    return render(request, 'bens/registrar_movimentacao.html', {'form': form})


def dashboard(request):
    # Exemplificando como obter dados para o dashboard
    total_ativos = Bem.objects.filter(status='ativo').count()
    total_inativos = Bem.objects.filter(status='inativo').count()
    total_manutencao = Bem.objects.filter(status='em manutenção').count()
    total_movimentacoes = Movimentacao.objects.count()

    return render(request, 'bens/dashboard.html', {
        'total_ativos': total_ativos,
        'total_inativos': total_inativos,
        'total_manutencao': total_manutencao,
        'total_movimentacoes': total_movimentacoes,
    })

def relatorio(request):
    bens = Bem.objects.all()
    return render(request, 'bens/relatorio.html', {'bens': bens})

def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data')
    return render(request, 'bens/lista_movimentacoes.html', {'movimentacoes': movimentacoes})

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