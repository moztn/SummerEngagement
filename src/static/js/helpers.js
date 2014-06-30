/*
   This file contains some helper function and data structures.
*/


/*
   aRawEngagement is optional.
*/
function createMozillian(aRawMozillian, aRawEngagement) {
  var tmp_duration = 0;
  var rawCheckins = aRawMozillian.checkins;
  var tmp_checkins = new Array();

  for(var i = 0; i < rawCheckins.length;i++){
    var rawCheckin = aRawMozillian.checkins[i];

    // We update duration at the same time.
    tmp_duration += rawCheckin.duration;

    tmp_checkins.push(createCheckin(rawCheckin));

  }


  var struct = {
    id: aRawMozillian.id,
    nickname: aRawMozillian.nickname,
    email: aRawMozillian.email,
    duration: tmp_duration,
    checkins: tmp_checkins,
    engagement: typeof aRawEngagement !== 'undefined' ? engagement(aRawEngagement) : null, // Since engagement is loaded sparetely
    getProgress: function() {
      if (this.engagement == null)
        return 0;
      return (this.duration / this.engagement.getTotalDuration())*100;
    }
  }

  return struct;
}

function createCheckin(aRawCheckin) {
  var struct = {
    id: aRawCheckin.id,
    duration: aRawCheckin.duration,
    datetime: new Date(aRawCheckin),
    note: aRawCheckin.note
  }

  return struct;
}

function createEngagement(aRawEngagement){
  var struct = {
    numberOfHours: aRawEngagement.numberOfHours,
    numberOfDays : aRawEngagement.numberOfDays,
    startingDay: aRawEngagement.startingDay,
    getTotalDuration: function() {
      return numberOfDays * numberOfHours;
    }
  }

  return struct;
}


