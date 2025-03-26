# Human Times
Super simple python class to generate times in an easily digestible format.

I created this to provide nice ETA's in my python projects.

## Install:
`pip3 install humantimes`

## Usage:
```
>>> from humantimes import HumanTimes
>>> HumanTimes().get(5400)
'1 Hour 30 Minutes'
>>> HumanTimes().get(7_200_000)
'2 Months 3 Weeks'
>>> HumanTimes().get(100_000_000_000)
'3170 Years 0 Months'
```
