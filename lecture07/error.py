C = 2.99792458


class unphys_err(Exception):
    def __init__(self, msg, vel):
        print(msg, vel)
        super().__init__(msg)


def input_velocity():
    try:
        x = float(input("Enter velocity: \n"))
    except ValueError:
        print("oh no, QQ; there exist value errors")
        return None
    else:
        try:
            if x >= C:
                # raise RuntimeError("input velocity cannot be larger than C")
                raise unphys_err(msg="unphys error!!!", vel=x)
        except unphys_err as err:
            print("oh no, QQ; there runtime value errors\n")
            raise RuntimeError("another runtime error\n") from err
    finally:
        print("done")


def readData():
    try:
        f = open("test.txt", mode="r")
        l = f.readline()
        print(l)
        s = l.strip()
        val = int(s)
    except OSError as err:
        print("the error occurred, file not found.\n", err)
    except ValueError as err:
        print("the error occurred, cannot conver to int.\n", err)
    except:
        print("the error occurred!\n")
    else:
        print("print the else message")

    return None


if __name__ == "__main__":
    input_velocity()
    data = readData()
