import re

def timeConversion(am_pm_format):
    am_pm_format = ' ' + am_pm_format

    if (bool(re.search('AM',am_pm_format))==True):
        for i in (("AM", " "), (" 12:", " 00:")):
            am_pm_format = am_pm_format.replace(*i)
    elif (bool(re.search('PM',am_pm_format))==True):
        for i in (("PM", " "), (" 01:", " 13:"), (" 02:", " 14:"), (" 03:", " 15:"), (" 04:", " 16:"), (" 05:", " 17:"), (" 06:", " 18:"), (" 07:", " 19:"), (" 08:", " 20:"), (" 09:", " 21:"), (" 10:", " 22:"), (" 11:", " 23:")):
            am_pm_format = am_pm_format.replace(*i)

    return am_pm_format.strip()


if __name__ == '__main__':
    am_pm_format = input("\nEnter time in 12-hour AM/PM format: ")
    result = timeConversion(am_pm_format)
    print(f"Conversion to military time is: {result}")
