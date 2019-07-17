from __future__ import absolute_import
from tinydb import TinyDB, Query, where
from tinydb.operations import delete
from data_access_layer.BaseDB import BaseDB
from typing import List
from typing import Dict


class RestDB(BaseDB):

    def __init__(self, path):
        self.db = TinyDB(path)

    def db_insert(self, identity, name, status, username) -> None:
        """
            Inserts a workspace with id, name and status to the db
            :param name: name of the workspace to be inserted in db
            :param identity: unique uuid_name assigned to the workspace
            :param status: field specifying workspace creation inserted in db
            :param username: username of the user creating the workspace
        """
        self.db.insert({'id': str(identity), 'name': name, 'status': status, 'username': username})

    def db_insert_no_name(self, identity, status, username) -> None:
        """
            Inserts a workspace with id, and status to the db
            :param identity: unique uuid_name assigned to the workspace
            :param status: field specifying workspace creation inserted in db
        """
        self.db.insert({'id': str(identity), 'status': status, 'username': username})

    def db_remove(self, identity, admin, username) -> None:
        """
            Removes a workspace record from db
            :param identity: unique uuid_name assigned to the workspace
        """
        workspace = Query()
        if admin:
            self.db.remove(workspace.id == identity)
        else:
            el = self.db.get((workspace.id == identity) & (workspace.username == username))
            doc_id = el.doc_id
            self.db.remove(doc_ids=[doc_id])

    def db_update(self, identity, status) -> None:
        """
            Removes a workspace record from db
            :param identity: unique uuid_name assigned to the workspace
            :param status: field specifying workspace creation inserted in db
        """
        workspace = Query()
        self.db.update({'status': status}, workspace.id == identity)

    def db_search(self, name, admin, username) -> List[Dict]:
        """
        """
        workspace = Query()
        if admin:
            return self.db.search(workspace.name == name)
        else:
            return self.db.search((workspace.name == name) & (workspace.username == username))

    def db_search_username(self, username) -> List[Dict]:
        """
            Removes a workspace record from db
            :param name: name of the workspace to be inserted in db
            :return: a list of records in db that match name with param name
        """
        workspace = Query()
        return self.db.search(workspace.username == username)

    def db_search_identity(self, identity) -> List[Dict]:
        """
            Removes a workspace record from db
            :param name: name of the workspace to be inserted in db
            :return: a list of records in db that match name with param name
        """
        workspace = Query()
        return self.db.search(workspace.id == identity)[0]

    def db_list_all(self, username, admin) -> List[Dict]:
        """
            Lists all workspace records in database
            :return: a list of all records in db
        """
        if admin:
            return self.db.all()
        else:
            workspace = Query()
            return self.db.search(workspace.username == username)


