import sqlite3

class DBHelper():
	"""`DBHelper is used to handle connections and queries to sqlite database"""
	def __init__(self, dbname="lucasbot.sqlite"):
		super(DBHelper, self).__init__()
		self.dbname=dbname
		self.conn = sqlite3.connect(dbname)

	def setup(self):
		"""
		"Schema: tabela chamados com nome do usuario no telegram, nome da pessoa, e-mail, e mensagem"
		"""
		stmt = "CREATE TABLE IF NOT EXISTS chamados (id INTEGER PRIMARY KEY AUTOINCREMENT, user text, nome text, email text, mensagem text)"
		self.conn.execute(stmt)
		self.conn.commit()

	def add_chamado(self, user, nome, email, mensagem):
		stmt = "INSERT INTO chamados (user, nome, email, mensagem) VALUES (?,?,?,?)"
		args = (user, nome, email, mensagem)
		self.conn.execute(stmt, args)
		self.conn.commit()

	def delete_chamado(self, id_chamado):
		stmt = "DELETE FROM chamados WHERE id = (?)"
		args = (id_chamado )
		self.conn.execute(stmt, args)
		self.conn.commit()

	def get_items(self):
		stmt = "SELECT * FROM chamados"
		return [list(x) for x in self.conn.execute(stmt)]

	def add_tmp(self, text):
		stmt = "INSERT INTO tmp (texto) VALUES (?)"
		args = (text,)
		self.conn.execute(stmt, args)
		self.conn.commit()
