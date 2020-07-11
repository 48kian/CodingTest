package com.company;

public class Main {

    public static void main(String[] args) {
        // write your code here
        System.out.println("a");

        int[][] computers = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
        int n = 3;

        Network network = new Network();
        for(int i = 0; i<3; i++){
            System.out.println(network.solution(n, computers));
        }
    }
}
