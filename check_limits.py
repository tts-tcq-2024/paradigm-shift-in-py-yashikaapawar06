from abc import ABC, abstractmethod

class Reporter(ABC):
    @abstractmethod
    def report(self, message):
        pass

class DetailedReporter(Reporter):
    def report(self, message):
        print(f'Detailed report:{message}')

def is_in_range(value, min_value, max_value):
    return min_value <= value <= max_value

def check_parameter(parameter_name, value, min_value, max_value, reporter):
    if value < min_value:
        reporter.report(f'{parameter_name} is too low! Value: {value}, Min: {min_value}')
        return False
    elif value > max_value:
        reporter.report(f'{parameter_name} is too high! Value: {value}, Max: {max_value}')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate, reporter):
    return all([
        check_parameter("Temperature", temperature, 0, 45, reporter),
        check_parameter("State of Charge", soc, 20, 80, reporter),
        check_parameter("Charge Rate", charge_rate, 0, 0.8, reporter)
    ])

if __name__ == '__main__':
    reporter = DetailedReporter()  
    assert(battery_is_ok(25, 70, 0.7, reporter) is True)
    assert(battery_is_ok(50, 85, 0, reporter) is False)
    assert(battery_is_ok(-2, 40, 0.9, reporter) is False)
    assert(battery_is_ok(0, 20, 0.8, reporter) is True)
