from flask import Flask, render_template

app = Flask(__name__)


@app.route('/varDemo')
def var_demo():
    context = {
        'username': 'John Doe',
        'age': 30,
    }
    return render_template('varDemo.html',context=context)

@app.route('/filterDemo')
def filter_demo():
    context = {
        'username': ['John Doe','Jane Smith','Bob Johnson','Jenner','Jack Black'],
        'age': [30, 25, 40, 35, 28],
        'is_active': [True, False, True, True, False],
        'salary': [123456.789, 987654.321, 456789.123, 654321.987, 321654.789],
        'date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
    }
    return render_template('filterDemo.html', context=context)
if __name__ == '__main__':
    app.run(debug=True)