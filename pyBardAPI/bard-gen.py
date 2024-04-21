# uses browser_cookie3 - install with `pip install browser-cookie3`
# uses BardCookies - install with `pip install bardapi`

import browser_cookie3
from bardapi import BardCookies
import json
import time
import random

# Load cookies from Chrome
cookies = browser_cookie3.opera_gx()

def getCookieValue(key):
    for cookie in cookies:
        if cookie.name == key:
            return(cookie.value)
            break
    return 0

def generate_id():
    epoch_time = int(time.time())
    random_hex = format(random.randint(0, 0xFFFF), "04x")
    result = f"{epoch_time}-{random_hex}"
    return result

def generateTags():
    coreTags = ["Home Gardening"]
    additional = ["Senior gardening","Gardening for older adults","Accessible gardening","Low-maintenance gardens","Raised bed gardening","Container gardening","Fall/winter/spring/summer gardening","Gardening on a budget","Therapeutic gardening","health and well-being","Herbs for seniors","Flowers for beginners","Shade-loving plants","Drought-tolerant plants","Pollinator-attracting plants","Fragrant plants","Edible plants","Medicinal plants","Native plants","Easy-to-grow plants","Seed starting","Composting","Pruning","Planting","Weeding","Birdwatching","Butterfly gardening","Sensory gardening","DIY gardening projects","Crafts with natural materials","Mental health and gardening","Mindfulness and gardening","Physical activity and gardening","Gardening for memory care","Social gardening","Gardening communities","Gardening tips for grandchildren","Gardening in small spaces","Sustainable gardening", "Eco-friendly gardening"]
    minCount = 2
    maxCount = 4
    selectedCount = random.randint(minCount, maxCount)
    chosenTags = random.sample(additional, selectedCount)
    finalTags = coreTags + chosenTags
    return finalTags

def main():
    cookie_dict = {
        "__Secure-1PSID": getCookieValue("__Secure-1PSID"),
        "__Secure-1PSIDTS": getCookieValue("__Secure-1PSIDTS"),
        "__Secure-1PSIDCC": getCookieValue("__Secure-1PSIDCC"),
        "NID": getCookieValue("NID"),
    }
    
    bard = BardCookies(cookie_dict=cookie_dict)
    #prompt = "Please write a 200 word article for older people about the topic of outdoor home gardening in winter time. present the answer in the following JSON format {title: \"<<Name of the Article>>\", body: [\"<<Text of the article, Paragraph 1>>\", \"Paragraph 2\", \"Paragraph 3\"]} Do not give any confirmation messages such as \"Sure, here is a 200-word article\" or \"I hope you enjoy this article\" and do not add in any other html formatting such as new lines, <p> or bold. Plain text only"
    tags = generateTags()
    tagsStr = ", ".join(tags)
    prompt = "Please write a 200 word article using the following tags for inspiration: " + tagsStr + ". present the answer in the following JSON format {\"title\": \"<<Name of the Article>>\", \"body\": [\"<<Text of the article, Paragraph 1>>\", \"Paragraph 2\", \"Paragraph 3\"]} Do not give any confirmation messages such as \"Sure, here is a 200-word article\" or \"I hope you enjoy this article\" and do not add in any other html formatting such as new lines, <p> or bold. Plain text only. Make sure it is a correct JSON object that can be interpreted correctly by a computer. Ensure all opening and closing curly braces are matched as well as square brackets. Any carriage returns should be repesented by \\n "
    
    print(prompt)
    print("")
    #answer = '{"title": "Gardening Through the Chill: Winter Delights for Your Outdoor Haven", "body": ["As the brisk air settles in and leaves dance in fiery hues, many gardens transform into quiet landscapes. But for the green-thumbed adventurer, winter presents a unique opportunity to cultivate resilience and harvest hidden joys. Fear not the frost, fellow nature enthusiasts! Let\'s explore the magic of winter outdoor gardening.", "With a shift in mindset, your garden can become a wonderland of textures and pops of color. Pansies and violas unfurl their cheerful faces, braving the cold with vibrant petals. Evergreen shrubs like holly and juniper add structure and depth, their rich greens a stark contrast to the snow. Don\'t forget the humble winterberry, its fiery berries like tiny embers against the bare branches.", "Embrace the season\'s bounty. Harvest herbs like rosemary and thyme, their flavors intensified by the chill. Plant garlic cloves for a spring bounty, their pungent aroma a promise of warmer days. Tend to your dormant perennials, ensuring they slumber soundly beneath a protective blanket of mulch. Remember, winter is not an ending, but a pause, a time to nurture and plan for the vibrant symphony of spring."]}'
    #ok answer = '{"title": "Gardening Through the Chill: Winter Delights for Your Outdoor Haven", "body": ["As the brisk air settles in and leaves dance in fiery hues, many gardens transform into quiet landscapes. But for the green-thumbed adventurer, winter presents a unique opportunity to cultivate resilience and harvest hidden joys. Fear not the frost, fellow nature enthusiasts!", "ok"]}'
    answer = bard.get_answer(prompt)['content']
    #answer = answer.replace("\n", "\\n")
    print(answer)
    print("")

    final = json.loads(answer)
    final["id"] = generate_id()
    final["createdAt"] = int(time.time())
    final["tags"] = tags
    print(final)
    filename = final["id"] + ".json"

    with open("articles/"+filename, "w") as file: 
        file.write(json.dumps(final))
        print("File written to " + filename)



main()
