var book = require ("./lib/grades.js") .book;

for (i = 2; i < process.argv.length; i += 1){
  book.addGrade (parseInt(process.argv[i]))
};

console.log ("Average grade: " + book.getAverage());
