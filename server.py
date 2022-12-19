from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

# def test():
#     return 'hello there'

def index():
    return '''
    <link href="/static/style.css" rel="stylesheet" />
    <div class="important">
        This is important!
    </div>
    <div>
        This is normal.
    <div>
    '''

if __name__ == '__main__':
    app.run()

@app.route('/user/<username>')
def profile(username):
    return f'hello {username}'
    # return render_template('profile.html', name=name)

