import java.util.*; // package contains the Map, HashMap, TreeSet.

public class CountWord {

 public static void main(String args[]) {

  Map < String, Integer > map = new HashMap < > (); 
  String sc = "Java programme to count no. of word in group of word.";

  String[] tokens = sc.split(" "); 
  for (String token: tokens) {

   String word = token.toLowerCase();
   if (map.containsKey(word)) {
    int count = map.get(word); 
    map.put(word, count + 1); 
   } else {
    map.put(word, 1); // default word count = 1
   }
  }

  //display the data
  Set < String > keys = map.keySet(); // list of unique words using set

  TreeSet < String > sortedKeys = new TreeSet < > (keys); // ascending order of words

  for (String str: sortedKeys) {

   System.out.println("Word =" + str + " and it's count = " + map.get(str));

  }
 }
}