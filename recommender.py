import pandas as pd
from surprise import SVD, Dataset, Reader

class TravelRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.reader = Reader(rating_scale=(1, 5))
        self.data = Dataset.load_from_df(self.df[['User ID', 'Destination', 'Rating']], self.reader)
        self.model = SVD()
        self.train_model()

    def train_model(self):
        trainset = self.data.build_full_trainset()
        self.model.fit(trainset)

    def get_recommendations(self, user_id="new_user", top_n=3):
        all_destinations = list(set(self.df['Destination']))
        predictions = [self.model.predict(user_id, dest) for dest in all_destinations]
        predictions.sort(key=lambda x: x.est, reverse=True)
        return [pred.iid for pred in predictions[:top_n]]
