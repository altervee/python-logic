let character = "#";
for (let i = 0; i < 7; i++) {
    console.log(character);
    character += "#";
}
// Output:
// #
// ##
// ###
// ####
// #####
// ######
// #######

// FizzBuzz
for (let i = 1; i <= 100; i++) {
    let output = "";
    if ((i % 3 == 0)&&(i % 5 == 0)) output += "FizzBuzz";
    else if (i % 3 == 0) output += "Fizz";
    else output = i
    console.log(output);
}
// chessboard
let size = 8;
let board = ""; 
for (let i=0; i<size;i++){
    for (let j=0; j<size;j++){
        if ((i+j)%2==0) board += " ";
        else board += "#";
    }
    board += "\n";
    console.log(board);
}
