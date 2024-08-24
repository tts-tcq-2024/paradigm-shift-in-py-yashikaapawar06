class Reporter:
    def report(self, message):
        raise NotImplementedError("Subclass must implement abstract method")

class PrintReporter(Reporter):
    def report(self, message):
        print(message)

def check_value_in_range(value, min_value, max_value, parameter_name, reporter):
    if value < min_value:
        reporter.report(f'{parameter_name} is too low! Value: {value}')
        return False
    if value > max_value:
        reporter.report(f'{parameter_name} is too high! Value: {value}')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate, reporter):
    parameters = {
        'Temperature': (temperature, 0, 45),
        'State of Charge': (soc, 20, 80),
        'Charge Rate': (charge_rate, 0, 0.8),
    }
    for param, (value, min_value, max_value) in parameters.items():
        if value < min_value:
            reporter.report(f'{param} is too low! Value: {value}')
            return False
        if value > max_value:
            reporter.report(f'{param} is too high! Value: {value}')
            return False

    return True
    
if __name__ == '__main__':
    reporter = PrintReporter()
    assert(battery_is_ok(25, 70, 0.7, reporter) is True) #All parameters within range
    assert(battery_is_ok(50, 85, 0, reporter) is False) #Temperature and SOC out of range
    assert(battery_is_ok(-2,40,0.9, reporter) is False) #All parameters are out of range
    assert(battery_is_ok(0,20,0.8, reporter) is True) #Edge values but within range
