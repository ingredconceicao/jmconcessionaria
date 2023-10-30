**JM CONCESSIONARIA**

*Este Sistema formado em python com o auxilio do framework Django.  O Django proporciona um conjunto de bibliotecas que facilitam a criação e execução de atividades.*
*Ao criar projetos com Django utiliza-se uma divisão de estruturas Chamadas de **Project (Que tem como finalidade enblobar todos as camadas responsáveis para a execução do Django**
e também as **Aplicações (Estrururas plugáveis que formam o sistema**. Com isso é possivel criar um só projeto e inserir varias aplicações*

**1. Intalação de recursos**

**1.1** Ao clonar o repositorio e adiciona-lo na IDE, abra o terminal *Prompt Command* e insira o comando para ativar a Venv do JMCONCESSIONARIA
```cmd
.\venv\Scripts\activate
```
**1.2** Após isso utilize o comando para baixar todas as dependências do JMCONCESSIONARIA:
```cmd
pip install -r requirements.txt
```
**OBS:** Caso o requirements.txt não funcione baixe as dependências manualmente utilizando: 
```cmd
pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage MySQL
```
**2. Configuração do MySql** Para utilizar o Mysql em seu computador siga os passos para configurar um novo usuario e migrar o banco de dados

**2.1** Primeiramente execute o sistema Django utilizando o seguinte comando:  

```python
python manage.py runserver
```
De inicio o sistema irá dar erro porém apresentará o nome de usuario do seu computador da seguinte forma: 

      
      
      
