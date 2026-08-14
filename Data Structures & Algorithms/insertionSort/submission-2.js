/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        const result = [];
        for(let i=0; i < pairs.length; i++){
            let curr = i;
            let prev = curr - 1;
            while(curr > 0 && (pairs[prev].key > pairs[curr].key)){
                [pairs[prev], pairs[curr]] = [pairs[curr], pairs[prev]];
                prev--;
                curr--;
            }
            result.push([...pairs]);
        }
        return result;
    }
}
