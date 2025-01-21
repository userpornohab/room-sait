import servises

src = servises
data_start_test = '01.01.2024'
data_end_test = '01.03.2024'
src.year = 2024
print('wdqwqd')
src.limit_number = 4
src.upd_price_test = 3000
a = src.create_calendar_dict(src.year)

src.update_price(a, data_start_test, data_end_test) # обновляет цену в календаре на заданные даты
#src.upd_number_rooms_up(a, data_start_test, data_end_test) # обновляет число комнат в положительную сторону на заданные даты
src.upd_number_rooms_down(a, data_start_test, data_end_test) # обновляет число комнат в отрицательную сторону на заданные даты
print(src.checking_occupancy(a, data_start_test, data_end_test)) # проверяет занятость комнат на заданные даты 

'''
id
год 
максимальное количество гостей
назване номера либо его номер
календарь с датами занятости и ценами 
'''