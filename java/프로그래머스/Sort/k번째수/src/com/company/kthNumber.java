package com.company;
import java.util.*;

class KthNumber {
    public int[] solution(int[] array, int[][] commands) {
            int[] answer = new int[commands.length];


            //int[] array = {1, 5, 2, 6, 3, 7, 4};
            //int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

            for(int i = 0; i < commands.length; i++){
                int beginNum = commands[i][0];
                int endNum = commands[i][1];
                int kthNum = commands[i][2];

                int[] tempArray = new int[endNum - beginNum + 1];

                for(int j = beginNum - 1; j < beginNum - 1 + endNum - beginNum + 1; j++){
                    tempArray[j - beginNum + 1] = array[j];
                }
                Arrays.sort(tempArray);
                answer[i] = tempArray[kthNum - 1];
            }

            return answer;
    }
}
