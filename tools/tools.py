from langchain_community.tools.tavily_search import TavilySearchResults

## MOCK this?
# def get_profile_url_tavily(name: str):
#     search = TavilySearchResults()
#     res = search.run(f"{name}")
#     return res[0]["url"]

#  This only returns an url, I have mocked this to stop using API limit requests, this is just studpid...
def get_profile_url_tavily(name: str):
    import random
    return random.choice(url_list)

url_list = [
    "https://x.com/edenemarco177?lang=enQuestion",
    "https://www.linkedin.com/today/author/eden-marco",
    "https://si.linkedin.com/in/eden-marco",
    "https://github.com/emarco177",
    "https://www.udemy.com/user/eden-marco/",
    "https://www.researchgate.net/profile/Eden-Marco",
    "https://twitter.com/edenemarco177?lang=en",
    "https://www.udemy.com/course/langchain/",
    "https://si.linkedin.com/in/edenmarco",
    "https://github.com/g-emarco",
    "https://www.udemy.com/user/eden-marco/",
    "https://brokenlink.no/nothing-here",
    # "https://www.vg.no",          # Verdens Gang
    # "https://www.dagbladet.no",   # Dagbladet
    # "https://www.aftenposten.no", # Aftenposten
    # "https://www.nrk.no",         # NRK (Norwegian Broadcasting Corporation)
    # "https://www.tv2.no",         # TV 2
    # "https://www.dn.no",          # Dagens Næringsliv
    # "https://www.nettavisen.no",  # Nettavisen
    # "https://www.ba.no",          # Bergensavisen
    # "https://www.bt.no",          # Bergens Tidende
    # "https://www.adressa.no",     # Adresseavisen
    ]