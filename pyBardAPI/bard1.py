# https://github.com/dsdanielpark/Bard-API/tree/main#auto-cookie-bard

from bardapi import Bard

token22 = 'Ugh-PP7qku_d4WVRIYNOJujPIJqg5bM3ZUmUqYS5xAFJEjU3zW5zJiTl2p62OtJgSnCnPQ.'
bard = Bard(token=token22)
print(bard.get_answer("How can I advise my friend on the advantages of living a NEET lifestyle in less than 100 words?")['content']);
