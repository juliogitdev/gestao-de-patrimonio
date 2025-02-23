from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Fornecedor, Departamento, Bem, Movimentacao
from .forms import CategoriaForm, FornecedorForm, DepartamentoForm, BemForm, MovimentacaoForm
from datetime import timedelta
from django.utils import timezone


# View para exibir informações gerais sobre o sistema
def inicio(request):
    total_bens = Bem.objects.count()  # Total de bens cadastrados
    
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

    # Passando as informações para o template
    contexto = {
        'patrimonio_total': total_bens,
        'bens_em_manutencao': bens_em_manutencao,
        'bens_movimentados_recentemente': len(movimentacoes_recent),
        'total_movimentacoes': total_movimentacoes,
        'total_fornecedores': total_fornecedores,
        'total_categorias': total_categorias,
        'movimentacoes_recent': movimentacoes_recent,
    }

    return render(request, 'inicio.html', contexto)


# Listar todos os bens cadastrados no sistema
def listar_bens(request):
    bens = Bem.objects.all()  # Obtendo todos os bens
    return render(request, 'bens/listar_bens.html', {'bens': bens})


# Criar um novo bem no sistema
def criar_bem(request):
    if request.method == 'POST':
        form = BemForm(request.POST)  # Instanciando o formulário com os dados recebidos
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando o novo bem no banco de dados
            return redirect('bens')  # Redireciona para a lista de bens
        else:
            print(form.errors)  # Imprime os erros no terminal caso o formulário seja inválido
            return render(request, 'bens/criar_bem.html', {'form': form})
    else:
        form = BemForm()  # Instanciando um formulário vazio
    return render(request, 'bens/criar_bem.html', {'form': form})


# Exibir detalhes de um bem específico
def detalhar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)  # Obtendo o bem pelo ID
    return render(request, 'bens/detalhar_bem.html', {'bem': bem})


# Atualizar os dados de um bem existente
def atualizar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)  # Obtendo o bem pelo ID
    if request.method == 'POST':
        form = BemForm(request.POST, instance=bem)  # Instanciando o formulário com os dados do bem
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando as alterações
            return redirect('bens')  # Redireciona para a lista de bens
    else:
        form = BemForm(instance=bem)  # Instanciando o formulário com os dados do bem para edição
    return render(request, 'bens/atualizar_bem.html', {'form': form})


# Deletar um bem do sistema
def deletar_bem(request, pk):
    bem = get_object_or_404(Bem, pk=pk)  # Obtendo o bem pelo ID
    if request.method == 'POST':
        bem.delete()  # Deletando o bem
        return redirect('bens')  # Redireciona para a lista de bens
    return render(request, 'bens/deletar_bem.html', {'bem': bem})


# Registrar uma movimentação de um bem
def registrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)  # Instanciando o formulário com os dados da movimentação
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando a movimentação no banco de dados
            return redirect('inicio')  # Redireciona para a página inicial
    else:
        form = MovimentacaoForm()  # Instanciando um formulário vazio
    return render(request, 'bens/registrar_movimentacao.html', {'form': form})


# Exibir um relatório com todos os bens cadastrados
def relatorio(request):
    bens = Bem.objects.all()  # Obtendo todos os bens
    return render(request, 'bens/relatorio.html', {'bens': bens})


# Lista todas as movimentações com a opção de filtrar por RFID
def lista_movimentacoes(request):
    rfid = request.GET.get('rfid', '')  # Obtendo o RFID da URL (se houver)
    
    # Filtrando as movimentações com base no RFID (caso fornecido)
    if rfid:
        movimentacoes = Movimentacao.objects.filter(rfid__icontains=rfid)
    else:
        movimentacoes = Movimentacao.objects.all()  # Obtendo todas as movimentações
    
    return render(request, 'bens/listar_movimentacoes.html', {'movimentacoes': movimentacoes})


# Listar todos os fornecedores cadastrados no sistema
def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()  # Obtendo todos os fornecedores
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})


# Adicionar um novo fornecedor
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)  # Instanciando o formulário com os dados recebidos
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando o novo fornecedor no banco de dados
            return redirect('lista_fornecedores')  # Redireciona para a lista de fornecedores
    else:
        form = FornecedorForm()  # Instanciando um formulário vazio
    return render(request, 'fornecedores/form_fornecedor.html', {'form': form})


# Editar um fornecedor existente
def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)  # Obtendo o fornecedor pelo ID
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)  # Instanciando o formulário com os dados do fornecedor
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando as alterações
            return redirect('lista_fornecedores')  # Redireciona para a lista de fornecedores
    else:
        form = FornecedorForm(instance=fornecedor)  # Instanciando o formulário com os dados do fornecedor para edição
    return render(request, 'fornecedores/form_fornecedor.html', {'form': form})


# Excluir um fornecedor do sistema
def excluir_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)  # Obtendo o fornecedor pelo ID
    if request.method == 'POST':
        fornecedor.delete()  # Deletando o fornecedor
        return redirect('lista_fornecedores')  # Redireciona para a lista de fornecedores
    return render(request, 'fornecedores/confirmar_exclusao_fornecedor.html', {'fornecedor': fornecedor})


# Listar todas as categorias cadastradas no sistema
def lista_categorias(request):
    categorias = Categoria.objects.all()  # Obtendo todas as categorias
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})


# Adicionar uma nova categoria
def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)  # Instanciando o formulário com os dados recebidos
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando a nova categoria no banco de dados
            return redirect('lista_categorias')  # Redireciona para a lista de categorias
    else:
        form = CategoriaForm()  # Instanciando um formulário vazio
    return render(request, 'categorias/form_categoria.html', {'form': form})


# Editar uma categoria existente
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)  # Obtendo a categoria pelo ID
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)  # Instanciando o formulário com os dados da categoria
        if form.is_valid():  # Validando o formulário
            form.save()  # Salvando as alterações
            return redirect('lista_categorias')  # Redireciona para a lista de categorias
    else:
        form = CategoriaForm(instance=categoria)  # Instanciando o formulário com os dados da categoria para edição
    return render(request, 'categorias/form_categoria.html', {'form': form})


# Excluir uma categoria do sistema
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)  # Obtendo a categoria pelo ID
    if request.method == 'POST':
        categoria.delete()  # Deletando a categoria
        return redirect('lista_categorias')  # Redireciona para a lista de categorias
    return render(request, 'categorias/confirmar_exclusao_categoria.html', {'categoria': categoria})
