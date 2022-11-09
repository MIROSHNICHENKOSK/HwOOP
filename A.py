class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        

class Lecturer(Mentor):
	def to_compare(self):
		try:
			gr = 0
			for v in self.grades.values():
				for el in v: gr += int(el)
			gr /= len(self.grades)

			return gr
		except ZeroDivisionError: return 0.0

	def __str__(self):
		gr = 0
		for v in self.grades.values():
			for el in v: gr += int(el)
		gr /= len(self.grades)

		return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {gr}\n+------------------+'
			

class Reviewer(Mentor):
	def hw_rate(self, student, course, grade):
		if isinstance(student, Student) and course in student.courses_in_progress:
			if course in student.grades:
                
				student.grades[course] += [grade]
			else:
                
				student.grades[course] = [grade]
		else:
			print( 'Ошибка' )


	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\n+------------------+'



class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}


	def to_compare(self):
		try:
			gr = 0
			for v in self.grades.values():
				for el in v: gr += int(el)
			gr /= len(self.grades)

			return gr
		except ZeroDivisionError: return 0.0


	def cruel_rate(self, victim, course, grade):
		if course in self.courses_in_progress and course in victim.courses_attached:
			if course in victim.courses_attached:
				if course in victim.grades:
					victim.grades[course] += [grade]
				else:
					victim.grades[course] = [grade]


			else:
				return '[ERROR] Лектор не ведёт такие курсы!'
		else:
			return '[ERROR] Что-то здесь не так... -_- '

		return '[!]', victim.grades


	def __str__(self):
		gr = 0
		for v in self.grades.values():
			for el in v: gr += int(el)
		gr /= len(self.grades)


		cip = ''
		for el in self.courses_in_progress:
			cip += str(el)
			if self.courses_in_progress.index(el) != len(self.courses_in_progress)-1: cip += ', '

		fc = ''
		for el in self.finished_courses:
			fc += str(el)
			if self.finished_courses.index(el) != len(self.finished_courses)-1: fc += ', '


		return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {gr}\nКурсы в процессе изучения: {cip}\nЗавершенные курсы: {fc}\n+------------------+'


def compare(a, b):
	a_grades = a.to_compare()
	b_grades = b.to_compare()

	if a_grades > b_grades:
		return f'{a.name} > {b.name}'

	if a_grades < b_grades:
		return f'{a.name} < {b.name}'

	else:
		return 'Ой, два одинаковых балла скинули'


def grades_of_all(students, course):
	grades_list = []
	for student in students:
		grades_list.append( student.to_compare() )

	try:
		return ( sum(grades_list)/len(grades_list) )

	except ZeroDivisionError: return 0.0



best_student					 	= Student('Ruoy', 'Eman', 'Attack_helicopter_apache')
best_student.courses_in_progress	+= ['Python']
best_student.finished_courses 		+= ['ООП', 'git']
worst_student 						= Student('Mentor\'s', 'Pain', 'Rockgender')
worst_student.courses_in_progress 	+= ['Python', 'git']
worst_student.finished_courses 		+= ['Профессиональное сливание с пар', 'git']


cool_mentor 					= Lecturer('Some', 'Buddy')
cool_mentor.courses_attached 	+= ['Python']
normal_mentor 					= Lecturer('Shrek', 'Vazovsky')
normal_mentor.courses_attached 	+= ['git']

refactor_dude 	= Reviewer('I_am', 'YOUR_PAIN')
refactor_dude2 	= Reviewer('Just', 'refactoring')


refactor_dude.hw_rate(best_student, 'Python', 12) 
best_student.cruel_rate(cool_mentor, 'Python', 10)


print(best_student)
print(cool_mentor)
print(refactor_dude)

print( compare(best_student, worst_student) )
print( grades_of_all([best_student, worst_student], 'Python') )
print( grades_of_all([cool_mentor, normal_mentor], 'Python') )


