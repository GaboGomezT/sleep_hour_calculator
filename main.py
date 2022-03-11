from datetime import datetime, timedelta


def calculate(wake_up: datetime, desired_sleep=7):
    """
    As a first approach (I'm writing this before going to bed)
    I will get the target wake up hour and the amount of desired sleep hours
    which will be defaulted at 7 hours.
    Then I will count how many 90 min cycles are available and get the hour you need to sleep.
    """
    minutes_desired_sleep = desired_sleep * 60
    total_cycles = minutes_desired_sleep // 90
    return wake_up - timedelta(minutes=90 * (total_cycles+1))


if __name__ == "__main__":
    wake_up = "2022-03-11T06:15:00"
    wake_up = datetime. strptime(wake_up, '%Y-%m-%dT%H:%M:%S')
    print(calculate(wake_up))
