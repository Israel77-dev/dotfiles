from libqtile import widget

from libqtile.widget.battery import BatteryState

class MyBacklight(widget.Backlight):
    def poll(self) -> str:
        info = self._get_info()
        if info is False:
            return '---'
        self._perc = int(info * 100)
        char = '☼'
        #self.layout.colour = color_alert
        return '{} {}%'.format(char, self._perc)  # chr(0x1F50B))
    
    @property
    def brightness_value(self) -> int:
        return int(self._get_info() * 100)
    
    @brightness_value.setter
    def brightness_value(self, value: int) -> None:
        self._change_backlight(value)
    
    def increase_brightness(self, step: int):
        self.brightness_value += step

    def decrease_brightness(self, step: int):
        self.brightness_value -= step


class MyBattery(widget.Battery):
    def poll(self) -> str:
        status = self._battery.update_status()
        
        percent = status.percent
        symbol = ""
        charging = ""

        if status.state == BatteryState.CHARGING:
            charging = "ﮣ"

        if percent >= .95:
            symbol = ""
        elif percent >= .90:
            symbol = ""
        elif percent >= .80:
            symbol = ""
        elif percent >= .70:
            symbol = ""
        elif percent >= .60:
            symbol = ""
        elif percent >= .50:
            symbol = ""
        elif percent >= .40:
            symbol = ""
        elif percent >= .30:
            symbol = ""
        elif percent >= .20:
            symbol = ""
        else:
            symbol = ""

        return "{} {:.0f}% {}".format(symbol, percent * 100, charging)
