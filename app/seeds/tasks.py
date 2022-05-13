from app.models import db, Task


def seed_tasks():
    task_one = Task(
        user_id=1,
        board_id=1,
        tasks='Finish first CRUD feature',
    )
    task_two = Task(
        user_id=1,
        board_id=1,
        tasks='Finish second CRUD feature',
    )
    task_three = Task(
        user_id=1,
        board_id=1,
        tasks='Styling and finalize features',
    )
    task_four = Task(
        user_id=1,
        board_id=2,
        tasks='Start capstone'
    )
    task_five = Task(
        user_id=1,
        board_id=2,
        tasks='Edit capstone'
    )
    task_six = Task(
        user_id=1,
        board_id=2,
        tasks='Finish capstone'
    )
    task_seven = Task(
        user_id=1,
        board_id=4,
        tasks='I met some pretty cool people throughout this program'
    )
    task_eight = Task(
        user_id=1,
        board_id=4,
        tasks='One more week... And we are finally done with projects!'
    )
    task_nine = Task(
        user_id=1,
        board_id=4,
        tasks='I am so hungry, what shall I have for breakfast? 💬'
    )


    db.session.add_all([task_one, task_two, task_three, task_four, task_five, task_six, task_seven, task_eight, task_nine])
    db.session.commit()

def undo_tasks():
    db.session.execute('TRUNCATE tasks RESTART IDENTITY CASCADE;')
    db.session.commit()
