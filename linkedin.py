from linkedin import linkedin

APPLICATON_KEY    = '##############'
APPLICATON_SECRET = '################'

RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInAuthentication(
                    APPLICATON_KEY,
                    APPLICATON_SECRET,
                    RETURN_URL,
                    linkedin.PERMISSIONS.enums.values()
                )

authentication.authorization_code = '#############################################'
result = authentication.get_access_token()

print ("Access Token:", result.access_token)
print ("Expires in (seconds):", result.expires_in)

# Profile API, retrieves users profile
application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
{u'distance': 0,
 u'educations': {u'_total': 1,
  u'values': [{u'activities': u'This is my activity and society field',
    u'degree': u'graduate',
    u'endDate': {u'year': 2009},
    u'fieldOfStudy': u'computer science',
    u'id': 42611838,
    u'notes': u'This is my additional notes field',
    u'schoolName': u'\u0130stanbul Bilgi \xdcniversitesi',
    u'startDate': {u'year': 2004}}]},
 u'firstName': u'ozgur',
 u'id': u'COjFALsKDP',
 u'lastName': u'vatansever',
 u'location': {u'country': {u'code': u'tr'}, u'name': u'Istanbul, Turkey'},
 u'numConnections': 13}

 application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})
# Search URL is https://api.linkedin.com/v1/company-search:(companies:(name,universal-name,website-url))?keywords=apple%20microsoft

# Company api. Retrieves and displays one or more company profiles based on the 
# company ID or universal name. * Returns basic company profile data, such as 
# name, website, and industry.
{u'companies': {u'_count': 10,
  u'_start': 0,
  u'_total': 1064,
  u'values': [{u'name': u'Netflix',
    u'universalName': u'netflix',
    u'websiteUrl': u'httsp://netflix.com'},
   {u'name': u'Alliance Data',
    u'universalName': u'alliance-data',
    u'websiteUrl': u'www.alliancedata.com'},
   {u'name': u'GHA Technologies',
    u'universalName': u'gha-technologies',
    u'websiteUrl': u'www.gha-associates.com'},
   {u'name': u'Intelligent Decisions',
    u'universalName': u'intelligent-decisions',
    u'websiteUrl': u'https://www.intelligent.net'},
   {u'name': u'Mindfire Solutions',
    u'universalName': u'mindfire-solutions',
    u'websiteUrl': u'www.mindfiresolutions.com'},
   {u'name': u'Babel Media',
    u'universalName': u'babel-media',
    u'websiteUrl': u'https://www.babelmedia.com/'},
   {u'name': u'Milestone Technologies',
    u'universalName': u'milestone-technologies',
    u'websiteUrl': u'www.milestonepowered.com'},
   {u'name': u'Denali Advanced Integration',
    u'universalName': u'denali-advanced-integration',
    u'websiteUrl': u'www.denaliai.com'},
   {u'name': u'MicroAge',
    u'universalName': u'microage',
    u'websiteUrl': u'www.microage.com'},
   {u'name': u'TRUSTe',
    u'universalName': u'truste',
    u'websiteUrl': u'https://www.truste.com/'}]}}