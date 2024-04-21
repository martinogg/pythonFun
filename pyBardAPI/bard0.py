from bardapi import Bard

bard = Bard(token_from_browser=True)
response = bard.get_answer("Do you like cookies?")
print(response['content'])