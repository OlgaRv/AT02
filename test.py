import pytest
from main import init_db,add_user, get_users

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, 'John', 25)
    assert get_users(db_conn, 'John') == (1, 'John', 25)