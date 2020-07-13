class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7,
                  "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        year = str(date[:-5:-1])[::-1]
        month = str(months[date[-8:-5]])
        month = month if len(month) == 2 else "0"+month
        day = str(date[-12::-1])[::-1]
        day = day if len(day) == 2 else "0"+day
        return year+"-"+month+"-"+day