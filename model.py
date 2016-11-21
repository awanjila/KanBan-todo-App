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
				self.move_task(task_id, 'doing')
		except ValueError:
			print("\nTry again but this time round: TaskID should be a Number:\n")


#moves a task from doing section to done section	
	def done_task(self, task_id):
		try:
			if isinstance(int(task_id), int):
				self.move_task(task_id, 'done')
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

	def list_done(self):
		section='done'
		self.list_section(section)

	def list_section(self, section):
		self.section=section

		#the done section tasks
		if self.section=='done':
			query_selection="SELECT id, title, status, start_on, end_on FROM task WHERE status='done'"
			self.cursor.execute(query_selection)
			records=self.cursor.fetchall()
			if not records:
				print("\nYou have not finished any task(s) yet.\n")
			else:
				done_list=[]
				print("\nThese are the Tasks you have Completed and their Duration.\n")
				for row in records:
					start=datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
					stop=datetime.strptime(str(row[4]), '%Y-%m-%d %H:%M')
					start_time, stop_time =start.strftime('%H:%M').split(':'),stop.strftime('%H:%M').split(':')
					hours=int(stop_time[1])-int(stop_time[0])
					minutes=int(start_time[1])-int(start_time[0])
					tasks_duration=[row[0], row[1], row[2], hours, minutes]
					done_list.append(tasks_duration)
				print(tabulate(done_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
									numalign="center"))
				print('\n')

		elif self.section=='doing':
			query_selection="SELECT id, title, status, start_on, end_on FROM task WHERE status='doing'"
			self.cursor.execute(query_selection)
			records=self.cursor.fetchall()
			if not records:
				print("\nYou have not doing any task(s) yet.\n")
			else:
				doing_list=[]
				print("\nThese are the Tasks that you are still doing and their Duration.\n")
				for row in records:
					start=datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
					stop=datetime.strptime(str(row[4]), '%Y-%m-%d %H:%M')
					start_time, stop_time =start.strftime('%H:%M').split(':'),stop.strftime('%H:%M').split(':')
					hours=int(stop_time[1])-int(stop_time[0])
					minutes=int(start_time[1])-int(start_time[0])
					tasks_duration=[row[0], row[1], row[2], hours, minutes]
					done_list.append(tasks_duration)
				print(tabulate(doing_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
									numalign="center"))
				print('\n')

		elif self.section=='all':
			query_selection="SELECT * FROM task"
			self.cursor.execute(query_selection)
			records=self.cursor.fetchall()
			if not records:
				print("\nYou have not finished any task yet.\n")
			else:
				all_list=[]
				print('\n These are all the tasks in all the sections\n')
				for row in records:
					tasks_duaration=[row[0], row[1], row[2], row[3], row[4]]
					all_list.append(tasks_duration)
				print(tabulate(doing_list, headers=["Task Id", "Task Name", "Section", "Start Time", "End Time"],
									numalign="center"))
				print('\n')
		elif self.section=='todo':
			query_selection="SELECT * FROM task WHERE status='todo"
			self.cursor.execute(query_selection)
			records=self.cursor.fetchall()
			if not records:
				print("\nYou have not added any task(s) yet.\n")
			else:
				todo_list=[]
				print("\nThese are the Tasks that are to be done, and their initiation time.\n")
				for row in records:
					start=datetime.strptime(str(row[3]), '%Y-%m-%d %H:%M')
					stop=datetime.strptime(str(row[4]), '%Y-%m-%d %H:%M')
					start_time, stop_time =start.strftime('%H:%M').split(':'),stop.strftime('%H:%M').split(':')
					hours=int(stop_time[1])-int(stop_time[0])
					minutes=int(start_time[1])-int(start_time[0])
					tasks_duration=[row[0], row[1], row[2], hours, minutes]
					done_list.append(tasks_duration)
				print(tabulate(todo_list, headers=["Task Id", "Task Name", "Section", "Hours Taken", "Minutes Taken"],
									numalign="center"))
				print('\n')
	#method to move a task from one section to another
	def move_task(self, task_id, section):
		self.task_id =task_id
		self.section =section
		# check first if the task exists
		check="SELECT * FROM task WHERE id =?"
		self.cursor.execute(check, (self.task_id,))
		data =self.cursor.fetchone()

		if data is None:
			print('\nHey! There it seems that the Task you are looking for doesnt exist.\n\nType "list all" to check the Task list\n')
		else:
			task_current_section=data[2]
			if task_current_section=='todo' and self.section=='done':
				print('\nHey, You havent started doing that task yet\n')

			if task_current_section=='done' and self.selection=='done':
				print('\nHey, You have already fineshed doing that task\n')
			if task_current_section=='doing' and self.selection=='doing':
				print('\nHey, You havent currently doing that task\n')
			elif (task_current_section=='todo' and self.selection=='doing')\
			or (task_current_section=='doing' and self.selection=='done'):

			# if the task is in todo section move it to the doing section
				if task_current_section=='todo':
					start_time=datetime.now().strftime("%Y-%m-%d %H:%M")	
					move_task="UPDATE task SET status=?, start_on =? WHERE id=?"
					self.cursor.execute(move_task, (self.section, start_time, self.task_id))
					self.cursor.execute("SELECT * FROM task WHERE id =?", (self.task_id,))
					print("\nWonderful! You have started doing the following task\n")
					started_task=self.cursor.fetchall()
					for row in started_task:
						task_list=[row[0], row[1], row[2], row[3],row[4]]
						print(tabulate([task_list], headers=["Task ID", "Task Name", "Section", "Start Time", "Finish Time"],
							numalign="center"))
						print('\n')
						self.conn.commit()
			# if task is in doing section move it to done section
				elif task_current_section=='doing':
					current_time=datetime.now().strftime("%Y-%m-%d %H:%M")
					move_task="UPDATE task SET status=?, end_on=? WHERE id=?"
					done_cursor=self.cursor.execute(move_task, (self.section, current_time, self.task_id))
					print("\nGreat! You have finished the following task\n")
					task=done_cursor.fetchall()
					for row in task:
						task_list=[row[0], row[1], row[2], row[3],row[4]]
					print(tabulate([task_list], headers=["Task ID", "Task Name", "Section", "Start Time", "Finish Time"],
							numalign="center"))

					print('\n')
					self.conn.commit()
			else:
				print('\nInvalid Section\n')










