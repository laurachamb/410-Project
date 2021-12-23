import twint
from datetime import datetime, timedelta
import time
from asyncio import new_event_loop, set_event_loop


# this interface does not use an API to grab data 
# Since our group could not acquire a dev account for twitter, we scraped the data with the help of twint
# More info on twint can be found here: https://github.com/twintproject/twint



# the purpose of getting today's date is to help determine the current month as well as the previous two months
# Example if today is 12/20/2021 then I will get data for the months Dec, Nov, Oct
# This can change depending on the scope of the project 


# this will create a list of dates, 2 dates per month which will later be used in comparisons to create 3 lists
# each list created in this project will represent one of the latest 3 months
def retDates(todaysDate):

    dateList = []
    dateList.append(todaysDate)

    firstOfMonth = todaysDate.replace(day=1)
    dateList.append(firstOfMonth)
    # get last day of previous month
    previousMonth = firstOfMonth - timedelta(days=1)
    dateList.append(previousMonth)
    # get first day of previous month
    previousMonthFirstDay = previousMonth.replace(day=1)
    dateList.append(previousMonthFirstDay)

    # get last day of the last month
    lastMonth = previousMonthFirstDay - timedelta(days=1)
    dateList.append(lastMonth)
    # get first day of last month
    lastMonthFirstDay = lastMonth.replace(day=1)
    dateList.append(lastMonthFirstDay)

    return dateList


def setUpCall():
    config = twint.Config()

    # this can be changed to any twitter username
    config.Username = "impactfinctr"
    # config.Username = "mcdonalds"

    # it seems that limits don't always work as expected, but it's better to leave a value than to not esp with very active accounts
    config.Limit = 10
    config.Store_object = True
    # running a search prints twitter info to the terminal, so uncomment this to disable 
    # config.Hide_output = True


    # Originally, I did not use a try/catch and the program was able to compile
    # However, I ended up having issues and after researching how to resolve I found this solution and the program worked again
    try:
        twint.run.Search(config)
    except twint.token.RefreshTokenException:
        time.sleep(10)
        twint.run.Search(config)

    tweets = twint.output.tweets_list
    print("exiting...")
    return tweets

def start_program():
    
    largeList =setUpCall()
    today = datetime.now()
    dateList = retDates(today)
    list1 = createMonthList(largeList,dateList[1],dateList[0])
    list2 = createMonthList(largeList,dateList[3],dateList[2])
    list3 = createMonthList(largeList,dateList[5],dateList[4])
    finalList = []
    finalList.append(largeList)
    finalList.append(list1)
    finalList.append(list2)
    finalList.append(list3)
   # print('=======================================================')
    #for x in list1:
    #    strMonth = datetime.strptime(x.datestamp, '%Y-%m-%d').date()
    #    print( str(strMonth) + " Likes: " + str(x.likes_count) + " id:" + x.id_str + " " + strMonth.strftime("%A"))

    #print('=======================================================')
    #for x in list2:
    #    strMonth = datetime.strptime(x.datestamp, '%Y-%m-%d').date()
    #    print( str(strMonth) + " Likes: " + str(x.likes_count) + " id:" + x.id_str + " " + strMonth.strftime("%A"))
    #print('=======================================================')
   # for x in list3:
    #    strMonth = datetime.strptime(x.datestamp, '%Y-%m-%d').date()
    #    print( str(strMonth) + " Likes: " + str(x.likes_count) + " id:" + x.id_str + " " + strMonth.strftime("%A"))
    # addData(list1)

    return finalList


# creates a list for an individual month
# needs the list of 
def createMonthList(entireList, firstDay, lastDay):
    testList = []

    
    first = firstDay.date()

    
    for x in range(len(entireList)):

        date = entireList[x].datestamp 
        # adding the .date() at the end converts datetime to date object
        
        date_object = datetime.strptime(date,'%Y-%m-%d')
        if firstDay<=date_object<=lastDay:
            testList.append(entireList[x])

    return testList


# function to add likes, replies, retweets
def addData(anyList):
    someList = []
    likes = 0
    replies = 0
    retweets = 0
    
    for x in range(len(anyList)):
        likes = anyList[x].likes_count + likes
        replies = anyList[x].replies_count + replies
        retweets = anyList[x].retweets_count + retweets
    
    someList.append(likes)
    someList.append(replies)
    someList.append(retweets)

    return someList

# get a list of str for last 3 months to print on HTML webpage
def strMonths(testList):
    strList = []
    str1 = testList[1][0].datestamp
    date_object1 = datetime.strptime(str1,'%Y-%m-%d')
    s1 = date_object1.strftime("%B")

    str2 = testList[2][0].datestamp
    date_object2 = datetime.strptime(str2,'%Y-%m-%d')
    s2 = date_object2.strftime("%B")
  
    str3 = testList[3][0].datestamp
    date_object3 = datetime.strptime(str3,'%Y-%m-%d')
    s3 = date_object3.strftime("%B")

    strList.append(s1)
    strList.append(s2)
    strList.append(s3)

    return strList

#print("about to start....does it work?")
#finalList = []
#finalList = start_program()

#info1 = addData(finalList[1])
#info2 = addData(finalList[2])
#info3 = addData(finalList[3])

#strList = []
#strList = strMonths(finalList)







#size = len(tweets1)

# sort that sorts the list based on # of likes
#sortedList = sorted(tweets, key=lambda x:x.likes_count,reverse=True)

# this is the general format 
#sortedList[0].likes_count

# displaying data, used for debugging
#for x in sortedList:
#    strMonth = datetime.strptime(x.datestamp, '%Y-%m-%d').date()
#    print( str(strMonth) + " Likes: " + str(x.likes_count) + " id:" + x.id_str + " " + strMonth.strftime("%A"))



