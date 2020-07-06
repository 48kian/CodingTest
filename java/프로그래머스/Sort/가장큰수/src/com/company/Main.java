package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("a");

        int[] numbers = {3, 30, 34, 5, 9};

        BiggestNum biggestNum = new BiggestNum();
        for(int i = 0; i<3; i++){
            System.out.println(biggestNum.solution(numbers));
        }
    }
}
