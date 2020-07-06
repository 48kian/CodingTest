package com.company;
import java.util.*;

class BiggestNum {
    public String solution(int[] numbers) {
        String answer = "";


        //[3, 30, 34, 5, 9] 	9534330
        //[6, 10, 2]	6210

        String[] stringArr = new String[numbers.length];

        for(int j = 0; j<numbers.length; j++){
            stringArr[j] = String.valueOf(numbers[j]);
        }

        Arrays.sort(stringArr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {

                return (o2+o1).compareTo(o1+o2);
            }
        });

        if(stringArr[0].equals("0")){
            return "0";
        }

        for(int i = 0; i < stringArr.length; i++){

            answer += stringArr[i];

        }


        return answer;
    }
}


//        첫번째가 크면 큰거
//        만약에 같다면 1. 두번째 숫자가 첫번째 숫자보다 같거나 크면 그걸 앞으로 해줘
//        1. 내림차순 정렬을 한다.
//        2. 왼쪽과 오른쪽 비교해서 다르면 일단 넣는다.
//        3. 같으면 비교한다.
//
//
//        if (a[0] > b[0]) {
//            a가 더 큼;
//        } else if (a[0] == b[0]) {
//            compareString(a, b);
//        }
//
//        int compareString (String a, String b){
//            if (a.equals(b)) {
//                return 3;
//            }
//            if (a.length() <= b.length()) {
//                for (int i = 0; i < a.length(); i++) {
//                    if (a[i] < b[i] && a[0] < b[i]) {
//                        return 2;
//                    }
//                    if (a[i] > b[i] && a[0])
//                }
//
//            } else if (a.length() > b.length()) {
//                for (int i = 0; i < b.length(); i++) {
//
//                }
//            }
//
//        }

