var getDieRoll = function(dieSize) {
	// console.log ("rolling a " + dieSize + " sided die");
	var result = Math.ceil(dieSize * Math.random())
	return result ;
};

var showResult = function () {
	console.log ("You rolled a " + firstDie + " on your first die");
	console.log ("You rolled a " + secondDie + " on your second die");
	console.log ("For a total of " + (firstDie + secondDie));
};

var firstDie = getDieRoll(6);
var secondDie = getDieRoll(6);
showResult () ;
