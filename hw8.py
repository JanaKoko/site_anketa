import models
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anketa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
from flask import url_for, render_template, request, redirect


# In[2]:


@app.route('/')
def one():
    return render_template('form.html')


# In[3]:


@app.route('/questions', methods=['get'])
def que():
    return render_template('qu.html')


# In[4]:


@app.route('/stats')
def stat():
    return render_template('stats.html')


# In[5]:


@app.route('/thanks', methods=['get'])
def th():
            # достаем параметры
    gender = request.args.get('gender')
    english = request.args.get('english')
    age = request.args.get('age')
    t = str(time.time()).split('.')
    my_id = ''.join(t)
    # создаем профиль пользователя
    user = models.People(
        person_id = int(my_id),
        age=age,
        gender=gender,
        english = english
    )
    # добавляем в базу
    db.session.add(user)
    # сохраняемся
    db.session.commit()
    # получаем юзера с айди (автоинкремент)
    #db.session.refresh(user)
    
    # получаем два ответа
    q1 = request.args.get('score')
    q2 = request.args.get('me')
    q3 = request.args.get('others')
    
    # привязываем к пользователю (см. модели в проекте)
    answer = models.Answers(pers_id = int(my_id),
                     one = int(q1),
                     two = q2,
                     three = q3)
    # добавляем ответ в базу
    db.session.add(answer)
    # сохраняемся
    db.session.commit()
    
    #return 'Ok'
    return render_template('thanks.html')


# In[ ]:


if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:



