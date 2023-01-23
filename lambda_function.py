
import requests
# from botocore.vendored import requests
from bs4 import BeautifulSoup
import json

#lambda function
def lambda_handler(event, context):
  # 'body': json.dumps(urls)
  
  
  urls = event['urls']

  url = "https://system.gotsport.com/org_event/events/18280/schedules?club=3694"
  html = getHtml(url)
  games = parseHtml(html)
  
  return {
        'statusCode': 200,
        'data':games
  }


def getHtml(url):
  try:
    webpage = requests.get(url)
    if webpage.status_code == 200:
      webpage_bs = BeautifulSoup(webpage.text, 'html.parser')
      # webpage_bs = BeautifulSoup(webpage.content, 'html.parser')
      # print("Success")
      # print(webpage_bs.prettify())
      return webpage_bs
    else:
      # print(webpage.status_code+" "+url)
      return webpage.status_code+" "+url
  except Exception as e:
    # print("requests does not work : "+url)
    return False
    

# <div class='hidden-xs'>
# <h4 class='text-muted'>Sunday, September 18, 2022</h4>
# <div class='table-responsive'>
# <table class='table table-bordered table-condensed table-hover'>
# <thead>
def parseHtml(html):
  games = []
  # <h4 class='text-center'>Wednesday, November 09, 2022</h4>
  datesTags = html.find_all("h4", {"class": "text-center"})
  dates = [d.text for d in datesTags]
  # print(len(dates), dates)

  # <table class='table table-bordered table-condensed table-hover'>
  gamesGroupedByDate = html.find_all("table", {"class": "table table-bordered table-condensed table-hover"})
  
  # print("gamesGroupedByDate", gamesGroupedByDate)
  #loop over dates, the index of date matches the index of gamesGroupedByDate
  for index, gamesInADate in enumerate(gamesGroupedByDate):
    # print("index",index, dates[index], gamesInADate)
    table_body = gamesInADate.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        game = {'date':dates[index], 
                'matchNum': cols[0],
                'time': cols[1].replace("\n\nScheduled",""),
                'home': cols[2].replace("Freehold SL Freehold SL ", ""),
                'result': cols[3],
                'away': cols[4].replace("Freehold SL Freehold SL ", ""),
                'location': cols[5],
                'division': cols[6],
                'homeGame': True if "Freehold SL" in cols[2] else False,
                'year': cols[6].split(" ")[0],
                'sex': cols[6].split(" ")[1]
               }
        if game['homeGame']:
          game['homeField'] = game['location'].split("-")[0].strip()
          game['homeFieldNum'] = game['location'].split("-")[1].strip()
        else:
          game['homeField'] = ''
          game['homeFieldNum'] = ''
        games.append(game)
      
    # print("games", len(games))
    #   for g in games:
    #     print(g)
    return games

url = "https://system.gotsport.com/org_event/events/18280/schedules?club=3694"
html = getHtml(url)
games = parseHtml(html)
