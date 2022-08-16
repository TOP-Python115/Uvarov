# Напишите класс, определяющий текущий период суток в том или ином часовом поясе
# Подумайте, какие атрибуты должны определяться в классе, а какие в экземпляреэ

from datetime import datetime, timedelta, time

class Period_of_day:

	def __init__(self, u=0):
		self.utc0 = datetime.utcnow()
		self.u = u

	def Tzone(self):
		p = self.utc0 + timedelta(hours=self.u)
		return p.time().hour

	def Period(self):
		i = self.Tzone()

		if 0 <= i < 6:
			print('ночь')

		elif 6 <= i < 12:
			print('утро')

		elif 12 <= i < 18:
			print('день')

		elif 18 <= i < 24:
			print('вечер')

c = int(input('Введите часовой пояс (UTC): '))

t1 = Period_of_day(c)
t1.Period()
