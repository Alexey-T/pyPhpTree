
<?php

namespace app\a{
    class one{
       public static function _1(){
        echo 'a one _1<br>';
       }
    }
}

namespace app\b{
    class one{
        public static function _2(){
            echo 'b one _2<br>';
        }
    }
}

namespace app{

    echo a\one::_1();
    echo b\one::_2();
    echo a\two::_1();
}

namespace app\a{
    class two{
       public static function _1(){
        echo 'a two _1<br>';
       }
    }
}
