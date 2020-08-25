#!python
def tag(tag, *args, **kwargs):
    return f'<{tag}> </{tag}>'


if __name__ == "__main__":
    html = tag('p',
               tag('span', 'Curso de Python 3, por '),
               tag('strong', 'Juracy Filho', id='jf'),
               tag('span', ' e '),
               tag('strong', 'Leonardo Leitão', id='ll'),
               tag('span', '.'),
               css='alert')

    print(html)
