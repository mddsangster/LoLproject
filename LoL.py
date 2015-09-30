##pip install leagueoflegends
a = 2

if a==1:

    from leagueoflegends import LeagueOfLegends, RiotError


    lol = LeagueOfLegends('587a0251-12ba-4600-86f1-0bc65b21cb57')


    ##587a0251-12ba-4600-86f1-0bc65b21cb57
    ##8e702b3f-50a7-437a-b825-18627375da3e


    # Call the API with explicit summoner ID
    id = lol.get_summoner_by_name('your-summoner-name')
    lol.get_games(id)


    # Or set the ID globally for all future calls

    lol.set_summoner('bruntbear')
    lol.get_summoner_stats()
    lol.get_summoner_ranked_stats()



    # Access data through dictionaries

    try:
        teams = lol.get_summoner_teams()
        for t in teams:
            print t["name"]
            for m in t["roster"]["memberList"]:
                id = m["playerId"]
                print id
                print lol.get_summoner_by_id(id)["name"]
    except RiotError, e:
        print e.error_msg
    
   
   
   
if a == 2:   
    import fetchLoL
    from utils import todict

    

    riot = fetchLoL.RiotClient("587a0251-12ba-4600-86f1-0bc65b21cb57")
    
    ##587a0251-12ba-4600-86f1-0bc65b21cb57
    ##8e702b3f-50a7-437a-b825-18627375da3e
    
#     summoner_ids = [x for x in range(100)]
#     summoner_names = riot.get_summoner_names(summoner_ids)
    summoners = [40669715, 39809419]
    namelol = riot.get_summoner_names(summoners[1])
    print namelol


#     client = pymongo.mongo_client.MongoClient()
#     db = client.pylol
#     db.mastery_pages.insert([todict(x) for x in mastery_listings])