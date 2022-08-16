# Напишите класс, определяющий текущий период суток в том или ином часовом поясе
# Подумайте, какие атрибуты должны определяться в классе, а какие в экземпляреэ

# с 0 до 6 часов — ночь
# с 6 до 12 часов — утро
# с 12 до 18 часов — день
# с 18 до 24 часов — вечер

# Часовые пояса от -12 до +12

from datetime import datetime, timedelta, time

class Period_of_day:
	# period = ['ночь', 'утро', 'день', 'вечер']
	# dat = datetime.now()
	# time_now = datetime.time(dat)
	utc0 = datetime.utcnow()

	def __init__(self, u=0):
		self.u = u

	# def time_in_range(start, end, current):
	# 	return start <= current <= end

	def Tzone(self):
		p = self.utc0 + timedelta(hours=self.u)
		return p.time().hour

	def Period1(self):
		p = self.utc0 + timedelta(hours=self.u)

		if time(0, 0, 0) < p.time() and p.time() < time(6, 59, 59):
			print('ночь')

		elif time(6, 0, 0) < p.time() and p.time() < time(11, 59, 59):
			print('утро')

		elif time(12, 0, 0) < p.time() and p.time() < time(17, 59, 59):
			print('день')
			
		elif time(18, 0, 0) < p.time() and p.time() < time(23, 59, 59):
			print('вечер')

	def Period2(self):
		i = self.Tzone()

		if 0 < i and i < 6:
			print('ночь')

		elif 6 < i and i < 12:
			print('утро')

		elif 12 < i and i < 18:
			print('день')

		elif 18 < i and i < 24:
			print('вечер')



t1 = Period_of_day(0)
# print(t1.Tzone())
t1.Period1()
t1.Period2()
print()

t2 = Period_of_day(-12)
# print(t1.Tzone())
t2.Period1()
t2.Period2()
print()

t3 = Period_of_day(12)
# print(t1.Tzone())
t3.Period1()
t3.Period2()
print()

t4 = Period_of_day(-5)
# print(t1.Tzone())
t4.Period1()
t4.Period2()
print()

t5 = Period_of_day(5)
# print(t1.Tzone())
t5.Period1()
t5.Period2()
print()

t6 = Period_of_day(3)
# print(t1.Tzone())
t6.Period1()
t6.Period2()


# a = time(2, 0, 0)
# print(a)





# dat = datetime.now()
# time_now = datetime.time(dat)
# utc0 = datetime.utcnow().time()

# qwe = utc0 + timedelta(hours=2)
# print(utc0)


# a = 4
# import datetime

# test = datetime.time(2 + a, 10, 20, 14)
# print(test)

# t = datetime.time(1, 10, 20, 13)
# print(t)


# utc0 = datetime.datetime.utcnow()
# u = datetime.datetime.time()
# print(u)