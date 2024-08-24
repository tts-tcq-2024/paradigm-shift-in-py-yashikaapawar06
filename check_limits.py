class Reporter:
    def report(self, message):
        raise NotImplementedError("Subclass must implement abstract method")

class PrintReporter(Reporter):
    def report(self, message):
        print(message)

class LoggerReporter(Reporter):
    def __init__(self, logger):
        self.logger = logger

    def report(self, message):
        self.logger.error(message)

def check_value_in_range(value, min_value, max_value, parameter_name, reporter):
    if value < min_value:
        reporter.report(f'{parameter_name} is too low! Value: {value}')
        return False
    if value > max_value:
        reporter.report(f'{parameter_name} is too high! Value: {value}')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate, reporter):
    temp_ok = check_value_in_range(temperature, 0, 45, 'Temperature', reporter)
    soc_ok = check_value_in_range(soc, 20, 80, 'State of Charge', reporter)
    charge_rate_ok = check_value_in_range(charge_rate, 0, 0.8, 'Charge Rate', reporter)
    return temp_ok and soc_ok and charge_rate_ok
    
if __name__ == '__main__':
    reporter = PrintReporter()
    assert(battery_is_ok(25, 70, 0.7) is True) #All parameters within range
    assert(battery_is_ok(50, 85, 0) is False) #Temperature and SOC out of range
    assert(battery_is_ok(-2,40,0.9) is False) #All parameters are out of range
    assert(battery_is_ok(0,20,0.8) is True) #Edge values but within range
