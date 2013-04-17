from bottle import route, run, template, get, static_file
from random import choice, sample, randrange

minOfSyllables = 2
maxOfSyllables = 4
syllables = ["ба", "би", "ва", "ми", "вя", "га", "жа", "го", "ма", "зи", "ле",
             "ня", "ли", "ра", "са", "фа", "но", "ре", "мы", "ца", "пы", "сю",
             "та", "ся", "цо", "ша", "су", "фо", "ки", "ку", "ка", "тю", "ту",
             "тор", "сов", "мол", "мир", "вен", "бир", "гол", "лав", "нов", ]
femaleEnds = ["сия", "на", "ка", "тя", "ра", "да", "ля", "ша", "ния", "рия"]
maleEnds = ["андр", "ша", "ня", "та", "нид", "рей", "ор", "ан", "ис", "жа"]

def make_name(for_whom):
    name = sample(syllables, randrange(minOfSyllables, maxOfSyllables))
    if for_whom == 'boy':
        name += [choice(maleEnds)]
    elif for_whom == 'girl':
        name += [choice(femaleEnds)]
    return "".join(name).capitalize()

@route('/for/girl')
def girl():
    return template('names', name=make_name(for_whom='girl'), a_girl='active',
                    a_boy='', f_girl='#', f_boy='/for/boy')

@route('/for/boy')
def boy():
    return template('names', name=make_name(for_whom='boy'), a_girl='',
                    a_boy='active', f_girl='/for/girl', f_boy='#')

@route('/')
def index():
    return template('index')

# Static Routes
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

run(host='localhost', port=80, debug=True)
