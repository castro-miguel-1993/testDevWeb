import operator

def problemPadelLeague(datas):
    cleanList = cleanListMatches(datas)
    response = dict()
    for matchesInCategory in cleanList:
        matchesInCategory = matchesInCategory.strip()
        matches = matchesInCategory.split("\n")
        category = getCategory(matches)
        results = scoreByCategory(matches)
        results = sorted(results.items(), key=operator.itemgetter(1),reverse=True)

        if hasDraw(firstTeams=results):
            response[category]="EMPATE 0"
        else:
            response[category]=str(results[0][0])+" "+str(results[0][1])
    return response


def cleanListMatches(data):
    listdata = data.decode("utf-8") 
    listdata = listdata.strip()
    listdata = listdata.split("FIN")
    listdata.pop()
    return listdata

def scoreByCategory(matches):
    results = dict()
    for match in matches:
        result = match.split(" ")
        if len(result)>4:
            return JsonResponse("Datos sin formato adecuado.", status=400,safe=False)
            
        if localWin(match=result):            
            results = addScoreTeam(results,result,0,2)
            
            results = addScoreTeam(results,result,2,1)            
        else:            
            results = addScoreTeam(results,result,2,2)
            
            results = addScoreTeam(results,result,0,1)
    return results

def addScoreTeam(scoreTotal,match,indexTeam,score):
    team = match[indexTeam]
    if scoreTotal.get(team):
        scoreTotal[team]=scoreTotal.get(team) + score
    else:
        scoreTotal[team]=score
    return scoreTotal

def localWin(match):
    return match[1]>match[3]

def getCategory(matches):
    return matches.pop(0)

def hasDraw(firstTeams):
    return firstTeams[0][1] == firstTeams[1][1]