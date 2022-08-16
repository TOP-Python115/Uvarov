d1 = {
		"name": "Elijah Klein",
		"phone": "(994) 308-4233",
		"email": "nam.interdum.enim@outlook.edu",
		"address": "P.O. Box 706, 3251 Luctus Street",
		"postalZip": "18923-261",
		"region": "Bình Định",
		"country": "Italy",
		"numberrange": 8
	}

d2 = {
		"name": "Camilla Meyer",
		"phone": "1-635-166-9257",
		"email": "sagittis.semper@hotmail.org",
		"address": "670-5449 Nunc Av.",
		"postalZip": "6554",
		"region": "São Paulo",
		"country": "Costa Rica",
		"numberrange": 7
	}

dict = {key: [d1.get(key, ""), d2.get(key, "")] for key in {**d1, **d2}}

   
print(dict)


# {'name': ['Elijah Klein', 'Camilla Meyer'], 'phone': ['(994) 308-4233', '1-635-166-9257'], 'email': ['nam.interdum.enim@outlook.edu', 'sagittis.semper@hotmail.org'], 'address': ['P.O. Box 706, 3251 Luctus Street', '670-5449 Nunc Av.'], 'postalZip': ['18923-261', '6554'], 'region': ['Bình Định', 'São Paulo'], 'country': ['Italy', 'Costa Rica'], 'numberrange': [8, 7]}