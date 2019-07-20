let names = [];

operation = prompt("Would you to start route webapp? y/n");

while (operation === 'y'){
    performOperation(selectOption());

}

function performOperation(option){
    switch (option) {
        case "add":
            names.push(getName());
         break;
        case "remove":
            remove();
            break;
        case "display":
            displayList();
            break;
        case "quit":
            alert("Thanks for choosing our webapp");
            self.operation = "n";
           break;
        default:
            alert("You have chosen invalid option. Select valid option");
    }
}

function selectOption(){
   return  prompt("Please select  an action add, remove, display or quit");
}

function getName(){
    return prompt("What name would you like to add?");
}


function remove(){
    let remName = prompt("What name would you like to remove?");
    if(names.includes(remName)){
        let index = names.indexOf(remName);
        names.splice(index,1);
    }else {
        alert("The name " + remName + " is not present in the list. \n Please enter names present in the list shown:");
        displayList();
    }
}


function displayList() {
    let displayNames = "";
    names.forEach(function (name, index) {
        displayNames += name+ "\n";
    });
    alert("Names you have entered are : \n "+displayNames);
}
