# Problem Link: https://www.hackerrank.com/challenges/acm-icpc-team/problem


def totalTopics(p1, p2):
    count = 0
    for i in range(len(p1)):
        if p1[i] == '1' or p2[i] == '1':
            count += 1
    return count


def acmTeam(teams):
    topicArr = []
    for i in range(len(teams)):
        for k in range(i + 1, len(teams)):
            topicArr.append(totalTopics(teams[i], teams[k]))
    maxTopic = max(topicArr)
    maxTopicNum = topicArr.count(maxTopic)
    return [maxTopic, maxTopicNum]


team1 = ['10101', '11110', '00010']
team2 = ['10101', '11100', '11010', '00101']

print(acmTeam(team1))
