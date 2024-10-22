


def is_critically_balanced(neutronsEmissionPerSec,tempK):
    if tempK < 800 and neutronsEmissionPerSec > 500 and tempK*neutronsEmissionPerSec < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage,current,theoreticalMaxPower):
    generatedPower = voltage*current
    color = generatedPower/theoreticalMaxPower*100
    if color >= 80:
        return "zielony"
    elif color < 80 and color>=60:
        return "pomaranczowy"
    elif color <60 and color>=30:
        return "czerwony"
    elif color <30:
        return "czarny"


def fail_safe(tempK,neutronsEmissionPerSec,max):
    if tempK * neutronsEmissionPerSec < 0.9 * max:
        return "LOW"
    elif tempK * neutronsEmissionPerSec >= 0.9 * max and tempK * neutronsEmissionPerSec <= 1.1 * max:
        return "NORMAL"


