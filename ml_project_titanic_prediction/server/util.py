import json
import pickle
import numpy as np

__data_columns = None
__model = None
__scaler = None


def load_saved_artifacts():
    print("loading saved artifacts... start")
    global __data_columns
    global __model
    global __scaler

    # load columns
    with open("./artifacts/titanic_columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    # load model
    with open("./artifacts/titanic_model.pickle", "rb") as f:
        __model = pickle.load(f)

    with open("./artifacts/titanic_scaler.pickle", "rb") as f:
        __scaler = pickle.load(f)

    print("loading saved artifacts... done")


def get_columns():
    return __data_columns


def get_prediction(pclass, age, sibsp, parch, fare, sex, embarked):
    x = np.zeros(len(__data_columns))

    if sex == "female":
        sex_female = True
    else:
        sex_female = False

    if embarked == 'Q':
        embarked_Q = True
        embarked_S = False
    elif embarked == 'S':
        embarked_Q = False
        embarked_S = True
    else:
        embarked_Q = False
        embarked_S = False

    x[0] = pclass
    x[1] = age
    x[2] = sibsp
    x[3] = parch
    x[4] = fare
    x[5] = sex_female
    x[6] = embarked_Q
    x[7] = embarked_S

    x = __scaler.transform(x.reshape(1, -1))

    return __model.predict(x)[0]


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_columns())
    print(get_prediction(3, 22, 1, 0, 7.25, "male", "S"))
    print(get_prediction(1, 38, 1, 0, 71.2833, "female", "C"))
    print(get_prediction(3, 35, 0, 0, 8.4583, "male", "Q"))
    print(get_prediction(3,	27.0, 0, 2, 11.1333, "female", "S"))
    print(get_prediction(1, 58.0, 0, 0, 26.5500, "female", "S"))
    print("Answer: 0 1 0 1 1")
