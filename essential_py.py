import os
import datetime as datetime

def verify_create_path(path):
    if (not os.path.exists(path)):
        os.makedirs(path)

def verify_create_log(log_path, string_input):
    try:
        if (not os.path.exists(log_path)):
            with open(log_path, 'w') as log:
                log.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] | [{string_input}] \n')
        else:
            with open(log_path, 'a') as log:
                log.write(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] | [{string_input}] \n')
    except Exception as e:
        print("Failed to verify or create log", e)

def wrout(stringData):
    log_dir = os.path.join(os.getcwd(), 'Logs')

    verify_create_path(log_dir)
    verify_create_log(f'{log_dir}\{datetime.datetime.today().strftime("%Y-%m-%d")}.txt', stringData)
