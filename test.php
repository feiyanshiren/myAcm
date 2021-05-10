<?php
$in;
while(($in=fgets(STDIN))!=false)
{
    $arr=explode(" ",$in);
    echo $arr[0]+$arr[1]."\n";
}