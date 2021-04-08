import database_common
import bcrypt


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@database_common.connection_handler
def add_user(cursor, email, password):
    query = """
        INSERT INTO users
        VALUES (%(email)s, %(password)s);
        """
    cursor.execute(query, {'email': email, 'password': password})


@database_common.connection_handler
def get_password_for_user(cursor, email):
    query = """
    SELECT password 
    FROM users
    WHERE email=%(email)s
    """
    cursor.execute(query, {'email': email})
    return cursor.fetchone()


@database_common.connection_handler
def get_email(cursor, email):
    query = """
    SELECT email 
    from users
    WHERE email=%(email)s
    """
    cursor.execute(query, {'email': email})
    return cursor.fetchone()


@database_common.connection_handler
def get_questions(cursor):
    query = '''
    SELECT *
    FROM questions
    '''
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_question_by_id(cursor, id=1):
    query = '''
    SELECT *
    FROM questions
    where id=%(id)s
    '''
    cursor.execute(query, {'id': id})
    return cursor.fetchone()


@database_common.connection_handler
def get_next_question(cursor, offset):
    query = '''
    select * from questions
    limit 1 offset %(offset)s
    '''
    cursor.execute(query, {'offset': offset})
    return cursor.fetchone()


@database_common.connection_handler
def get_number_of_questions(cursor):
    query='''
    select count(id) from questions
    '''
    cursor.execute(query)
    return cursor.fetchone()