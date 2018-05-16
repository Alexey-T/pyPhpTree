<?
  class C1 {
    function F1a(a,b){
      }
    function /*t
      cmt*/F1b
      /*t*/()/*t*/
      {
        return 'str\'str function Fake1(){}' + 'str
            str2\'str2
            function Fake2(){}
            str3' + '' + "str\"str function Fake3(){}
            function Fake4(){}
            str"
      }
    //function Fake() {}
    function F1c(){}
?>

<?
  } /*end of C1*/
  
  class C2 /*t*/{
    function F2a(a){
    }
?>

function FakeZ(){} <?
    function F2b(){} 
    }
  } /*end if C2*/
?>
