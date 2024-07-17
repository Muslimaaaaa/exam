from task1 import database
class Product:
    table_name = "product"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {Product.table_name} ORDER BY id"
        data = database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO country(name) VALUES('{self.name}')
        """
        return database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"

        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}'"

        return database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        if column == "id":
            query = f"DELETE FROM {table} WHERE {column} = {data}"

        else:
            query = f"DELETE FROM {table} WHERE {column} = '{data}'"
        return database.connect(query, "delete")