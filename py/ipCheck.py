import string

class Solution(object):
    hex = set(string.hexdigits)

    NEITHER = "Neither"
    V4 = "IPv4"
    V6 = "IPv6"


    def isHex(self, hex_string):
        for c in hex_string:
            if c not in self.hex:
                return False
        return True

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if "." in IP:
            return self.check4(IP)
        elif ":" in IP:
            return self.check6(IP)
        else:
            return self.NEITHER
    def check6(self, ip):
        octets = ip.split(":")
        stillOk = True
        if len(octets) != 8:
            return self.NEITHER
        for num in octets:
            if not (1 <= len(num) <= 4 and self.isHex(num)):
                return self.NEITHER
        return self.V6

    def check4(self, ip):
        octets = ip.split(".")
        stillOk = True
        if len(octets) != 4:
            return self.NEITHER
        for num in octets:
            try:
                if not (1 <= len(num) <= 3 and 0 <= int(num) <= 255):
                    return self.NEITHER
            except:
                return self.NEITHER
            if (num[0] == '0' and len(num) > 1) or num[0] == '-':
                return self.NEITHER
        return self.V4


s = Solution()
print(s.validIPAddress("01.01.01.01"))
print(s.validIPAddress("123.145.132"))
print(s.validIPAddress("123.145.132.234"))
print(s.validIPAddress("0.0.0.255"))
print(s.validIPAddress("0.0.0000.255"))
print(s.validIPAddress("1e1.4.5.6"))
print(s.validIPAddress("::1"))
print(s.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(s.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"))
print(s.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"))
print(s.validIPAddress("0.0.0000.255"))

