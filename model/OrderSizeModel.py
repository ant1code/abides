import json
from pomegranate import GeneralMixtureModel


class OrderSizeModel:

    def __init__(self, pomegranate_model_json):
        with open(pomegranate_model_json, "rb") as f:
            model_json = json.dumps(json.load(f))

        self.model = GeneralMixtureModel.from_json(model_json)

    def sample(self, random_state):
        return round(self.model.sample(random_state=random_state))
