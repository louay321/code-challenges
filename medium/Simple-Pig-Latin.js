/*
--CODEWARS--

TASK :

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
*/

function pigIt(str){
  var notLetters = /^[!,.?]+$/;
  str = str.split(' ');
  for(var i =0; i < str.length; i++){
    if(str[i] != '!' && str[i] != '?' && str[i] != '.' && str[i] != ','){
      str[i] = str[i].substr(1)+ str[i].substr(0,1) + 'ay';}
    
  }
  str = str.join(' ');
  
  return str
}
