<?
  class C1 {
    function F1a(a,b){
      }
    function /*t*/F1b
      /*t*/
      (/*t*/)/*t*/
      {
        return 'str\'str' + 'str
            str2\'str2
            function Fake1() {}
            str3' + "str
            function Fake2() {}
            str"
      }
    //function Fake() {}
?>

<?
  } /*end of C1*/
  
  class C2 /*t*/{
    function F2a(a){
    }
?>

function Z(){} <?
    function F2b(){} 
    }
  } /*end if C2*/
?>
