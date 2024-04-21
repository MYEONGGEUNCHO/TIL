package java.basic.week5.q5;

class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String res1 = "";
        String res2 = "";
        for (int num: num_list) {
            if (num % 2 == 0) {
//                res1 += Integer.toString(num);
            	res1 += (num +"");
            } else {
//                res2 += Integer.toString(num);
            	res2 += (num +"");
            }
        }
        answer = Integer.parseInt(res1) + Integer.parseInt(res2);
        return answer;
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
