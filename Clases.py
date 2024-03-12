from datetime import datetime 
import convert

def file_log(func):
    def wrapper(*args, **kwargs):
        file_name = 'activity.log'
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"{timestamp} - User saved\n"
        func(*args, **kwargs)
        try:
            convert.read(file_name)
        except FileNotFoundError:
            convert.create(file_name, content)
        else:
            convert.update(file_name, content)
    return wrapper

def console_log(func):
    def wrapper(*args,**kwargs):
        instance = args[0]
        func(*args,**kwargs)
        print(f'{instance.__class__} saved')
    return wrapper

def save_data(file_name,data):
        try:
            convert.read(file_name)
        except FileNotFoundError:
            convert.create(file_name,data)
            return data
        convert.update(file_name,data)
        return data

class User:

    class_name = 'User'
    def __init__(
        self, first_name, last_name, username, password,age
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.age = age

    def as_dict(self):
        return {
        'first_name' : self.first_name,
        'last_name' : self.last_name,
        'username' : self.username,
        'password' : self.password,
        'age' : self.age
        }
    
    def __str__(self) ->str:
        return f'{self.first_name}{self.last_name}'

    @file_log
    @console_log
    def save(self):
        file_name = 'users.json'
        return save_data(file_name,self.__dict__)
        
    
    def raise_age(self):
        self.age+=1

    def saludar(self):
        print(f"Hola, mi nombre es: {self.first_name}")

class Post:

    class_name = 'User'

    def __init__(self, author, date_posted, location, modify=False, delete = False ) -> None:
        self.author = author
        self.date_posted = date_posted
        self.location = location
        self.delete = delete
        self.modify = modify

    def as_dict(self):
        return {
        'author' : self.author,
        'date_posted' : self.date_posted,
        'location' : self.location,
        'delete' : self.delete,
        'modify' : self.modify,
        }
    @file_log
    @console_log
    def save(self):
        Post = self.as_dict()
        json_Post= convert.create('Post.json',Post)
        return json_Post
    
class Article:

    class_name = 'User'

    def __init__(self, title, author,content, date_published, category,views) -> None:
        self.title = title
        self.author = author
        self.content = content
        self.date_published = date_published
        self.category = category
        self.views = views
    
    def as_dict(self):
        return {
        'title' : self.title,
        'author' : self.author,
        'content' : self.content,
        'date_published' : self.date_published,
        'category':self.category,
        'views' : self.views
        }
    
    def save(self):
        Article = self.as_dict()
        json_Article = convert.create('Article.json',Article)
        return json_Article



hugo = User("Hugo", "Lozano","El karakuri",123,24)
hugo = hugo.save()

# user1= User('user1','apellido_user1','apodo,user1',12342,34)
# user1= user1.save()
hugo_post = Post('Hugo','2004/03/04','México')
hugo_post = hugo_post.save()

# hugo_Article = Article('Titulo del artículo','Hugo','Contenido del artículo','2004/03/04','Todas las categorías',0)
# hugo_Article = hugo_Article.save()