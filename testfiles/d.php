<?
//Test heredoc

//id
<<<AB
  function Fake1() {}
AB
  //still heredoc  
  function Fake1b() {}
AB;

//'id'
<<<'BB'
  function Fake2() {}
    BB;  
  function Fake2b() {}
BB;

//"id"  
<<<"DD"
  function Fake3() {}
DD;

function F1() {}
