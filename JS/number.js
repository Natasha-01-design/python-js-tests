// Given a list containing n distinct numbers from 0 to n, find the missing number.

// Input: [3, 0, 1]

// Output: 2
// NOTE: No number limit
const numbers = [ 0,2,3,4,5,6];
const n= numbers.length;
const sumedNum= (n*(n+1))/2;
const currentSum= numbers.reduce((sumed,current)=>sumed+current,0);
const missingNumber = sumedNum - currentSum;
console.log(missingNumber); 
