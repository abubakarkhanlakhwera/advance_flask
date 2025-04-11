from flask import Flask, render_template

app = Flask(__name__)

@app.route('/printTable/<int:number>')
def print_table(number):
    return render_template('printTable.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)