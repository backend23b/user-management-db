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

def test_get_user():
    print(db.get_user(user_id=101))

# test_get_user()

def test_get_all_users():
    print(db.get_all_users())

# test_get_all_users()

def test_update_user():
    print(db.update_user(
        user_id=101,
        username="ndjsabn"
    ))

# test_update_user()

def test_delete_user():
    print(db.delete_user(user_id=101))

# test_delete_user()

