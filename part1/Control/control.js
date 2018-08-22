var getDieRoll = function(dieSize) {
	var result = Math.ceil(dieSize * Math.random())
	return result ;
};

var roll = getDieRoll (6);

var things = ["pizza", "fish", "salad", "chips", "foo"];

for (var i = 0; i < things.length; i++){
	console.log(i);
}


for(var i = 0; i < 5; i += 1){
	console.log(roll);
	roll = getDieRoll(6);
}

if (roll >= 4){
	console.log (roll);
	console.log("*");
}
else {
	console.log (roll);
	console.log("-");
}
