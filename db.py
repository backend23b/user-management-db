from tinydb import TinyDB, Query
from tinydb.table import Document


class DB:
    def __init__(self, file_path):
        db = TinyDB(file_path, indent=4)
        self.users = db.table('users')

    def is_user(self, user_id):
        return self.users.contains(doc_id=user_id)

    def add_user(self, user_id, firstname, lastname, username):
        if self.is_user(user_id):
            return False
        else:
            doc = Document(
                value={
                    "firstname": firstname,
                    "lastname": lastname,
                    "username": username
                },
                doc_id=user_id
            )
            self.users.insert(doc)
            return True

    def get_user(self, user_id):
        if self.is_user(user_id):
            return self.users.get(doc_id=user_id)
        return False
    
    def get_all_users(self):
        return self.users.all()

    def update_user(self, user_id, firstname=None, lastname=None, username=None):
        if self.is_user(user_id):
            fields = {}
            if firstname: fields['firstname'] = firstname
            if lastname: fields['lastname'] = lastname
            if username: fields['username'] = username

            self.users.update(fields=fields, doc_ids=[user_id])
            return True
        
        return False

    def delete_user(self, user_id):
        if self.is_user(user_id):
            self.users.remove(doc_ids=[user_id])
            return True
        return False
