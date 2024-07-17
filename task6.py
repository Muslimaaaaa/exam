import psycopg2 as psql

class database:
    @staticmethod
    def connect(query:str, query_type:str):
        db = psql.connect(
            database = 'exam',
            user = 'postgres',
            password = 'muslima2004',
            host = 'localhost',
            port = "5432"
        )
        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'delete', 'insert', 'update']
        if query_type in data:
            db.commit()
            return f"""{query_type} query successfully"""
        else:
            return cursor.fetchall()