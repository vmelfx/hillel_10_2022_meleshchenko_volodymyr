# class Session:
#     @staticmethod
#     def execute(self):
#         pass
#
#     @staticmethod
#     def close(self):
#         pass
#
#
# class Database:
#     @staticmethod
#     def create_session():
#         return Session
#
#     @staticmethod
#     def get_users() -> list[dict]:
#         print("SELECT * FROM users; ")
#         return []
#
#     @staticmethod
#     def save_user() -> None:
#         print("INSERT INTO users SET(id, name) VALUES (%s, %s);", **values)
# users = Database.get_users()
#
# # OUR CODE
# class DBClient:
#     def __init__(self, host: str, port: int) -> None:
#         self.host: str = host
#         self.port: int = port
#
#     def __enter__(self, *args, **kwargs):
#         self.session = Database.create_session()
#
#     def __exit__(self):
#         self.session.close()
#
#     @staticmethod
#     def get_users() -> list[dict]:
#         with self.session as session:
#             session.execute(Database.get_users)
#         return users
#
# def main():
#     client = DBClient(host="localhost", port=5432)
#     user = client.get_users()
