/*
--CODEWARS--

TASK :
What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Preconditions:

Week starts on Monday.
Year is between 1583 and 4000.
Calendar is Gregorian.
Example:

mostFrequentDays(2427) => ['Friday']
mostFrequentDays(2185) => ['Saturday']
mostFrequentDays(2860) => ['Thursday', 'Friday']
*/

function mostFrequentDays (year) {
  var weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];
  var dayOne = new Date("January 01 " + year);
  var answer = [];
  answer.push(weekdays[dayOne.getDay()]);  
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    answer.push(weekdays[dayOne.getDay()+1]);
    if (answer[0] == 'Sunday') return ['Monday','Sunday'];
  }
  return answer;
}
