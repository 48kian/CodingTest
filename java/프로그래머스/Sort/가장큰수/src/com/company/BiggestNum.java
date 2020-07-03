package com.company;
import java.util.*;

class BiggestNum {
    public String solution(int[] numbers) {
            String answer = "";


            //[3, 30, 34, 5, 9] 	9534330
            //[6, 10, 2]	6210

            첫번째가 크면 큰거
                만약에 같다면 1. 짧은걸 넣어줘


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
