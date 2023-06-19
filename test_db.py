from db import DB

db = DB('db.json')

def test_add_user():
    db.add_user(
        user_id=101,
        firstname='Ali',
        lastname="Valiyev",
        username="optimist"
    )

# test_add_user()

def test_is_user():
    print(db.is_user(user_id=101))

# test_is_user()