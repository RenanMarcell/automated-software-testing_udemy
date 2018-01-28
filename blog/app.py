from blog import Blog
from post import Post

MENU_PROMPT = 'Enter (c) to create a blog, (l) to list blogs, (r) to read a blog,'
' (p) to create a post or (q) to quit: \n'
blogs = dict()


def menu():
    # Show the user the avaliables blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit
    print_blogs()
    option = input(MENU_PROMPT).lower()
    while option != 'q':
        if option == 'c':
            ask_create_blog()
        elif option == 'l':
            print_blogs()
        elif option == 'r':
            ask_read_blog()
        elif option == 'p':
            ask_create_post()
        option = input(MENU_PROMPT).lower()

    pass


def ask_create_blog():
    blog_title = input('Digite o nome do novo blog: \n')
    blog_author = input('Digite o nome do autor do blog: \n')
    new_blog = Blog(blog_title, blog_author)
    if blog_title not in blogs.keys():
        blogs[blog_title] = new_blog
    else:
        print('Já existe um blog com este titulo')


def ask_read_blog():
    print_blogs()
    opcao = input("Qual blog deseja ler?\n")
    if opcao in blogs.keys():
        for post in blogs[opcao].posts:
            print('{}\n{}'.format(post.title, post.content))
    else:
        print("Esse blog não existe")


def ask_create_post():
    post_title = input('Digite o nome do novo post: \n')
    post_content = input('Digite o conteudo: \n')
    print_blogs()
    chosen_blog = input("Digite o blog a ser adicionado o post:\n")
    if chosen_blog in blogs.keys():
        blogs[chosen_blog].create_post(post_title, post_content)
    else:
        print('Blog não existente')


def print_blogs():
    # Print the avaliable blogs
    for key, value in blogs.items():
        print('- {}'.format(value))


print_blogs()
