from datetime import timedelta, datetime

pattern = '%H:%M'
start_time = datetime.strptime(input(), pattern)
end_time = datetime.strptime(input(), pattern)
current_time = start_time

for i in range((end_time - start_time + timedelta(minutes=10)) // timedelta(minutes=55)):
    print(f'{current_time.strftime(pattern)} - {(current_time + timedelta(minutes=45)).strftime(pattern)}')
    current_time = current_time + timedelta(minutes=55)
