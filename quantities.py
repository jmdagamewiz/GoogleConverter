

class Area:
    pass


class DataTransferRate:
    pass


class DataStorage:
    pass


class Energy:
    pass


class Frequency:
    pass


class FuelEconomy:
    pass


class Length:
    pass


class Mass:
    pass


class PlaneAngle:
    pass


class Pressure:
    pass


class Speed:
    pass


class Temperature:

    name = "Temperature"
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    initial_units = ["Celsius", "Fahrenheit"]
    initial_values = ["0", "32"]

    @staticmethod
    def convert(value, unit, to_unit):
        """
        converts value with a unit to different unit
        :param value:
        :param unit:
        :param to_unit:
        :return:
        """

        if unit in Temperature.units and to_unit in Temperature.units:

            decimal_places = 4
            answer = 0

            if unit == "Celsius":
                if to_unit == "Fahrenheit":
                    answer = value * 9/5 + 32
                elif to_unit == "Kelvin":
                    answer = value + 273.15

            elif unit == "Fahrenheit":
                if to_unit == "Celsius":
                    answer = (value - 32) * 5/9
                if to_unit == "Kelvin":
                    answer = (value - 32) * 5/9 + 273.15

            elif unit == "Kelvin":
                if to_unit == "Celsius":
                    answer = value - 273.15
                elif to_unit == "Fahrenheit":
                    answer = (value - 273.15) * 9/5 + 32

            if answer == 0:
                return 0.0

            return round(answer, decimal_places)

        else:
            raise ValueError

    @staticmethod
    def get_solution_text(value, unit, answer, to_unit):

        formula_text = ""

        if unit == "Celsius":
            if to_unit == "Fahrenheit":
                formula_text = f"({value}°C × 9/5) + 32 = {answer}°F"
            elif to_unit == "Kelvin":
                formula_text = f"{value}°C + 273.15 = {answer}K"
            else:
                raise ValueError

        elif unit == "Fahrenheit":
            if to_unit == "Celsius":
                formula_text = f"({value}°F − 32) × 5/9 = {answer}°C"
            elif to_unit == "Kelvin":
                formula_text = f"({value}°F − 32) × 5/9 + 273.15 = {answer}K"
            else:
                raise ValueError

        elif unit == "Kelvin":
            if to_unit == "Celsius":
                formula_text = f"{value}K − 273.15 = {answer}°C"
            elif to_unit == "Fahrenheit":
                formula_text = f"({value}K − 273.15) × 9/5 + 32 = {answer}°F"
            else:
                raise ValueError

        else:
            raise ValueError

        return formula_text


class Time:
    pass


class Volume:
    pass

