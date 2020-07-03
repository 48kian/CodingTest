package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("a");

        int[] numbers = {6, 10, 2};

        BiggestNum biggestNum = new BiggestNum();
        for(int i = 0; i<3; i++){
            System.out.println(biggestNum.solution(numbers));
        }
    }
}
