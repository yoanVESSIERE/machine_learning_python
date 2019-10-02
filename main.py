from fonction_model import Model, check

data = {
    "name": ["John", "Sam", "Edouard", "Sallie", "Kennie", "Ellie", "Tom", "Alexandre", "Peter", "Tim"],
    "feature": ["sick", "age"],
    "data": ["[1, 24]", "[0, 27]", "[1, 32]", "[0, 18]", "[1, 45]", "[0, 55]", "[0, 84]", "[1, 23]", "[1, 30]", "[0, 25]", "[1, 66]", "[0, 28]", "[1, 35]", "[0, 15]", "[1, 10]", "[0, 59]", "[0, 100]", "[1, 75]", "[1, 43]", "[1, 25]"],
    "target": ["Survived", "Dead"],
    "survived": [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
}

feature = data["data"]
feature_name = data["feature"]
label = data["survived"]
label_name = data["target"]

model = Model()
model.get_data(feature_name)
model.split_train_and_test(feature, label, train_size=0.6)
model.train()
model.test_model_prediction()
model.prediction()
model.accuracy(10)