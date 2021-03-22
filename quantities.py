import json


class Quantity:

    folder = "Quantities"

    def __init__(self, quantity_name):
        self.name = quantity_name
        self.filename = self._get_filename(self.name)
        self.file_location = Quantity.folder + "/" + self.filename
        self.quantity_dict = self._get_quantity_dict()

        self.units = self.quantity_dict["units"].keys()
        self.initial_values = [
            self.quantity_dict["initial values"]["left value"],
            self.quantity_dict["initial values"]["right value"]
        ]
        self.initial_units = [
            self.quantity_dict["initial units"]["left unit"],
            self.quantity_dict["initial units"]["right unit"]
        ]

    @staticmethod
    def _get_filename(quantity_name):
        filename = ""

        if quantity_name == "Area":
            filename = "area.json"
        elif quantity_name == "Data Transfer Rate":
            filename = "data_transfer_rate.json"
        elif quantity_name == "Digital Storage":
            filename = "digital_storage.json"
        elif quantity_name == "Energy":
            filename = "energy.json"
        elif quantity_name == "Frequency":
            filename = "frequency.json"
        elif quantity_name == "Fuel Economy":
            filename = "fuel_economy.json"
        elif quantity_name == "Length":
            filename = "length.json"
        elif quantity_name == "Mass":
            filename = "mass.json"
        elif quantity_name == "Plane Angle":
            filename = "plane_angle.json"
        elif quantity_name == "Pressure":
            filename = "pressure.json"
        elif quantity_name == "Speed":
            filename = "speed.json"
        elif quantity_name == "Temperature":
            filename = "temperature.json"
        elif quantity_name == "Time":
            filename = "time.json"
        elif quantity_name == "Volume":
            filename = "volume.json"
        else:
            raise ValueError

        return filename

    def _get_quantity_dict(self):

        with open(self.file_location, "r") as file:
            quantity_dict = json.load(file)

        return quantity_dict

    def convert(self, value, unit, to_unit):
        formula = self.quantity_dict["units"][unit]["convert to"][to_unit]["formula"]

        # value variable is inside formula text
        answer = eval(formula)

        return answer

    def get_solution_text(self, value, unit, answer, to_unit):
        solution_text_format = self.quantity_dict["units"][unit]["convert to"][to_unit]["solution text"]
        solution_text = solution_text_format

        if "{value}" in solution_text:
            solution_text.replace("{value}", str(value))
        if "{answer}" in solution_text:
            solution_text.replace("{answer}", str(answer))

        return solution_text
