package java.basic.week6.q1;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        
        int n = num_list.length;
        int[] arr = new int[num_list.length + 1];
        
        for (int i=0; i<n; i++) {
        	arr[i] = num_list[i];
        }
        
        int a = num_list[n-1];
        int b = num_list[n-2];
        
        if (a>b) {
        	arr[n] = a*2;
        } else {
        	arr[n] = a - b;
        }
        
        
        
        return arr;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
