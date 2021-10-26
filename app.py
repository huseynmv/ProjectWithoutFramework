import cgi

form = '''
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Bootstrap CSS -->
    <!-- https://cdnjs.com/libraries/twitter-bootstrap/5.0.0-beta1 -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.0.0-beta1/css/bootstrap.min.css"
    />

    <!-- Icons: https://getbootstrap.com/docs/5.0/extend/icons/ -->
    <!-- https://cdnjs.com/libraries/font-awesome -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"
    />

    <title>Hello, world!</title>
  </head>
  <body>
    <div class="container-fluid p-0">
        <div class="row">
            <div class="col">
                <form action="/contact" method='POST'>
                    <div class="mt-3">
                        <input type="text" class="form-control" placeholder="Ad" name='name'>
                        <input type="text" class="form-control mt-3" placeholder="Soyad" name='password'>
                        <input type="submit" class="btn btn-primary mt-4" value='Register'>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.0.0-beta1/js/bootstrap.bundle.min.js"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->

    <!-- https://cdnjs.com/libraries/popper.js/2.5.4 -->
    <!-- <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.5.4/umd/popper.min.js"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.0.0-beta1/js/bootstrap.min.js"
    ></script> -->

    <!-- More: https://getbootstrap.com/docs/5.0/getting-started/introduction/ -->
</body>
</html>
'''


def render_template(template_name='contact.html', context={}):
    # html_str = ""
    with open(template_name, 'r') as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str

def app(environ, start_response):
    html = form

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            # keep_blank_values=True
        )
        html = post['name'].value
        
        print(html)

    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [html]
    data =  render_template(template_name="contact.html",context={"path": html})
    data = data.encode()
    return [data]



if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        print("http://localhost:8080")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')


#-----------------------------------------


# import cgi

# class User():
#     def __init__(self,_id,_name):
#         self.id=_id
#         self.name=_name

# users=[

# ]



# def home(environ):
#     return render_template(
#         template_name='index.html', 
#         context={}
#     )

# def contact_us(environ):
#     return render_template(
#         template_name='contact.html', 
#         context={}
#     )

# def app(environ, start_response):
#     path = environ.get("PATH_INFO")
#     print(path)
#     # form = cgi.FieldStorage()
#     # name = environ.get("PATH_INFO")
#     # print(name)
#     if path.endswith("/"):
#         path = path[:-1]

#     if path == "": 
        
#         data = home(environ)
#         if path != "":
#             path = environ.get("PATH_INFO")[12:]
#             print(path)
#     else:
#         data = render_template(template_name="contact.html",context={"path": path})
#     data = data.encode("utf-8")
#     start_response(
#         f"200 OK", [
#             ("Content-Type", "text/html"),
#             ("Content-Length", str(len(data)))
#         ]
#     )
#     return iter([data])



# # from urllib.parse import urlparse
# # from urllib.parse import parse_qs

# # url = 'http://localhost:8080/app.py?name=salam'
# # parsed_url = urlparse(url)
# # captured_value = parse_qs(parsed_url.query)['name'][0]

# # print(captured_value)

# if __name__ == '__main__':
#     try:
#         from wsgiref.simple_server import make_server
#         httpd = make_server('', 8080, app)
#         print('Serving on port 8080...')
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print('Goodbye.')

#-----------------------------------------------------


# from wsgiref.simple_server import make_server
 
 
# def new():
#      ret_str = '<html><head></head><body><h1 style="color:blue;">liuhonglei is so handsome</h1></body></html>'
#      return [ret_str.encode('utf-8')]
 
 
# def index():
#      ret_str = '/index'
#      return [ret_str.encode('utf-8')]
 
 
# URLS = {
#      "/new": new,
#      "/index": index
#  }
 
 
# def RunServer(environ, start_response):
#      start_response('200 OK', [('Content-Type', 'text/html')])
#      url = environ['PATH_INFO']
#      if url in URLS.keys():
#          func_name = URLS[url]
#          ret = func_name()
#      else:
#          ret = '404'.encode('utf-8')
#      return ret
 
# if __name__ == '__main__':
#      httpd = make_server('', 8000, RunServer)
#      httpd.serve_forever()




