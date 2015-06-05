def tranFromIPToInt(strIP):
    lst = strIP.split(".")
    if len(lst) != 4:
        return "error ip"
    return int(lst[0]) * (256 ** 3) + int(lst[1]) * (256 ** 2) +\
           int(lst[2]) * 256 + int(lst[3])
def tranFromIntToIP(strInt):
    ip1 = 0
    ip2 = 0
    ip3 = 0
    ip4 = 0
    ip1 = int(strInt) / (256 ** 3)
    ip2 = (int(strInt) % (256 ** 3)) / (256 ** 2)
    ip3 = (int(strInt) % (256 ** 2)) / 256
    ip4 = int(strInt) % 256
    return str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
c=raw_input( "input 'b' for IP-->INT or 'a' for INT-->IP :")
if c=='a':
    x=raw_input('A int: ')
    print tranFromIntToIP(x)
elif c=='b':
    y=raw_input('A IP: ')
    print tranFromIPToInt(y)
