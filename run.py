from flask import Flask, render_template
app = Flask(__name__)

#dynamic data


@app.route("/")
def template_test():
    return render_template('template.html', my_string="game module here", my_list=[0,1,2,3,4,5])


if __name__ == '__main__':
    app.run(debug=True)