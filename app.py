# import cgi

# form = b'''
# <html>
#     <head>
#         <title>Hello User!</title>
#     </head>
#     <body>
#         <form method="post">
#             <label>Hello</label>
#             <input type="text" name="name">
#             <input type="submit" value="Go">
#         </form>
#     </body>
# </html>
# '''

# def app(environ, start_response):
#     html = form

#     if environ['REQUEST_METHOD'] == 'POST':
        # post_env = environ.copy()
        # post_env['QUERY_STRING'] = ''
        # post = cgi.FieldStorage(
        #     fp=environ['wsgi.input'],
        #     environ=post_env,
        #     keep_blank_values=True
        # )
#         html = b'Hello, ' + post['name'].value + '!'

#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [html]

# if __name__ == '__main__':
#     try:
#         from wsgiref.simple_server import make_server
#         httpd = make_server('', 8080, app)
#         print('Serving on port 8080...')
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print('Goodbye.')

import cgi

class User():
    def __init__(self,_id,_name):
        self.id=_id
        self.name=_name

users=[

]

def render_template(template_name='index.html', context={}):
    html_str = ""
    with open(template_name, 'r') as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str

def home(environ):
    return render_template(
        template_name='index.html', 
        context={}
    )

def contact_us(environ):
    return render_template(
        template_name='contact.html', 
        context={}
    )

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    print(path)
    # form = cgi.FieldStorage()
    # name = environ.get("PATH_INFO")
    # print(name)
    if path.endswith("/"):
        path = path[:-1]

    if path == "": 
        
        data = home(environ)
        if path != "":
            path = environ.get("PATH_INFO")[12:]
            print(path)
    else:
        data = render_template(template_name="contact.html",context={"path": path})
    # else:
    #     data = render_template(template_name='404.html', context={"path": path})
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])



from urllib.parse import urlparse
from urllib.parse import parse_qs

url = 'http://localhost:8080/app.py?name=salam'
parsed_url = urlparse(url)
captured_value = parse_qs(parsed_url.query)['name'][0]

print(captured_value)

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')



