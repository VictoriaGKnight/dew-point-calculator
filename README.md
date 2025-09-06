# Dew Point Calculator 

A Python program that prompts the user for relative humidity (%) and temperature (°C), validates inputs, and computes the dew point using the Magnus formula.

## Features
- Input validation:
  - **Relative humidity:** 1–100%
  - **Temperature (°C):** -40 to 60
- Clear, user-friendly prompts and error messages
- Accurate dew point calculation for common atmospheric conditions

## Formula (Magnus)
\[
\gamma(T, RH) = \frac{aT}{b + T} + \ln(RH)
\quad\Rightarrow\quad
T_d = \frac{b \cdot \gamma}{a - \gamma}
\]
Where \(a = 17.62\), \(b = 243.12^\circ C\), \(T\) in °C, and \(RH\) as a fraction (0–1).

## Run Locally
```bash
python dew_point.py

