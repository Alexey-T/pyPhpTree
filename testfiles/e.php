
<?php function getTotal($products_costs, $tax)
    {
        $total = 0.00;
       
        $callback =
            function ($pricePerItem) use ($tax, &$total)
            {
               
                $total += $pricePerItem * ($tax + 1.0);
            };
       
        array_walk($products_costs, $callback);
        return round($total, 2);
    }
?>
