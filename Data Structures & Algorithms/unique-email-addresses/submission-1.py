import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set()

        for email in emails:
            names = email.split('@')
            local_name = names[0].split('+')[0]
            local_name = local_name.replace('.', '')

            output.add(f'{local_name}@{names[-1]}')

        return len(output)