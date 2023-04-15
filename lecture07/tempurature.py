class Unphys_temp_err(Exception):
    def __init__(self, msg, temp):
        print(msg, temp)
        super().__init__(msg)


class High_temp_err(Exception):
    def __init__(self, msg, temp):
        print(msg, temp)
        super().__init__(msg)


def set():
    try:
        new_temp = float(input("Enter the temp: \n"))
        if new_temp <= 0:
            raise Unphys_temp_err(msg="too low", temp=new_temp)
        elif new_temp > 30:
            print("Warning")
            raise High_temp_err(msg="too high", temp=new_temp)

    except High_temp_err:
        f = open("temperature.log", mode="a")
        line = f"{new_temp}\n"
        f.write(line)
        f.close()
    return new_temp


if __name__ == "__main__":
    set()
