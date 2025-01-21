import calendar

cost_price = []
counter_room = [] 

def create_calendar_dict(year):

    cal_dict = {}
    for month in range(1, 13):
        month_str = f"{month:02d}"  # Преобразуем номер месяца в строку с ведущим нулем (01, 02, ...)
        cal_dict[month_str] = {}
        # Определяем количество дней в месяце
        num_days = calendar.monthrange(year, month)[1] 
        for day in range(1, num_days + 1):
            day_str = f"{day:02d}" 
            # Создаем словарь для каждого дня с начальными значениями
            cal_dict[month_str][day_str] = {'цена': 100, 'заполняемость': 1}
    return cal_dict

def validate_date_range(start_year, end_year):
    """Проверяет, что начальный и конечный год совпадают."""
    if start_year != end_year:
        raise ValueError("Начальный и конечный год должны совпадать")

def update_price_range(month_str, day_str, cal_dict):
    cal_dict[month_str][day_str]['цена'] = upd_price_test


def update_number_rooms_up(month_str, day_str, cal_dict):
    occupancy = cal_dict[month_str][day_str]['заполняемость']
    if occupancy < limit_number:
         cal_dict[month_str][day_str]['заполняемость'] +=1
    else:
        raise ValueError("Превышение лимита")

def update_number_rooms_down(month_str, day_str, cal_dict):
    occupancy = cal_dict[month_str][day_str]['заполняемость']
    if occupancy > 0:
         cal_dict[month_str][day_str]['заполняемость'] -=1
    else:
        raise ValueError("Не возможно уменьшить количество комнат, по причине 0")
    
def checking_room_occupancy(month_str, day_str, cal_dict):
    counter_room.append(cal_dict[month_str][day_str]['заполняемость'])
    cost_price.append(int(cal_dict[month_str][day_str]['цена']))


def search_data(cal_dict, start_date_str, end_date_str, year, mutable_function):
    # Преобразуем строки дат в числа (день, месяц, год)
    start_day, start_month, start_year = map(int, start_date_str.split('.'))
    end_day, end_month, end_year = map(int, end_date_str.split('.'))

    validate_date_range(start_year, end_year)

    for month in range(start_month, end_month + 1):
        month_str = f"{month:02d}"
        start_day_month = start_day if month == start_month else 1
        end_day_month = end_day if month == end_month else calendar.monthrange(year, month)[1]

        for day in range(start_day_month, end_day_month + 1):
            if month == end_month and day == end_day:  # Отбрасываем последний день
                continue
            day_str = f"{day:02d}"
            # Устанавливаем новую цену для каждого дня в диапазоне
            mutable_function(month_str, day_str, cal_dict)


# Создание календаря на 2024 год

limit_number = None
year = None
upd_price_test = None

# Обновление цены с 25.01.2024 по 02.02.2024


def update_price(a, data_start, data_end):
    search_data(a, data_start, data_end, year, update_price_range)


def upd_number_rooms_up(a, data_start, data_end):
    search_data(a, data_start, data_end, year, update_number_rooms_up)
    print(a)
    

def upd_number_rooms_down(a, data_start, data_end):
    search_data(a, data_start, data_end, year, update_number_rooms_down)
    print(a)

def checking_occupancy(a, data_start, data_end):
    search_data(a, data_start, data_end, year, checking_room_occupancy)
    count_cost_day = sum(cost_price) 
    count_day = len(cost_price)

    if 0 in counter_room:
        return False
    else:
        return count_cost_day, count_day

