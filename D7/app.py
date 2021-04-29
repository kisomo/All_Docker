
#https://www.youtube.com/watch?v=Z1RJmh_OqeA

#RUN from app import db 
#RUN db.create_all()


from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


######################################################################################################################################
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks = tasks)

#######################################################################################################################################
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


########################################################################################################################################
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html',task = task)


########################################################################################################################################
if __name__ == "__main__":
    app.run(debug=True)

























#sudo docker build . -t flask_app_d7:1.0.0

#sudo docker images

#sudo docker run -d -p 5000:5000 flask_app_d7:1.0.0
#sudo docker run --rm -it flask_app_d7:1.0.0



