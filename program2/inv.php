<?php
$split_inv = 0;
/**
 * Recursively merges and sorts an array
 * @param array $array the unsorted array
 * @returns array the sorted array
 */
function merge_sort( $array ) {
//echo("merge_sort starting " . implode("|",$array)  . "\n");
    //if array is but one element, array is sorted, so return as is
    if ( sizeof ( $array ) == 1 ) {
//echo("merge_sort returning array " . implode("|",$array)  . "\n");
    	return $array;
    }

    //bifurcate unsorted array
    $array2 = array_splice( $array, ( sizeof( $array ) / 2 ) );

    //recursively merge-sort and return
    return merge_and_count_split_inv( merge_sort( $array ), merge_sort( $array2 ) );

}
/**
 * Merges two arrays into one sorted array and counts the number of inversions
 * @param array $array1 one array
 * @param array $array2 another array
 * @returns array the sorted, merged array
 */
function merge_and_count_split_inv( $array1, $array2 ) {
	global $split_inv;
//echo("merge_and_. starting: array1: " . implode("|",$array1) . "  array2: " . implode("|",$array2) . "\n");

    //init an empty output array
    $output = array();

    //loop through the arrays while at least one still has elements left in it
    while( !empty( $array1 ) || !empty( $array2 ) )

    	//one of the arrays is empty, so the last man standing wins...
    	if ( empty( $array1 ) || empty( $array2 ) )
    		$output[] = ( empty( $array2 ) ) ? array_shift( $array1 ) : array_shift( $array2 );

    	//both arrays still have elements, looks like we have a showdown...
    	else {
    	//	$output[] = ( $array1[ 0 ] <= $array2[ 0 ] ) ? array_shift( $array1 ) : array_shift( $array2 );
		if ( $array1[0] <= $array2[0] ) {
			$output[] = array_shift( $array1 );
		} else {
			$output[] = array_shift( $array2 );
			//$split_inv++;
			$split_inv = $split_inv + sizeof($array1);
		}
	}
//echo("merge_and_. returning output: " . implode("|",$output) . "\n");
echo("split_inv count: " . $split_inv . "\n");
    //pass back the output array
    return $output;

}
?>
