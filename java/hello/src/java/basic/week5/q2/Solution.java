package java.basic.week5.q2;

import java.util.ArrayList;
import java.util.List;

public class Solution {
	public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int n = included.length;
        List<Integer> arr = new ArrayList<Integer>();
        for (int i=0; i<n; i++) {
        	if (included[i]) {
        		int x = a + (d * i);
        		arr.add(x);        		
        	}
        }
        
        answer = arr.stream().mapToInt(Integer::intValue).sum();
        
        return answer;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
