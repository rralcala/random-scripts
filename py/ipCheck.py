import string


class Solution(object):
    hex_digits = set(string.hexdigits)

    NEITHER = "Neither"
    V4 = "IPv4"
    V6 = "IPv6"

    @staticmethod
    def is_hex(hex_string):
        for c in hex_string:
            if c not in Solution.hex_digits:
                return False
        return True

    def valid_ip_addr(self, ip):
        """
        :type ip: str
        :rtype: str
        """
        if "." in ip:
            return self.check4(ip)
        elif ":" in ip:
            return self.check6(ip)
        else:
            return self.NEITHER

    def check6(self, ip):
        octets = ip.split(":")
        if len(octets) != 8:
            return self.NEITHER
        for num in octets:
            if not (1 <= len(num) <= 4 and self.is_hex(num)):
                return self.NEITHER
        return self.V6

    def check4(self, ip):
        octets = ip.split(".")
        if len(octets) != 4:
            return self.NEITHER
        for num in octets:
            try:
                if not (1 <= len(num) <= 3 and 0 <= int(num) <= 255):
                    return self.NEITHER
            except Exception:
                return self.NEITHER
            if (num[0] == "0" and len(num) > 1) or num[0] == "-":
                return self.NEITHER
        return self.V4


if __name__ == "__main__":
    s = Solution()
    print(s.valid_ip_addr("01.01.01.01"))
    print(s.valid_ip_addr("123.145.132"))
    print(s.valid_ip_addr("123.145.132.234"))
    print(s.valid_ip_addr("0.0.0.255"))
    print(s.valid_ip_addr("0.0.0000.255"))
    print(s.valid_ip_addr("1e1.4.5.6"))
    print(s.valid_ip_addr("::1"))
    print(s.valid_ip_addr("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
    print(s.valid_ip_addr("2001:db8:85a3:0:0:8A2E:0370:7334"))
    print(s.valid_ip_addr("2001:db8:85a3:0:0:8A2E:0370:7334"))
    print(s.valid_ip_addr("0.0.0000.255"))
