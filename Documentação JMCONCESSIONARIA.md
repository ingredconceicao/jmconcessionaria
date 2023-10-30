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
**2. Configuração do MySql**
Para utilizar o Mysql em seu computador siga os passos para configurar um novo usuario e migrar o banco de dados

**2.1** Primeiramente execute o sistema Django utilizando o seguinte comando:  

```python
python manage.py runserver
```
De inicio o sistema irá dar erro porém apresentará o nome de usuario do seu computador da seguinte forma: 

![image](https://github.com/ingredconceicao/jmconcessionaria/assets/111439073/35fd265a-742d-4685-a87f-ceca1b6e0073)


**2.2** Copie este nome de usuário, abra a pasta **projectConcessionaria** e procure o arquivo **settings.py**

![image](https://github.com/ingredconceicao/jmconcessionaria/assets/111439073/90ebb7d2-66bb-491b-a9b7-eb5fd6b5942e)


**2.3** Procure o local onde é feio  a configuração do DATABASE:

![image](https://github.com/ingredconceicao/jmconcessionaria/assets/111439073/2b46b96f-1375-47aa-9690-f19382caf968)


**2.4** Crie um novo elif utilizando o nome de usuario disponibilizado anteriormente, altere o 'USER' e 'PASSWORD' de acordo a configuração do 
seu MySQL:

![image](https://github.com/ingredconceicao/jmconcessionaria/assets/111439073/0c9fa691-c4d3-41bb-a8a5-3d142fa61f1d)  


**2.5** Após isso abra o seu Mysql acesso a conexão que foi adicionada na configuração do Elif.

**2.6** Crie o novo banco de dados chamado **db_concessionaria**

![image](https://github.com/ingredconceicao/jmconcessionaria/assets/111439073/afb4130e-11bb-47b3-b472-42aa3adb78fd)



**2.7** Após isso volte ao  terminal do Django e utilize o seguinte comando para exportar as tabelas do Django para o MySQL:
```python
python manage.py migrate
```

![image](https://github.com/ingredconceicao/jmconcessionaria/assets/111439073/7bf1848f-ea46-41e1-8b15-071ae8853711)


**2.8** Após isso execute o sistema normalmente utilizando: 
```python
python manage.py runserver
```





      
      
      
