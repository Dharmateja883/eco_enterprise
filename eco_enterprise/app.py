from flask import Flask, render_template, request, redirect
from repository.issue_repo import add_issue, get_issues

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['location'],
            request.form['issue_type'],
            request.form['description']
        )
        add_issue(data)
        return redirect('/admin')

    return render_template('home.html')

@app.route('/admin')
def admin():
    issues = get_issues()
    return render_template('admin.html', issues=issues)

if __name__ == '__main__':
    app.run(debug=True)