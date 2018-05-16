<?php
// multiple namespaces in a single file:

namespace foo{
  class Cat {
    static function says() {echo 'meoow';}  }
}

namespace bar{
  class Dog {
    static function says() {echo 'ruff';}  } 
  class Cat {
    static function says() {echo 'meowi';}  }
  class Mouse {     //nonstatic function
    function says() {echo 'Come and get me ;)';}  }
}

namespace animate{
  class Animal {
    static function breathes() {echo 'air';}  }
}

namespace{        // No Namespace: global code
  use foo as feline;
  use bar as canine;
  use bar\Mouse as MouseOnly;
  use animate;
  echo animate\Animal::breathes(), "<br />\n"; 
  echo feline\Cat::says(), "<br />\n"; //not starting with a slash!
  echo canine\Cat::says(), "<br />\n";
  echo canine\Dog::says(), "<br />\n";
  //any of the three following lines work:
  // $micky=new bar\Mouse();
  // $micky=new canine\Mouse();
  $micky=new test();
  echo $micky->says();
}
?>
