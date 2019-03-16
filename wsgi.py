from bottle import route, run, view, static_file, get
import os
import bottle
py_dir = base_path = os.path.abspath(os.path.dirname(__file__))
css_dir = img_dir = template_path = os.path.join(base_path, '_core')
spy_dir = os.path.join(base_path, '..', "_spy")
bottle.TEMPLATE_PATH.insert(0, template_path)


@route('/')
@view('index')
def index():
    return {}


@get("/_static/<filepath:re:.*..(png|jpg|svg|gif|ico)>")
def img(filepath):
        return static_file(filepath, root=img_dir)


@get("/css/<filepath:re:.*..css>")
def ajs(filepath):
        return static_file(filepath, root=css_dir)


# Static Routes
@get("<:path>/__init__.py")
def init_py():
    print("initview_py/__init__.py")
    return ""


# Static Routes
@get("/__code/kwarwp/<filepath:path>")
def view_py(filepath):
    print("view_py", filepath)
    return static_file(filepath, root=py_dir+"/kwarwp")


# Static Routes
@get("/__code/_spy/<module_name>/<filepath:re:.*..py>")
def spy(module_name, filepath):
    # print("spy", module_name, filepath)
    print("view_py", module_name, filepath)
    return static_file(filepath, root=os.path.join(spy_dir, module_name))


# Static Routes
# @get("/__code/<module_name:re:[a-z].*>/<filepath:re:.*\.py>")
@get("/__code/<module_name>/<filepath:re:.*..py>")
def core_py(filepath, module_name="julia"):

    print("core_py", module_name, filepath, os.path.join(py_dir, module_name))
    return static_file(filepath, root=os.path.join(py_dir, module_name))


run(host='localhost', port=8080)
