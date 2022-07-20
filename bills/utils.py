from datetime import timedelta,datetime


def validate_bill(data):
    json_data = []
    for num in range(1, len(data)):
        if any( '-' in str(item) or item == '' for item in data[num]):
            continue
        #convert date
        data[num][4] = datetime.fromordinal(datetime(1900, 1, 1)\
                               .toordinal() + data[num][4] - 2).date()
        #validate sum
        data[num][3]= float(str(data[num][3]).replace(',','.'))
        json_data.append(dict(zip(data[0],data[num])))
    return json_data