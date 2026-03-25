from flask import Flask, render_template, request, redirect
from database import init_db, insert_feedback, get_feedback
import os

# Resolve templates/static path so it works both in Docker (/app/templates) and local dev (../templates)
basedir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(basedir, os.pardir))

if os.path.isdir(os.path.join(basedir, 'templates')):
    template_dir = os.path.join(basedir, 'templates')
else:
    template_dir = os.path.join(project_root, 'templates')

if os.path.isdir(os.path.join(basedir, 'static')):
    static_dir = os.path.join(basedir, 'static')
else:
    static_dir = os.path.join(project_root, 'static')

print('DEBUG: template_dir=', template_dir)
print('DEBUG: static_dir=', static_dir)
print('DEBUG: index exists', os.path.exists(os.path.join(template_dir, 'index.html')))

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

init_db()

@app.route('/')
def index():
    feedbacks = get_feedback()
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    insert_feedback(name, message)
    return redirect('/')

if __name__ == '__main__':
    print("Starting Flask App...")
    app.run(host='0.0.0.0', port=5000, debug=False)