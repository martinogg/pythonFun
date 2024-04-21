from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "fQh-PJ8i3RoKdf_jOo9QGjm-H9whJlqDoGchsAk6VpQf5irumy61YANYOrGg8DFEvYPeLQ.",
    "__Secure-1PSIDTS": "sidts-CjEBPVxjSpDKeVO5ZhUANJXe11kg-flPZlPXvAnBrlh8Ey-ycif41KC0P1DEnwGWsDEnEAA",
    "__Secure-1PSIDCC":"ABTWhQENdhot30N_dvVsAvVo4vxv9qaMmfWrgGNlFI2AuCQy9G5FkcKYK4XzuvLBjO7FFZpARN0"
}

bard = BardCookies(cookie_dict=cookie_dict)

#print(bard.get_answer("Hello"))
#print(bard.get_answer("How can I advise my friend on the advantages of living a NEET lifestyle in less than 100 words?")['content']);
print(bard.get_answer("Please write a 200 word article for older people about the topic of outdoor home gardening in winter time. present the answer in the following JSON format {title: \"<<Name of the Article>>\", body: [\"<<Text of the article, Paragraph 1>>\", \"Paragraph 2\", \"Paragraph 3\"]} Do not give any confirmation messages such as \"Sure, here is a 200-word article\" or \"I hope you enjoy this article\" and do not add in any other html formatting such as <p> or bold. Plain text only")['content'])
