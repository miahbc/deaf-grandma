function deafGrandma(str) {
    let abc = "abcdefghijklmnopqrstuvwxyz"
    if (str === "") {
    console.log("WHAT?!")
    } else if (str.length > 0) {
// let arr = []
// arr.push(str)
// let arr2 = arr[0].split('')
// return abc
for (let i=0; i<str.length; i++) {
    if (abc.includes(str[i])) {
        console.log("SPEAK UP, KID!")
    } else {console.log("NO, NOT SINCE 1946!")}}

if (str.includes("GOODBYE")) {
    console.log("LEAVING SO SOON?")
}}
// console.log(abc)
// if (str2.includes())
}

console.log(deafGrandma(''));
console.log(deafGrandma('hello'));
console.log(deafGrandma('HELLO'));
console.log(deafGrandma('GOODBYE'));
console.log(deafGrandma('GOODBYE, GOODBYE'));


// Write a program which can imitate a Grandma who's hard of hearing and follows these constraints:

// If you don't input anything (just hit enter) she responds with WHAT?!

// If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!

// If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!

// The first time you say GOODBYE! she says LEAVING SO SOON?

// The second time you say GOODBYE! she says LATER, SKATER! and the program exits.