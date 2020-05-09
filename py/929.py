import re
import unittest

"""https://leetcode.com/problems/unique-email-addresses/"""


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        domains = {}
        for email in emails:
            user, domain = email.split("@")
            domains.setdefault(domain, set())
            clean_user = re.sub("\.", "", user).split("+")[0]
            domains[domain].add(clean_user)
        c = 0
        for l in domains.values():

            c += len(l)

        return c


class Tests(unittest.TestCase):
    def test_examples(self):
        o = Solution()
        o.numUniqueEmails(
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ]
        )


if __name__ == "__main__":
    unittest.main()
