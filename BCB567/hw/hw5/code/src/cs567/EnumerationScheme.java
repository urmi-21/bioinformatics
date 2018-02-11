package cs567;

import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

public class EnumerationScheme {

	/**
	 * Given a vertex a, return the next vertex of a preorder enumeration
	 * 
	 * Each element of the enumeration (i.e. vertex) is represented
	 * as a java.util.List of Integers. The root of the enumeration tree
	 * is represented as the empty list (a List of size 0), and each prefix node
	 * i.e. internal node has a size equal to the length of the prefix, where a.size()-1
	 * is the right-most value of the prefix. The left most index is 0.
	 * 
	 * If a is the last element in the enumeration, then the first element is returned.
	 * 
	 * @param a The vertex from which the next vertex is to be found
	 * @param L The total possible number of digits each vertex can have
	 * @param k A List of size L, where k.get(i) is the total possible number of values the ith digit can have
	 * @return the next vertex
	 */
	public static List<Integer> nextVertex(List<Integer> a, int L, List<Integer> k){
		return null; //TODO
	}
	
}
