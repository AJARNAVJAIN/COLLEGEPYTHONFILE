print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
class Weather:
    def __init__(self, temperature, humidity, wind_speed):
        # Initialize weather parameters
        self.weather_params = {
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
        }

    def __str__(self):
        """Returns a string representation of the weather parameters."""
        return f"Temperature: {self.weather_params['temperature']}°C, " \
               f"Humidity: {self.weather_params['humidity']}%, " \
               f"Wind Speed: {self.weather_params['wind_speed']} km/h"

    def __contains__(self, item):
        """Overloads the 'in' operator to check if an item is present in weather parameters."""
        return item in self.weather_params

# Example usage
if __name__ == "__main__":
    # Create a Weather object with specific parameters
    weather = Weather(temperature=22, humidity=60, wind_speed=15)

    print(f"Weather Data: {weather}")

    # Check if specific weather parameters are present using 'in' operator
    print("\nIs 'temperature' a weather parameter?", "temperature" in weather)
    print("Is 'rainfall' a weather parameter?", "rainfall" in weather)
    print("Is 'wind_speed' a weather parameter?", "wind_speed" in weather)
