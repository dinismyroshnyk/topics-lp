# Documentação para a Aplicação Django

## VIEWS.PY

Este ficheiro contém as views para a aplicação Django. As views são responsáveis por gerir a lógica da aplicação e devolver as respostas apropriadas ao utilizador.

### Index View
A index view gere a exibição da página principal da aplicação.

### Detail View
A detail view gere a exibição de informações detalhadas para um item específico.

### Create View
A create view gere a criação de novos itens na aplicação.

### Update View
A update view gere a atualização de itens existentes na aplicação.

### Delete View
A delete view gere a eliminação de itens da aplicação.

## MODELS.PY

Este ficheiro contém os modelos para a aplicação Django. Os modelos definem a estrutura da base de dados e as relações entre diferentes peças de dados.

### Item Model
O item model define a estrutura dos itens na aplicação, incluindo campos como nome, descrição e preço.

## FORMS.PY

Este ficheiro contém os formulários para a aplicação Django. Os formulários são usados para gerir a entrada do utilizador e validar os dados antes de serem guardados na base de dados.

### ItemForm
O ItemForm é usado para criar e atualizar itens na aplicação.

## URLS.PY

Este ficheiro contém as configurações de URL para a aplicação Django. As URLs definem as diferentes rotas que os utilizadores podem seguir dentro da aplicação.

### Index URL
A index URL direciona para a index view.

### Detail URL
A detail URL direciona para a detail view de um item específico.

### Create URL
A create URL direciona para a create view.

### Update URL
A update URL direciona para a update view de um item específico.

### Delete URL
A delete URL direciona para a delete view de um item específico.

## SETTINGS.PY

Este ficheiro contém as configurações para a aplicação Django. As configurações definem a configuração da aplicação, incluindo configurações da base de dados, apps instaladas e middleware.

### Configurações da Base de Dados
As configurações da base de dados definem a configuração para a base de dados usada pela aplicação.

### Apps Instaladas
A secção de apps instaladas lista as apps que estão instaladas e usadas pela aplicação.

### Middleware
A secção de middleware lista o middleware que é usado pela aplicação.

## README.MD

Este ficheiro contém a documentação para a aplicação Django. Fornece uma visão geral da aplicação e explica como configurá-la e usá-la.

### Configuração
Para configurar a aplicação, siga estes passos:
1. Instale as dependências necessárias.
2. Configure as definições da base de dados em `settings.py`.
3. Execute as migrações da base de dados.
4. Inicie o servidor de desenvolvimento.

### Utilização
Para usar a aplicação, siga estes passos:
1. Navegue até à página principal da aplicação.
2. Use os links de navegação para aceder a diferentes partes da aplicação.
3. Use os formulários para criar, atualizar e eliminar itens na aplicação.

### Contribuição
Para contribuir para a aplicação, siga estes passos:
1. Faça um fork do repositório.
2. Crie um novo branch para as suas alterações.
3. Faça as suas alterações e faça commit delas.
4. Envie as suas alterações para o seu fork.
5. Crie um pull request para fundir as suas alterações no repositório principal.

### Licença
Esta aplicação está licenciada sob a Licença MIT.
