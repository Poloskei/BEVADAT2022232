import pandas as pd


class NJCleaner:

    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        self.data.sort_values('scheduled_time', inplace=True)
        return self.data

    def drop_columns_and_nan(self):
        self.data.drop(['from', 'to'], axis=1, inplace=True)
        self.data.dropna(inplace=True)
        return self.data

    def convert_date_to_day(self):
        self.data['day'] = pd.to_datetime(self.data['date']).dt.day_name()
        self.data.drop('date', axis=1, inplace=True)
        return self.data

    def convert_scheduled_time_to_part_of_the_day(self):
        self.data['part_of_the_day'] = pd.to_datetime(self.data['scheduled_time'], format='%Y-%m-%d %H:%M:%S').dt.hour.apply(
            lambda x: 'early_morning' if 4 <= x <= 7 else 'morning' if 8 <= x <= 11 else 'afternoon' if 12 <= x <= 15 else
            'evening' if 16 <= x <= 19 else 'night' if 20 <= x <= 23 else 'late_night')
        self.data.drop('scheduled_time', axis=1, inplace=True)
        return self.data

    def convert_delay(self):
        self.data['delay'] = self.data['delay_minutes'].apply(lambda x: 1 if x >= 5 else 0)
        return self.data

    def drop_unnecessary_columns(self):
        self.data.drop(['train_id', 'actual_time', 'delay_minutes'], axis=1, inplace=True)
        return self.data

    def save_first_60k(self, save_path):
        self.data[:60000].to_csv(save_path, index=False)

    def prep_df(self, csv_path='NJ_pm.csv'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(csv_path)
        return self.data
