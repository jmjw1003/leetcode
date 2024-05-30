/** 
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */

var mergeAlternately = function(word1, word2) {
    var result = '';
    for (var i = 0; i < Math.min(word1.length, word2.length); i++) {
        result += word1[i] + word2[i]
    };
    result += word1.slice(i) + word2.slice(i);
    return result;
}
