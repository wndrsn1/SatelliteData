import os

os.chdir('/nfsscratch/Users/wndrsn')
access_token = ''


def Download_data():    
    days = ['00' + str(_) for _ in range(1,10)] + ['0' + str(_) for _ in range(10,100)] + [str(_) for _ in range(100,366)]
    years = ['2019','2020','2021','2022','2023']
    for year in years:
        for day in days:
            command_1 = f'wget -e robots=off -m -np -R .html,.tmp -nH --cut-dirs=3 "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD06_L2/{year}/{day}/" --header "Authorization: Bearer {access_token}" -P .'
            command_2 = f'wget -e robots=off -m -np -R .html,.tmp -nH --cut-dirs=3 "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD06_L2/{year}/{day}/" --header "Authorization: Bearer {access_token}" -P .'
            os.system(command_1)
            os.system(command_2)
