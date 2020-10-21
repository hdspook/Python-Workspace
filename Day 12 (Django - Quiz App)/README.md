python manage.py migrate
python manage.py makemigrations quiz
python manage.py sqlmigrate quiz 001
python manage.py migrate
python manage.py shell


from quiz.models import Choice, Question

q = Question(question_text="How many days do we have in a week?")
q.save()

q.choice_set.create(choice_text='7', marked = 'NO', answer = 'YES')
q.choice_set.create(choice_text='8', marked = 'NO', answer = 'NO')
####
q = Question(question_text="How many colors are there in a rainbow?")
q.save()

q.choice_set.create(choice_text='7', marked = 'NO', answer = 'YES')
q.choice_set.create(choice_text='8', marked = 'NO', answer = 'NO')
####
q = Question(question_text="How many letters are there in the English alphabet?")
q.save()

q.choice_set.create(choice_text='27', marked = 'NO', answer = 'NO')
q.choice_set.create(choice_text='26', marked = 'NO', answer = 'YES')
####
q = Question(question_text="How many sides are there in a triangle?")
q.save()

q.choice_set.create(choice_text='5', marked = 'NO', answer = 'NO')
q.choice_set.create(choice_text='3', marked = 'NO', answer = 'YES')