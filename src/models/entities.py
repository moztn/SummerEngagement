from common import *

class Checkin(SQLObject):
  duration = IntCol()
  note = StringCol()
  checkinDate = DateTimeCol()
  mozillian = ForeignKey('Mozillian')

  def toDict(self):
    return {'duration':self.duration, 'note':self.note,\
      'checkinDate':self.checkinDate, 'mozillian':self.mozillian}


class Mozillian(SQLObject):

  nickname = StringCol(unique=True)
  email = StringCol( unique = True)
  engagement = ForeignKey('Engagement')
  checkins = MultipleJoin('Checkin')

  def toDict(self):
    return {'nickname':self.nickname, 'email':self.email,\
      'engagement':self.engagement,\
      'checkins':map(lambda c: c.toDict(), Checkin.selectBy(mozillian = self.id))}


class Engagement(SQLObject):

  numberOfDays = IntCol()
  numberOfHours = IntCol()
  startingDay = DateCol()

  def toDict(self):
    return {'numberOfDays':self.numberOfDays, 'numberOfHours':self.numberOfHours,\
      'startingDay':self.startingDay}
