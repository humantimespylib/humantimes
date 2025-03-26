#!/usr/bin/env python3
#URL: https://github.com/humantimespylib/humantimes
#CreationDateTime: Wed 25 Mar 04:28 GMT
class HumanTimes:
	def get(self, timeStamp: int or float) -> str:
		if timeStamp < 0: # invert negative numbers
			timeStamp = timeStamp * -1

		if timeStamp < self.deltas['minute']: #less than  1 minute
			timeString = f"{round(timeStamp, 2)} Seconds"
		elif timeStamp < self.deltas['hour']: #less than 1 hour
			timeString = f"{round(timeStamp // self.deltas['minute'])} Minutes {round(timeStamp % self.deltas['minute'])} Seconds"
		elif timeStamp < self.deltas['day']: #less than 1 day
			timeString = f"{round(timeStamp // self.deltas['hour'])} Hours {round(timeStamp // self.deltas['minute'] % self.deltas['minute'])} Minutes"
		elif timeStamp < self.deltas['week']: #less than 1 week
			timeString = f"{round(timeStamp // self.deltas['day'])} Days {round(timeStamp // self.deltas['hour'] % 24)} Hours"
		elif timeStamp < self.deltas['month']: #less than 1 month
			timeString = f"{round(timeStamp // self.deltas['week'])} Weeks {round(timeStamp // self.deltas['day'] % 7)} Days"
		elif timeStamp < self.deltas['year']: #less than 365 days
			timeString = f"{round(timeStamp // self.deltas['month'])} Months {round(timeStamp // self.deltas['week'] % 4)} Weeks"
		else: # greater than 1 year
			timeString = f"{round(timeStamp // self.deltas['year'])} Years {round(timeStamp // self.deltas['month'] % 12)} Months"

		for key in self.deltas.keys(): # deplurify words like: "{deltaKey}s" into: "{deltaKey}"
			key = key.capitalize()
			pluralCorrectment = f"1 {key}s"

			if timeString.startswith(pluralCorrectment) or timeString.endswith(" " + pluralCorrectment):
				timeString = timeString.replace(pluralCorrectment, f"1 {key}")

		return timeString

	def __init__(self):
		self.deltas = {
			"year": 31536000,
			"month": 2592000,
			"week": 604800,
			"day": 86400,
		 	"hour": 3600 ,
			"minute": 60,
			"second": 1
		}
