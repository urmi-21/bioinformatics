package cs567.hw4;

import cs567.EnumerationScheme;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

/*
 * For the following problems, DNA input will be given as a String over the alphabet A,T,C,G.
 * Sequences are delimited by newline characters '\n'.
 * 
 * For example, the following DNA input:
 * 			AAAA
 * 			TTTT
 * 			CCCC
 * 			GGGG
 * 
 * would be represented as:
 * 
 * 			String dna = "AAAA\nTTTT\nCCCC\nGGGG"
 *
 *
 * Also note that sequences need not be all the same length.
 *
 *			ATTACGGGGGGGGGG
 *			TTTT
 *			ATTGACG
 *			GACTTGACCT
 *
 * The above is another example of a valid sequence, and would be represented as the String:
 * 			"ATTACGGGGGGGGGG\nTTTT\nATTGACG\nGACTTGACCT"
 * 
 * The terminology "substring" is used to refer to substrings across the alphabet A,T,C,G; the newline character is not included.
 * 
 * 
 * Make use of your EnumerationScheme class to give solutions to the following problems.
 *  You create as many of your own additional classes, methods, or other constructs as you like, 
 *  but you must follow the specifications presented below. 
 *  
 *  It may be beneficial to create helper methods to aid in converting from List<Integer> form to
 *  the proper output. Again, notice that the DNA input may not be a square matrix of n by t.
 *  
 *  (Also, the method dna.split("\n") will return an array, where each element is one of the DNA sequences; the size of this array would be equal to 't' with respect to the examples shown in lecture)
 */
public class SolutionsByEnumeration{

	
	/**
	 * Provides a solution to the motif finding problem.
	 * This problem differs from the one given in lecture, in that
	 * the size of each DNA sequence is not guaranteed to be the same size,
	 * i.e. the length n may vary from sequence to sequence,
	 * though n will always be greater or equal to l.
	 * 
	 * @param dna A String representing a collection of DNA sequences.
	 * Each DNA sequence is delimited by a newline character '\n'.
	 * 
	 * @param l The length of the pattern to find
	 * 
	 * @return a List of t starting positions s maximizing score(s, dna, l)
	 */
	public static List<Integer> findMotif(String dna, int l){
		return null; //TODO
	}
	
	/**
	 * 
	 * @param s A list of integer starting positions in dna (one for each sequence), representing a profile of l-mers
	 * 
	 * @param dna A String representing a collection of DNA sequences
	 * 
	 * @param l The length of each l-mer
	 * 
	 * @return the profile score
	 */
	public static int score(List<Integer> s, String dna, int l){
		return 0; //TODO
	}
	
	/**
	 * Provides a solution to the median string problem. Note that this problems differes from
	 * the one presented in lecture, in that the DNA sequences may be of varying length.
	 * @param dna A String representing a collection of DNA sequences
	 * @param l
	 * @return
	 */
	public static String medianString(String dna, int l){
		return null; //TODO
	}
	
	/**
	 * Returns the hamming distance between two Strings of the same length
	 * @param x
	 * @param y
	 * @return The hamming distance between x and y
	 */
	public static int hd(String x, String y){
		return 0; //TODO
	}
	
	/**
	 * Let l = v.length()
	 * Returns the minimum hamming distance from v across all Strings of length l in dna 
	 * @param v The candidate string
	 * @param dna A String representing a collection of DNA sequences
	 * @return for all substrings s in dna, the minimum hd(v,s)
	 */
	public static int totalDistance(String v, String dna){
		return 0; //TODO
	}
		
}
