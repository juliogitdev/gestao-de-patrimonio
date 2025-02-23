# Sistema de Gestão de Patrimônio

Este projeto é um sistema de gestão de patrimônio desenvolvido em Django. Ele permite o cadastro, consulta, atualização e exclusão de bens, além de gerenciar movimentações de bens, categorias, fornecedores e departamentos. O sistema também possui funcionalidades para rastreamento de ativos utilizando RFID e geração de relatórios sobre o desempenho dos bens.

## Funcionalidades

- **Cadastro e gerenciamento de bens**: Adicionar, editar, excluir e visualizar bens do patrimônio.
- **Movimentação de bens**: Registrar movimentações dos bens e acompanhar o status de cada ativo.
- **Categorias**: Gerenciar categorias para classificar os bens.
- **Fornecedores**: Cadastrar e gerenciar fornecedores de bens.
- **Relatórios**: Gerar relatórios detalhados sobre o patrimônio e movimentações.
- **Dashboard**: Exibir indicadores de desempenho como o número de bens, bens em manutenção, e movimentações recentes.

## Requisitos

- Python 3.x
- Django 4.x
- Banco de dados (pode ser SQLite para desenvolvimento)
- Sistema operacional: Linux, macOS ou Windows

## Instalação

### 1. Clonar o repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/juliogitdev/gestao-de-patrimonio
```
2. Instalar dependências
Após clonar o repositório, entre no diretório do projeto e instale as dependências necessárias com o pip:
```bash
cd nome-do-repositorio
pip install -r requirements.txt
```
3. Migrate para o banco de dados
Depois de instalar as dependências, execute as migrações do banco de dados para criar as tabelas necessárias:
```bash
python manage.py migrate
```
4. Criar um superusuário
Para acessar o painel administrativo do Django, crie um superusuário com o seguinte comando:
```bash
python manage.py createsuperuser
```
5. Iniciar o servidor de desenvolvimento
Agora, você pode iniciar o servidor de desenvolvimento para testar o sistema:
```bash
python manage.py runserver
```
O servidor estará rodando em http://127.0.0.1:8000/ por padrão. Acesse o painel administrativo em http://127.0.0.1:8000/admin/ para gerenciar os dados do sistema.

Como Usar
1. Acessar o Sistema
Após iniciar o servidor, acesse a URL http://127.0.0.1:8000/ no seu navegador. O sistema estará disponível na interface principal, onde você pode visualizar os dados cadastrados.

2. Cadastro de Bens
No painel de administração ou na interface de usuário, vá até a seção de Bens. Nela, você pode adicionar, editar ou excluir bens do patrimônio. Cada bem pode ser categorizado e associado a um fornecedor e a um departamento.

3. Movimentações de Bens
A movimentação de bens é registrada automaticamente no sistema, podendo ser associada a um tipo (exemplo: entrada ou saída), data e hora. Isso permite um rastreamento completo dos bens.

4. Relatórios
A partir do dashboard, você pode gerar relatórios sobre os bens cadastrados, bens em manutenção, movimentações e fornecedores. Esses relatórios podem ser usados para análise e gestão do patrimônio.

5. Visualização de Estatísticas
O sistema exibe em tempo real indicadores de desempenho, como o total de bens cadastrados, número de bens em manutenção e outras métricas.






