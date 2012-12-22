# A Tic Tac Toe Program

# 1.0 Do you want to play tic tac toe?

# 1.1 Assume the person wants to play...

$PlayAndPlayAndPlay = 1;

while ($PlayAndPlayAndPlay == 1) {

print ("Do you wish to play tic tac toe? Please answer Y or N\n");

# 2.0 Get answer

# 2.1 Get raw answer

$Answer = <STDIN>;

# 2.2 Filter out extraneous characters

chomp($Answer);

# 3.0 If answer is no, then say ok, goodbye

if ( $Answer eq "N" || $Answer eq "n") {

print ("Ok, goodbye!\n");

$PlayAndPlayAndPlay = 0;

last;

}

# 4.0 If answer is maybe, then say

# I need yes or no answer.

if ( $Answer ne "N" && $Answer ne "n" && $Answer ne "Y" && $Answer ne "y") {

print ("Give me a yes or no answer next time, please. Goodbye!\n");

}

# 5.0 If answer is yes,

if ( $Answer eq "Y" || $Answer eq "y") {

#

# 5.1 define board and favorite moves

@Board = (" ", " ", " ", " ", " ", " ", " ", " ", " ");

@BestMoves = (5, 1, 3, 7, 9);

# 5.2 tell person they will be x

print ("You will be X.\n");

# 5.3 tell person they will be first

print ("You will be first!\n");

# 5.3.5 while no winner, play

$Winner = 0;

while ( $Winner != 1 ) {

# 5.4 what is your next move?

# 5.5 get answer

$Answer = GetHumanMove();

# 5.6 put answer on board

$Position = $Answer - 1;

$Board[$Position] = "X";

DisplayBoard();

$Winner = CheckForWinner();

if ($Winner >=1) {last};

# 5.7 decide on computer's next move

$Answer = GetComputerMove();

$Position = $Answer - 1;

$Board[$Position] = "O";

# 5.8 put computer's move on board

DisplayBoard();

$Winner = CheckForWinner();

if ($Winner >= 1) {last};

}

if ($Winner ==1) {print ("X is a winner!!! \a\a\a\n")};

if ($Winner ==2) {print ("O is a winner!!! \n")};

}

}

######

# Subroutines

######

sub DisplayBoard {

print ("------------TOP----------------\n");

print ("|$Board[0]|$Board[1]|$Board[2]|\n");

print ("|$Board[3]|$Board[4]|$Board[5]|\n");

print ("|$Board[6]|$Board[7]|$Board[8]|\n");

print ("----------BOTTOM---------------\n");

}

sub GetComputerMove {

$MyMove = 0;

foreach $i (@BestMoves) {

if ( $Board[$i-1] eq " " ) {

$MyMove = $i;

last;

}

}

if ($MyMove != 0) {

return $MyMove};

for ($i = 1; $i<=9 ; $i++) {

if ( $Board[$i-1] eq " " ) {

$MyMove = $i;

last;

}

}

return $MyMove;

}

sub GetHumanMove {

#

# assume human makes bad moves

$OkMove = 0;

# while human continues to give bad stuff

while ($OkMove == 0) {

#

# ask human for a move, get it, remove \n

print ("What is your next move? Please enter 1-9\n");

$i = <STDIN>;

chomp($i);

#

# if human gave us between 1 and 9, then...

if ($i > 0 && $i < 10) {

#

# input ok so see if board occupied

if ( $Board[$i-1] ne " ") {

$OkMove = 0;

print ("Bad Move! Give me a better one!\n");

DisplayBoard();

} else {

#

# indicate move is ok and return it

$OkMove = 1;

$MyMove = $i;

}

} else {

#

# input bad so indicate

$OkMove = 0;

print ("Number must be 1 through 9!\n");

}

}

return $MyMove;

}

sub CheckForWinner {

#

#check if x is a winner

if ($Board[0] eq "X" && $Board[1] eq "X" && $Board[2] eq "X" ){return 1};

if ($Board[3] eq "X" && $Board[4] eq "X" && $Board[5] eq "X" ){return 1};

if ($Board[6] eq "X" && $Board[7] eq "X" && $Board[8] eq "X" ){return 1};

if ($Board[0] eq "X" && $Board[3] eq "X" && $Board[6] eq "X" ){return 1};

if ($Board[1] eq "X" && $Board[4] eq "X" && $Board[7] eq "X" ){return 1};

if ($Board[2] eq "X" && $Board[5] eq "X" && $Board[8] eq "X" ){return 1};

if ($Board[0] eq "X" && $Board[4] eq "X" && $Board[8] eq "X" ){return 1};

if ($Board[2] eq "X" && $Board[4] eq "X" && $Board[6] eq "X" ){return 1};

#

#check if 0 is a winner

if ($Board[0] eq "O" && $Board[1] eq "O" && $Board[2] eq "O" ){return 2};

if ($Board[3] eq "O" && $Board[4] eq "O" && $Board[5] eq "O" ){return 2};

if ($Board[6] eq "O" && $Board[7] eq "O" && $Board[8] eq "O" ){return 2};

if ($Board[0] eq "O" && $Board[3] eq "O" && $Board[6] eq "O" ){return 2};

if ($Board[1] eq "O" && $Board[4] eq "O" && $Board[7] eq "O" ){return 2};

if ($Board[2] eq "O" && $Board[5] eq "O" && $Board[8] eq "O" ){return 2};

if ($Board[0] eq "O" && $Board[4] eq "O" && $Board[8] eq "O" ){return 2};

if ($Board[2] eq "O" && $Board[4] eq "O" && $Board[6] eq "O" ){return 2};

}
