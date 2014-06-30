from common import *

class Checkin(SQLObject):
  duration = IntCol()
  note = StringCol()
  checkinDate = DateTimeCol()
  mozillian = ForeignKey('Mozillian')

  def toDict(self):
    return {'id':self.id, 'duration':self.duration, 'note':self.note,\
      'checkinDate':self.checkinDate.isoformat(), 'mozillian':self.mozillian.id}


class Mozillian(SQLObject, UserMixin):

  nickname = StringCol(unique=True)
  email = StringCol( unique = True)
  engagement = ForeignKey('Engagement')
  checkins = MultipleJoin('Checkin')

  def toDict(self):
    return { 'id':self.id, 'nickname':self.nickname, 'email':self.email,\
      'engagement':self.engagementID,\
      'checkins':map(lambda c: c.toDict(), Checkin.selectBy(mozillian = self.id))}

class Engagement(SQLObject):

  numberOfDays = IntCol()
  numberOfHours = IntCol()
  startingDay = DateCol()

  def toDict(self):
    return {'numberOfDays':self.numberOfDays, 'numberOfHours':self.numberOfHours,\
      'startingDay':self.startingDay.isoformat()}
