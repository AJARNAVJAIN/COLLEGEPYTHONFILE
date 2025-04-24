print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()  # Normalize time to make sure no negative values or overflow

    def normalize_time(self):
        # Normalize time so that seconds and minutes stay within their bounds
        if self.seconds >= 60:
            extra_minutes = self.seconds // 60
            self.seconds = self.seconds % 60
            self.minutes += extra_minutes
        if self.minutes >= 60:
            extra_hours = self.minutes // 60
            self.minutes = self.minutes % 60
            self.hours += extra_hours
        if self.hours < 0:
            self.hours = 0
        if self.minutes < 0:
            self.minutes = 0
        if self.seconds < 0:
            self.seconds = 0

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def total_seconds(self):
        """Returns total seconds of the time"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        """Add two Time objects."""
        total_seconds = self.total_seconds() + other.total_seconds()
        return Time.from_seconds(total_seconds)

    def __sub__(self, other):
        """Subtract two Time objects."""
        total_seconds = self.total_seconds() - other.total_seconds()
        return Time.from_seconds(total_seconds)

    @classmethod
    def from_seconds(cls, total_seconds):
        """Creates a Time object from total seconds."""
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def __lt__(self, other):
        """Less than comparison between two Time objects (for < operator)."""
        return self.total_seconds() < other.total_seconds()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.total_seconds() <= other.total_seconds()

    def __eq__(self, other):
        """Equality comparison."""
        return self.total_seconds() == other.total_seconds()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.total_seconds() > other.total_seconds()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.total_seconds() >= other.total_seconds()


# Example usage
if __name__ == "__main__":
    time1 = Time(2, 45, 50)  # 2 hours, 45 minutes, 50 seconds
    time2 = Time(1, 30, 25)  # 1 hour, 30 minutes, 25 seconds

    print("Time 1:", time1)
    print("Time 2:", time2)

    # Addition of two times
    added_time = time1 + time2
    print(f"\nTime 1 + Time 2 = {added_time}")

    # Subtraction of two times
    subtracted_time = time1 - time2
    print(f"Time 1 - Time 2 = {subtracted_time}")

    # Comparison of times
    if time1 > time2:
        print("\nTime 1 is greater than Time 2.")
    elif time1 < time2:
        print("\nTime 1 is less than Time 2.")
    else:
        print("\nTime 1 is equal to Time 2.")

    # Convert time to total seconds
    print(f"\nTotal seconds in Time 1: {time1.total_seconds()} seconds")
    print(f"Total seconds in Time 2: {time2.total_seconds()} seconds")
