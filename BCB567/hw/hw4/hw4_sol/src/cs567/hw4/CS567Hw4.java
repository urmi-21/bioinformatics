/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cs567.hw4;

import static cs567.hw4.EnumerationScheme.nextVertex;
import static cs567.hw4.SolutionsByEnumeration.findMotif;
import static cs567.hw4.SolutionsByEnumeration.hd;
import static cs567.hw4.SolutionsByEnumeration.medianString;
import static cs567.hw4.SolutionsByEnumeration.score;
import static cs567.hw4.SolutionsByEnumeration.totalDistance;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.TimeUnit;

/**
 *
 * @author usingh
 */
public class CS567Hw4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String INPUT1 = "ATTGACGATTGACT" + "\n"
                + "GAACTTGACGATTGCAG" + "\n"
                + "GTGACGATTTACCGACT" + "\n"
                + "CATGACGATTGGAC" + "\n"
                + "GGACTGACGATTAT" + "\n"
                + "GATCTTGACGATTCTAT" + "\n"
                + "CATAGATATGACGATTA";
        //Enumerate all Lmers with alphabets in k
        System.out.println("Enumerating all lmers");
        List<Integer> result = new ArrayList<Integer>();
        List<Integer> a1 = new ArrayList<Integer>();
        List<Integer> k = new ArrayList<Integer>();
        List<Integer> finallist = new ArrayList<Integer>();
        k.add(1);
        k.add(2);
        k.add(3);
        k.add(4);
        int L = 2;
        for (int i = 0; i < L; i++) {
            finallist.add(k.get(k.size() - 1));
        }

        //enumerate all Lmers with alphabet in k
        while (true) {
            result = nextVertex(result, L, k);
            //System.err.println(result);
            if (result.size() == L) {
                System.out.println(result);
            }
            if (finallist.equals(result)) {
                break;
            }
        }

        System.out.println("Finding hd bw AAA GGG");
        //run median string algorithm
        int d = hd("AAA", "GGG");
        System.out.println("Finding hd bw AAA GGG:" + d);
        System.out.println("Finding total distance bw TTGACGAT and INPUT1");
        int td = totalDistance("TTGACGAT", INPUT1);
        System.out.println("Finding total distance bw TTGACGAT and INPUT1: " + td);

        System.out.println("Finding median String");
        String ans = medianString(INPUT1, 8);
        System.out.println("Finding median String: " + ans);

        System.out.println("Finding motif...");
        List<Integer> anspos = findMotif(INPUT1, 8);
        System.out.println("Finding motif : " + anspos);

        //simulating time for n and ls
        int t = 5; //total 10 dna sequences of each length n
        int n = 10;
        Random rand = new Random();

        //generate t random DNA of length n
        System.out.println("n\tm\tmotif_time\tmediantime");
        for (n = 50; n <= 50; n = n + 20) {
            String dna = "";
            for (int i = 0; i < t; i++) {
                for (int q = 0; q < n; q++) {
                    int r = rand.nextInt(4) + 1;
                    if (r == 1) {
                        dna = dna + "A";
                    } else if (r == 2) {
                        dna = dna + "G";
                    } else if (r == 3) {
                        dna = dna + "C";
                    } else if (r == 4) {
                        dna = dna + "T";
                    }

                }
                dna = dna + "\n";
            }
            dna = dna.substring(0, dna.length() - 1);
            //System.out.println(dna);

            //find times for motif and median search
            for (int m = 2; m <= 12; m = m + 2) {

                long startmedTime = System.currentTimeMillis();
                String medianstr = medianString(dna, m);
                long endmedTime = System.currentTimeMillis();
                long totalmedTime = endmedTime - startmedTime;

                long startmotifTime = System.currentTimeMillis();
                findMotif(dna, m);
                long endmotifTime = System.currentTimeMillis();
                long totalmotifTime = endmotifTime - startmotifTime;

                System.out.println(n + "\t" + m + "\t" + TimeUnit.MILLISECONDS.toSeconds(totalmotifTime) + "\t" + TimeUnit.MILLISECONDS.toSeconds(totalmedTime));
            }
        }
    }

}
