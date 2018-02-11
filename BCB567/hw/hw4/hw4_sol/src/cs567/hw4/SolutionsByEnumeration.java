/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cs567.hw4;

/**
 *
 * @author usingh
 */
//import EnumerationScheme;
import static cs567.hw4.EnumerationScheme.nextVertex;
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
public class SolutionsByEnumeration {

    /**
     * Provides a solution to the motif finding problem. This problem differs
     * from the one given in lecture, in that the size of each DNA sequence is
     * not guaranteed to be the same size, i.e. the length n may vary from
     * sequence to sequence, though n will always be greater or equal to l.
     *
     * @param dna A String representing a collection of DNA sequences. Each DNA
     * sequence is delimited by a newline character '\n'.
     *
     * @param l The length of the pattern to find
     *
     * @return a List of t starting positions s maximizing score(s, dna, l)
     */
    public static List<Integer> findMotif(String dna, int l) {

        int total_input = 0;
        int thisscore = 0;
        int maxscore = -9999999;
        String[] dna_seqs = dna.split("\n");
        total_input = dna_seqs.length;
        int max_len = 0;
        for (int i = 0; i < dna_seqs.length; i++) {
            if (max_len < dna_seqs[i].length()) {
                max_len = dna_seqs[i].length();
            }
        }
        //System.out.println("maxlen:"+max_len);
        List<Integer> anspos = new ArrayList<Integer>();
        //initialize with dummy vals
        for (int i = 0; i < total_input; i++) {
            anspos.add(-1);
        }
        //Enumerate all possible motif positions
        List<Integer> result = new ArrayList<Integer>();
        List<Integer> k = new ArrayList<Integer>();
        List<Integer> finallist = new ArrayList<Integer>();
        //find all possible positions
        
        if(l>max_len){
            return null;
        }
        //assuming all dna are of same length
        for (int i = 0; i < max_len - l + 1; i++) {
            k.add(i);
        }

        int L = total_input;
        String temp = null;
        for (int i = 0; i < L; i++) {
            finallist.add(k.get(k.size() - 1));
        }

        //enumerate all Lmers with alphabet in k
        while (true) {
            result = nextVertex(result, L, k);
            //System.err.println(result);

            if (result.size() == L) {
                temp = "";
                //System.out.println(result);
                //calculate score
                thisscore = score(result, dna, l);
                if (maxscore < thisscore) {
                    maxscore = thisscore;
                    //System.out.println(result);
                    //System.out.println(thisscore + " " + maxscore);
                    //anspos = result;
                    //copy result in anspos
                    for (int i = 0; i < result.size(); i++) {
                        anspos.set(i, result.get(i));
                    }
                }

            }
            if (finallist.equals(result)) {
                break;

            }
        }

        //System.out.println("Motif found " + anspos+" with score:"+maxscore);
        return anspos; //TODO
    }

    /**
     *
     * @param s A list of integer starting positions in dna (one for each
     * sequence), representing a profile of l-mers
     *
     * @param dna A String representing a collection of DNA sequences
     *
     * @param l The length of each l-mer
     *
     * @return the profile score
     */
    public static int score(List<Integer> s, String dna, int l) {

        String[] dna_seqs = dna.split("\n");
        String[] motifs = new String[dna_seqs.length];
        boolean eflag = false;
        int fscore = 0;
        int tscore=0;
        for (int i = 0; i < dna_seqs.length; i++) {
            //get All motifs if motif doesnt exist ignore 
            motifs[i] = "";
            if (s.get(i) + l - 1 < dna_seqs[i].length()) {
                for (int k = s.get(i); k <= s.get(i) + l - 1; k++) {
                    motifs[i] = motifs[i] + dna_seqs[i].charAt(k);
                }

            } else {
                //return low score as no alignment exist.;
                return -99;
            }
        }

        //print all motifs
        /*for (int k = 0; k < motifs.length; k++) {
            System.out.println(motifs[k]);

        }*/

        //create profile matrix 4Xmotifs.length
        /*     p1 p2 ... pn
             A
             G
             C
             T
         */
        int[][]profile=new int[4][l];
        for (int k = 0; k < motifs.length; k++) {
            //System.out.println(motifs[k]);
            for (int p = 0; p < l; p++) {
                //count A G C T at position p for each kth sub string
                if(motifs[k].charAt(p)=='A'){
                    profile[0][p]++;
                }
                else if(motifs[k].charAt(p)=='G'){
                    profile[1][p]++;
                }
                else if(motifs[k].charAt(p)=='C'){
                    profile[2][p]++;
                }
                else if(motifs[k].charAt(p)=='T'){
                    profile[3][p]++;
                }
            }
        }
        
        //calculate score using profile matrix
        int max=-9999;
        for(int j=0;j<l;j++){
            max=-9999;
            for(int i=0;i<4;i++){
                if(profile[i][j]>max){
                    max=profile[i][j];
                }
            }
            tscore=tscore+max;
        }
        
        return tscore;

    }

    /**
     * Provides a solution to the median string problem. Note that this problems
     * differes from the one presented in lecture, in that the DNA sequences may
     * be of varying length.
     *
     * @param dna A String representing a collection of DNA sequences
     * @param l
     * @return
     */
    public static String medianString(String dna, int l) {

        int min_dis = 99999990;
        int max = -99999;
        int dists = 0;
        String ans = "";
        String ans2 = "";
        String[] dnaseqs = dna.split("\n");
        //create all l-mers in dna using enumeration
        //Enumerate all Lmers with alphabets in k
        List<Integer> result = new ArrayList<Integer>();
        List<Integer> k = new ArrayList<Integer>();
        List<Integer> finallist = new ArrayList<Integer>();
        k.add(1);
        k.add(2);
        k.add(3);
        k.add(4);
        int L = l;
        String temp = null;
        for (int i = 0; i < L; i++) {
            finallist.add(k.get(k.size() - 1));
        }

        //enumerate all Lmers with alphabet in k
        while (true) {
            result = nextVertex(result, L, k);
            //System.err.println(result);

            if (result.size() == L) {
                temp = "";
                //System.out.println(result);
                //convet result to DNA string
                for (int t = 0; t < result.size(); t++) {
                    if (result.get(t) == 1) {
                        temp = temp + "A";
                    } else if (result.get(t) == 2) {
                        temp = temp + "G";
                    } else if (result.get(t) == 3) {
                        temp = temp + "C";
                    } else if (result.get(t) == 4) {
                        temp = temp + "T";
                    } else {
                        System.err.println("errrr");
                    }
                }
                //System.out.println(temp);

                //search temp
                dists = totalDistance(temp, dna);
                if (min_dis >= dists) {
                    min_dis = dists;
                    ans = temp;
                    //System.out.println(dists + ":" + temp);
                }

            }

            if (finallist.equals(result)) {
                break;

            }
        }

        //System.out.println("Median String found with total distance= " + min_dis + ":" + ans);
        //System.out.println(max+":"+ans2);

        return ans; //TODO
    }

    /**
     * Returns the hamming distance between two Strings of the same length
     *
     * @param x
     * @param y
     * @return The hamming distance between x and y
     */
    public static int hd(String x, String y) {
        int dist = 0;
        for (int i = 0; i < x.length(); i++) {
            if (x.charAt(i) != y.charAt(i)) {
                dist++;
            }
        }

        return dist; //TODO
    }

    /**
     * Let l = v.length() Returns the minimum hamming distance from v across all
     * Strings of length l in dna
     *
     * @param v The candidate string
     * @param dna A String representing a collection of DNA sequences
     * @return for all substrings s in dna, the minimum hd(v,s)
     */
    public static int totalDistance(String v, String dna) {
        int l = v.length();
        //create all lmers in dna and get distances
        int k = 0;
        String temp = "";
        int min_dist = 9999999;
        int dist = 0;
        int total_dist = 0;
        String[] dnaseqs = dna.split("\n");
        for (int p = 0; p < dnaseqs.length; p++) {
            min_dist = 9999999;
            for (int i = 0; i < dnaseqs[p].length() - l + 1; i++) {

                for (int j = i; j < i + l; j++) {
                    temp = temp + dnaseqs[p].charAt(j);
                }
                //System.out.println(temp);
                //calculate distance
                dist = hd(v, temp);

                //System.out.println(dist);
                //find min_dist
                if (min_dist > dist) {
                    min_dist = dist;
                }

                temp = "";
            }

            total_dist = total_dist + min_dist;

        }
        //System.out.println("min_dist is:" + min_dist);
        return total_dist; //TODO
    }

}
