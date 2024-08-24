class Reporter:
    def report(self, message):
        raise NotImplementedError("Subclass must implement abstract method")

class PrintReporter(Reporter):
    def report(self, message):
        print(message)

def is_in_range(value, min_value, max_value):
    return min_value <= value <= max_value

def check_temperature(temperature, reporter):
    if not is_in_range(temperature, 0, 45):
        reporter.report(f'Temperature is out of range! Value: {temperature}')
        return False
    return True

def check_soc(soc, reporter):
    if not is_in_range(soc, 20, 80):
        reporter.report(f'State of Charge is out of range! Value: {soc}')
        return False
    return True

def check_charge_rate(charge_rate, reporter):
    if not is_in_range(charge_rate, 0, 0.8):
        reporter.report(f'Charge Rate is out of range! Value: {charge_rate}')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate, reporter):
    return all([
        check_temperature(temperature, reporter),
        check_soc(soc, reporter),
        check_charge_rate(charge_rate, reporter)
    ])
    
if __name__ == '__main__':
    reporter = PrintReporter()
    assert(battery_is_ok(25, 70, 0.7, reporter) is True) #All parameters within range
    assert(battery_is_ok(50, 85, 0, reporter) is False) #Temperature and SOC out of range
    assert(battery_is_ok(-2,40,0.9, reporter) is False) #All parameters are out of range
    assert(battery_is_ok(0,20,0.8, reporter) is True) #Edge values but within range
