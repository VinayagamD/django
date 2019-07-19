function hello() {
    console.log("Hello World!");
}

function helloYou(name){
    console.log("Hello "+name);
}

function addNum(num1,num2){
    console.log(num1+num2);
}

function helloSomeOne(name = "Frankie") {
    console.log("Hello "+name);
}

function formal(name = "Sam", title = "Sir") {
    // console.log(title+ " "+ name)
    return title +" "+name;
}

function timesFive(numInput) {
    return numInput * 5;
}

var v = "GLOBAL V";
var stuff = "GLOBAL STUFF";

function fun(stuff) {
    console.log(v);
    self.stuff = "Reassign stuff inside func";
    console.log(stuff);
    
}

fun();

console.log(stuff);
