import sqlite3
from datetime import datetime
from tabulate import tabulate


class KanBan(object):
	def __init__(self):
		#connects to a KanBanApp database called tasks.db
		self.conn=sqlite3.connect('tasks.db')    
		self.cursor=self.conn.cursor()
		self.start = datetime.now().strftime("%Y-%M-%d %H:%M")
		#calls a method called create_table
		self.create_table()   

	# creates a table called task in the KanBanApp database
	def create_table(self):
		table = 'CREATE TABLE IF NOT EXISTS task('\
		'id INTEGER PRIMARY KEY AUTOINCREAMENT,'\
		'title TEXT,'\
		'status TEXT,'\
		'start_on DATETIME,'\
		'end_on DATETIME);'	

		self.cursor.execute(table)


	# This method creates a new task in the table task
	def create_task(self):
		self.name=name
		self.task_name=' '.join(self.name)
		self.section='todo'
		insert_query ='INSERT INTO task(title, status) VALUES(?, ?)'
		self.cursor.execute(insert_query, (self.task_name, self.selection))

		print("\nTask %s Has been created \n" %self.task_name)

		#gets the entry with the biggest value LIFO method from the table task
		self.cursor.execute("SELECT MAX(id), title, status, start_on, end_on FROM task")

		task=self.cursor.fetchall()
		for row in task:
			task_list=[row[0], row[1], row[2], row[3], row[4]]
		print(tabulate([task_list], headers=["Task Id", "Task Name", "Section", "Start Time", "Finish Time"],
					numalign="center"))
		self.conn.commit()
		print('\n')


#moves a task from todo section to doing section
	def doing_task(self, task_id):
		try:
			if isinstance(int(task_id), int):
				self.move_task(task_id, 'done')
		except ValueError:
			print("\nTry again but this time round: TaskID should be a Number:\n")


#moves a task from doing section to done section	
	def done_task(self, task_id):
		try:
			if isinstance(int(task_id), int):
		except ValueError:
			print("\nTry again but this time round: TaskID should be a Number:\n")



	def list_all(self):
		section='all'
		self.list_section(section)

	def list_todo(self):
		section='todo'
		self.list_section(section)

	def list_doing(self):
		section='doing'
		self.list_section(section)

	def list_doing(self):
		section='doing'
		self.list_section(section)

	def list_section(self, section):
		self.section=section





