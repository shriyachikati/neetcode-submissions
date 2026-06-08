import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set()
        for i, email in enumerate(emails):
            names = email.split('@')
            local_name = names[0].split('+')[0]
            local_name = local_name.replace('.', '')

            output.add(local_name + '@' + names[-1])

        return len(output)