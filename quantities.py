

class Area:

    name = "Area"
    units = ["Square kilometer", "Square meter", "Square mile", "Square yard",
             "Square foot", "Square inch", "Hectare", "Acre"]
    initial_units = ["Square meter", "Square kilometer"]
    initial_values = ["1", "1e-6"]

    @staticmethod
    def convert(value, unit, to_unit):

        if unit in Area.units and to_unit in Area.units:

            # TODO: some answers if there is a limit in decimal places return 0
            # TODO: but if there isn't a limit, some answers have way too many decimal places
            # decimal_places = 4
            answer = 0

            if unit == "Square kilometer":
                if to_unit == "Square meter":
                    answer = value * 1000000
                elif to_unit == "Square mile":
                    answer = value / 2.59
                elif to_unit == "Square yard":
                    answer = value * 1.196e+6
                elif to_unit == "Square foot":
                    answer = value * 1.076e+7
                elif to_unit == "Square inch":
                    answer = value * 1.55e+9
                elif to_unit == "Hectare":
                    answer = value * 100
                elif to_unit == "Acre":
                    answer = value * 247
                else:
                    raise ValueError

            elif unit == "Square meter":
                if to_unit == "Square kilometer":
                    answer = value / 1e+6
                elif to_unit == "Square mile":
                    answer = value / 2.59e+6
                elif to_unit == "Square yard":
                    answer = value * 1.196
                elif to_unit == "Square foot":
                    answer = value * 10.764
                elif to_unit == "Square inch":
                    answer = value * 1550
                elif to_unit == "Hectare":
                    answer = value / 10000
                elif to_unit == "Acre":
                    answer = value / 4047
                else:
                    raise ValueError

            elif unit == "Square mile":
                if to_unit == "Square kilometer":
                    answer = value * 2.59
                elif to_unit == "Square meter":
                    answer = value * 2.59e+6
                elif to_unit == "Square yard":
                    answer = value * 3.098e+6
                elif to_unit == "Square foot":
                    answer = value * 2.788e+7
                elif to_unit == "Square inch":
                    answer = value * 4.014e+9
                elif to_unit == "Hectare":
                    answer = value * 259
                elif to_unit == "Acre":
                    answer = value * 640
                else:
                    raise ValueError

            elif unit == "Square yard":
                if to_unit == "Square kilometer":
                    answer = value / 1.196e+6
                elif to_unit == "Square meter":
                    answer = value / 1.196
                elif to_unit == "Square mile":
                    answer = value / 3.098e+6
                elif to_unit == "Square foot":
                    answer = value * 9
                elif to_unit == "Square inch":
                    answer = value * 1296
                elif to_unit == "Hectare":
                    answer = value / 11960
                elif to_unit == "Acre":
                    answer = value / 4840
                else:
                    raise ValueError

            elif unit == "Square foot":
                if to_unit == "Square kilometer":
                    answer = value / 1.076e+7
                elif to_unit == "Square meter":
                    answer = value / 10.764
                elif to_unit == "Square mile":
                    answer = value / 2.788e+7
                elif to_unit == "Square yard":
                    answer = value / 9
                elif to_unit == "Square inch":
                    answer = value * 144
                elif to_unit == "Hectare":
                    answer = value / 107639
                elif to_unit == "Acre":
                    answer = value / 43560
                else:
                    raise ValueError

            elif unit == "Square inch":
                if to_unit == "Square kilometer":
                    answer = value / 1.55e+9
                elif to_unit == "Square meter":
                    answer = value / 1550
                elif to_unit == "Square mile":
                    answer = value / 4.014e+9
                elif to_unit == "Square yard":
                    answer = value / 1296
                elif to_unit == "Square foot":
                    answer = value / 144
                elif to_unit == "Hectare":
                    answer = value / 1.55e+7
                elif to_unit == "Acre":
                    answer = value / 6.273e+6
                else:
                    raise ValueError

            elif unit == "Hectare":
                if to_unit == "Square kilometer":
                    answer = value / 100
                elif to_unit == "Square meter":
                    answer = value / 10000
                elif to_unit == "Square mile":
                    answer = value / 259
                elif to_unit == "Square yard":
                    answer = value * 11960
                elif to_unit == "Square foot":
                    answer = value * 107639
                elif to_unit == "Square inch":
                    answer = value * 1.55e+7
                elif to_unit == "Acre":
                    answer = value * 2.471
                else:
                    raise ValueError

            elif unit == "Acre":
                if to_unit == "Square kilometer":
                    answer = value / 247
                elif to_unit == "Square meter":
                    answer = value / 4047
                elif to_unit == "Square mile":
                    answer = value / 640
                elif to_unit == "Square yard":
                    answer = value * 4840
                elif to_unit == "Square foot":
                    answer = value * 43560
                elif to_unit == "Square inch":
                    answer = value * 6.273e+6
                elif to_unit == "Hectare":
                    answer = value / 2.471
                else:
                    raise ValueError

            # put so that method ALWAYS returns a float value
            if type(answer) == int:
                return float(answer)

            return answer

        else:
            raise ValueError

    @staticmethod
    def get_solution_text(value, unit, answer, to_unit):

        formula_text = ""

        if unit == "Square kilometer":
            if to_unit == "Square meter":
                formula_text = "multiply the area value by 1e+6"
            elif to_unit == "Square mile":
                formula_text = "divide the area value by 2.59"
            elif to_unit == "Square yard":
                formula_text = "multiply the area value by 1.196e+6"
            elif to_unit == "Square foot":
                formula_text = "for an approximate result, multiply the area value by 1.076e+7"
            elif to_unit == "Square inch":
                formula_text = "multiply the area value by 1.55e+9"
            elif to_unit == "Hectare":
                formula_text = "multiply the area value by 100"
            elif to_unit == "Acre":
                formula_text = "for an approximate result, multiply the area value by 247"
            else:
                raise ValueError

        elif unit == "Square meter":
            if to_unit == "Square kilometer":
                formula_text = "divide the area value by 1e+6"
            elif to_unit == "Square mile":
                formula_text = "divide the area value by 2.59e+6"
            elif to_unit == "Square yard":
                formula_text = "multiply the area value by 1.196"
            elif to_unit == "Square foot":
                formula_text = "multiply the area value by 10.764"
            elif to_unit == "Square inch":
                formula_text = "for an approximate result, multiply the area value by 1550"
            elif to_unit == "Hectare":
                formula_text = "divide the area value by 10000"
            elif to_unit == "Acre":
                formula_text = "for an approximate result, divide the area value by 4047"
            else:
                raise ValueError

        elif unit == "Square mile":
            if to_unit == "Square kilometer":
                formula_text = "multiply the area value by 2.59"
            elif to_unit == "Square meter":
                formula_text = "multiply the area value by 2.59e+6"
            elif to_unit == "Square yard":
                formula_text = "for an approximate result, multiply the area value by 3.098e+6"
            elif to_unit == "Square foot":
                formula_text = "for an approximate result, multiply the area value by 2.788e+7"
            elif to_unit == "Square inch":
                formula_text = "for an approximate result, multiply the area value by 4.014e+9"
            elif to_unit == "Hectare":
                formula_text = "for an approximate result, multiply the area value by 259"
            elif to_unit == "Acre":
                formula_text = "multiply the area value by 640"
            else:
                raise ValueError

        elif unit == "Square yard":
            if to_unit == "Square kilometer":
                formula_text = "divide the area value by 1.196e+6"
            elif to_unit == "Square meter":
                formula_text = "divide the area value by 1.196"
            elif to_unit == "Square mile":
                formula_text = "for an approximate result, divide the area value by 3.098e+6"
            elif to_unit == "Square foot":
                formula_text = "multiply the area value by 9"
            elif to_unit == "Square inch":
                formula_text = "multiply the area value by 1296"
            elif to_unit == "Hectare":
                formula_text = "for an approximate result, divide the area value by 11960"
            elif to_unit == "Acre":
                formula_text = "divide the area value by 4840"
            else:
                raise ValueError

        elif unit == "Square foot":
            if to_unit == "Square kilometer":
                formula_text = "for an approximate result, divide the area value by 1.076e+7"
            elif to_unit == "Square meter":
                formula_text = "divide the area value by 10.764"
            elif to_unit == "Square mile":
                formula_text = "for an approximate result, divide the area value by 2.788e+7"
            elif to_unit == "Square yard":
                formula_text = "divide the area value by 9"
            elif to_unit == "Square inch":
                formula_text = "multiply the area value by 144"
            elif to_unit == "Hectare":
                formula_text = "for an approximate result, divide the area value by 107639"
            elif to_unit == "Acre":
                formula_text = "divide the area value by 43560"
            else:
                raise ValueError

        elif unit == "Square inch":
            if to_unit == "Square kilometer":
                formula_text = "divide the area value by 1.55e+9"
            elif to_unit == "Square meter":
                formula_text = "for an approximate result, divide the area value by 1550"
            elif to_unit == "Square mile":
                formula_text = "for an approximate result, divide the area value by 4.014e+9"
            elif to_unit == "Square yard":
                formula_text = "divide the area value by 1296"
            elif to_unit == "Square foot":
                formula_text = "divide the area value by 144"
            elif to_unit == "Hectare":
                formula_text = "divide the area value by 1.55e+7"
            elif to_unit == "Acre":
                formula_text = "for an approximate result, divide the area value by 6.273e+6"
            else:
                raise ValueError

        elif unit == "Hectare":
            if to_unit == "Square kilometer":
                formula_text = "divide the area value by 100"
            elif to_unit == "Square meter":
                formula_text = "multiply the area value by 10000"
            elif to_unit == "Square mile":
                formula_text = "for an approximate result, divide the area value by 259"
            elif to_unit == "Square yard":
                formula_text = "for an approximate result, multiply the area value by 11960"
            elif to_unit == "Square foot":
                formula_text = "for an approximate result, multiply the area value by 107639"
            elif to_unit == "Square inch":
                formula_text = "multiply the area value by 1.55e+7"
            elif to_unit == "Acre":
                formula_text = "multiply the area value by 2.471"
            else:
                raise ValueError

        elif unit == "Acre":
            if to_unit == "Square kilometer":
                formula_text = "for an approximate result, divide the area value by 247"
            elif to_unit == "Square meter":
                formula_text = "for an approximate result, multiply the area value by 4047"
            elif to_unit == "Square mile":
                formula_text = "divide the area value by 640"
            elif to_unit == "Square yard":
                formula_text = "multiply the area value by 4840"
            elif to_unit == "Square foot":
                formula_text = "multiply the area value by 43560"
            elif to_unit == "Square inch":
                formula_text = "for an approximate result, multiply the area value by 6.273e+6"
            elif to_unit == "Hectare":
                formula_text = "divide the area value by 2.471"
            else:
                raise ValueError

        else:
            raise ValueError

        return formula_text


class DataTransferRate:
    name = "Temperature"
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    initial_units = ["Celsius", "Fahrenheit"]
    initial_values = ["0", "32"]


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

