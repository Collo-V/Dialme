teams1=["Arsenal","Man Utd","Man City","Chelsea","Totenham","Liverpool","Leicester","Westham","Leeds","Everton"]

n=0
while n<len(teams1):
    teams2=teams1
    teams2.remove(teams2[n])
    n+=1
    print(teams2)
    

