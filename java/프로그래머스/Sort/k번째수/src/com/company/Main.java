package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("a");

        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        KthNumber kthNumber = new KthNumber();
        for(int i = 0; i<3; i++){
            System.out.println(kthNumber.solution(array, commands)[i]);
        }
    }
}
