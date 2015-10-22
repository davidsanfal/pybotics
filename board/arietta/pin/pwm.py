import os

class PWM(object):

    def __init__(self, port, period=0, duty_cycle=0):
        
        self.port = port
        self.path = "/sys/class/pwm/pwmchip0/pwm%s" % self.port
        if not os.path.exists("/sys/class/pwm/pwmchip0/pwm%s" % port):
            os.system("echo %s > /sys/class/pwm/pwmchip0/export" % port)
        self.period = period
        self.duty_cycle = duty_cycle
        self.enable = 1

    @property
    def enable(self):
        self._write("enable", 1)
 
    @property
    def disable(self):
        self._write("enable", 0)

    @property
    def status(self):
        self._read("enable")
    
    @property
    def period(self):
        return self._read("period")

    @period.setter
    def period(self, period):
        if self.duty_cycle >= period:
            self._write("period", period)

    @property
    def duty_cycle(self):
        return self._read("duty_cycle")

    @duty_cycle.setter
    def duty_cycle(self, period):
        self._write("duty_cycle", period)


    def _read(self, data):
        with open(os.path.join(self.path, data), 'r') as f:
            return f.read()

    def _write(self, data, value):
        with open(os.path.join(self.path, data), 'r+') as f:
            f.write(value)