package com.company;

public class Main {

    public static void main(String[] args) {

        // write your code here
        System.out.println("a");

        String begin = "hit";
        String target = "cog";
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};
        //String[] words2 = {"hot", "dot", "dog", "lot", "log"};

        ChangeWord changeWord = new ChangeWord();
        for(int i = 0; i<3; i++){
            System.out.println(changeWord.solution(begin, target, words));
        }
    }

}

