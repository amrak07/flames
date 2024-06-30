from flask import Flask, render_template, request

app = Flask(__name__)

# Store user details in a list
user_details = []

def get_relationship(name1, name2):
    name1 = list(name1.replace(" ", "").lower())
    name2 = list(name2.replace(" ", "").lower())
    for i in name2:
        if not i in name1:
            name1.append(i)
        else:
            name1.remove(i)
    total_letters = len(name1)
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
    while len(flames) > 1:
        index = total_letters % len(flames) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        result = get_relationship(name1, name2)
        # Store the user details
        user_details.append({'name1': name1, 'name2': name2, 'result': result})
        return render_template('index.html', result=result, name1=name1, name2=name2)
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', user_details=user_details)

if __name__ == '__main__':
    app.run(debug=True)
