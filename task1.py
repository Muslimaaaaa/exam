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

    def create_table(query:str, query_type:str):
        product = f"""
            CREATE TABLE product(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                price integer,
                color Varchar(70),
                image_url VARCHAR(40),
                create_date TIMESTAMP DEFAULT now());"""
        customers = f"""
                    CREATE TABLE customers(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        birth_date DATE,
                        create_date TIMESTAMP DEFAULT now());"""

        data = {"customers": customers,
                "product": product }
        for i in data:
            print(f"{i} {database.connect(data[i], "create")}")

if __name__ == "__main__":
    database = database()




