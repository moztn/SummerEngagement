from common import *
  
class Checkin(SQLObject):
  duration = IntCol()
  note = StringCol()
  checkinDate = DateTimeCol()
  mozillian = ForeignKey('Mozillian')

class Mozillian(SQLObject):

  nickname = StringCol(unique=True)
  email = StringCol( unique = True)
  engagement = ForeignKey('Engagement')
  checkins = MultipleJoin('Checkin')


class Engagement(SQLObject):

  numberOfDays = IntCol()
  numberOfHours = IntCol()
  startingDay = DateCol()
