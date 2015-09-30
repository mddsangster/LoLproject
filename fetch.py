import json
import urllib2
import time
import datetime
from utils import splitlist

class RiotObj(object):
	def load(self, json):
		self.__dict__ = json
    
class RiotClient(object):
	def __init__(self, api_key, realm = 'na', limit=True, max_per_ten_min=500, include_timestamp=True, summonerAPIVersion = "1.3", 
		championAPIVersion = "1.1", gameAPIVersion = "1.3", leagueAPIVersion = "2.3", statsAPIVersion = "1.2", teamAPIVersion = "2.2"):
		self.api_key = api_key
		self.realm = realm.lower()
		self._limit = limit 
		self._max_per_ten_min = max_per_ten_min
		self.include_timestamp = include_timestamp
		self.summonerAPIVersion = summonerAPIVersion
		self.championAPIVersion = championAPIVersion
		self.gameAPIVersion = gameAPIVersion
		self.leagueAPIVersion = leagueAPIVersion
		self.statsAPIVersion = statsAPIVersion
		self.teamAPIVersion = teamAPIVersion

		self._lastCallTime = time.time()
		self._numQueries = 0    
    
    
    def makeapicallonlist(self, url, lst, version):
        output = {}

        for group in splitlist(lst, 40):
            resp = self.makeapicall(url.replace('{}', ','.join([str(x) for x in group])), version)

            output = dict(output.items() + resp.items())

        return output
        
    
    def makeapicall(self, remainder, version):
        self.sleep()
        self._numQueries += 1

        url = "http://prod.api.pvp.net/api/lol/" + urllib2.quote(self.realm) + "/v" + urllib2.quote(version + remainder) + '?api_key=' + urllib2.quote(self.api_key)
        print "Calling: %s" % url
        return json.loads(urllib2.urlopen(url).read())
    
    
    
	
	