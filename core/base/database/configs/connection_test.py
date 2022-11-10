from .connection import DBConnection


def test_connect():
   with DBConnection() as db:
    assert db.session.is_active==True
    
   
   