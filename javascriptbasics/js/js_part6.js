employee = {
  name : "Vinay Ganesh",
  job : "Programmer",
  age: 27,
  nameLength: function () {
       console.log(this.name.length);
  }
};


employee = {
  name : "Vinay Ganesh",
  job : "Programmer",
  age: 27, 
  report: function () {
      alert("Name is "+this.name+", Job is: "+this.job+", age is "+this.age+".");
  }
};


employee = {
  name : "Vinay Ganesh",
  job : "Programmer",
  age: 27,
  lastName: function () {
      console.log(this.name.split(" ")[1]);
  }
};


