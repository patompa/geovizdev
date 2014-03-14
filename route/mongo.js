APIKEY = {'key':'n-qPGunpHvYeraLqFI552UMBuajf812z'};
function query(q,collection,callback) {
   var url = 'https://api.mongolab.com/api/1/databases/dbtest/collections/' + collection + '?apiKey=' + APIKEY['key'] + "&q=" + encodeURIComponent(JSON.stringify(q));
   $.getJSON(url, callback);
}

function getSentiment(box,val,callback) {
   var swlat = box.getSouthWest().lat();
   var swlon = box.getSouthWest().lng();
   var nelat = box.getNorthEast().lat();
   var nelon = box.getNorthEast().lng();
   query({"lat": {"$gt": swlat,"$lt":nelat},"lon": {"$gt":swlon,"$lt":nelon}},'sentiment',function (data) {
                //console.log(data);
                var sentiment = 0.0;
                for (var i=0; i< data.length; i++) {
                    //console.log("Got area sentiment: " + val + " " + data[i]['sentiment']);
                    sentiment += (data[i]['sentiment'] + 1.0) /2.0;
                }
                if (data.length > 0) {
                   sentiment = sentiment /data.length;
                } else {
                   sentiment = 0.5
                }
                callback(1-sentiment,val);
       });
}

var sentimentMap = {}
var sentimentsCollected = 0;
function getSentiments(boxes,callback) {
     sentimentMap = {};
     sentimentsCollected = 0;
     for (var i = 0; i< boxes.length; i++) {
         getSentiment(boxes[i],i,function (sentiment,index) {
              sentimentMap["" + index] = sentiment;      
              sentimentsCollected += 1;
              //console.log("Got sentiment " + sentiment + " for " + index);
              if (sentimentsCollected == boxes.length) {
                  callback(sentimentMap);
                  sentimentsCollected = 0;
              }
         });
     }
}

function getCrime(box,val,callback) {
   var swlat = box.getSouthWest().lat();
   var swlon = box.getSouthWest().lng();
   var nelat = box.getNorthEast().lat();
   var nelon = box.getNorthEast().lng();
   query({"lat": {"$gt": swlat,"$lt":nelat},"lon": {"$gt":swlon,"$lt":nelon}},'crime',function (data) {
                var crime = 0;
                var crimetext = [];
                var sep = "";
                for (var i=0; i< data.length; i++) {
                    crime += 1;
                    crimetext.push(data[i]);
                    sep = "\n";
                }
                callback({'count':crime,'crimes':crimetext},val);
       });
}

var crimeMap = {}
var crimesCollected = 0;
function getCrimes(boxes,callback) {
     crimeMap = {};
     crimesCollected = 0;
     for (var i = 0; i< boxes.length; i++) {
         getCrime(boxes[i],i,function (crime,index) {
              crimeMap["" + index] = crime;
              crimesCollected += 1;
              if (crimesCollected == boxes.length) {
                  callback(crimeMap);
                  crimesCollected = 0;
              }
         });
     }
}
