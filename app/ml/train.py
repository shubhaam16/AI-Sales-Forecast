from sklearn.ensemble import RandomForestRegressor

class ModelTrainer:

    @staticmethod
    def train (x_train, y_train):
        model = RandomForestRegressor(n_estimators=200,random_state=42)
        model.fit(x_train,y_train)

        return model
    