
import math

A = 17.62   
B = 243.12

def input_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = float(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                if min_val is not None and max_val is not None:
                    print(f"Please enter a value between {min_val} and {max_val}.")
                elif min_val is not None:
                    print(f"Please enter a value ≥ {min_val}.")
                else:
                    print(f"Please enter a value ≤ {max_val}.")
                continue
            return val
        except ValueError:
            print("That doesn't look like a number. Try again.")

def dew_point_c(temp_c: float, rh_percent: float) -> float:
    rh = max(0.0001, min(0.9999, rh_percent / 100.0))
    gamma = (A * temp_c) / (B + temp_c) + math.log(rh)
    td = (B * gamma) / (A - gamma)
    return td

if __name__ == "__main__":
    print("Dew Point Calculator")
    print("— Enter relative humidity (%) and temperature (°C) —")
    print("Valid ranges: RH 1–100%, Temperature -40 to 60 °C\n")

    rh = input_float("Enter relative humidity (%): ", 1, 100)
    temp_c = input_float("Enter temperature (°C): ", -40, 60)

    td = dew_point_c(temp_c, rh)
    print(f"\nFor {rh:.1f}% RH at {temp_c:.1f} °C, the dew point is {td:.2f} °C.")
