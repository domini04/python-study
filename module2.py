class useful_functions:
    def __init__(self, name):
        self.name = name

    def tell_time(self):
        import datetime
        current_time = datetime.datetime.now()
        print(f"The current time is {current_time}")

    def tell_date(self):
        import datetime
        current_date = datetime.datetime.now()
        print(f"The current date is {current_date}")
