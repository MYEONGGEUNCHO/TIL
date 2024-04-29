package java.basic.week6.q2;

class Solution {
    public int solution(int n, String control) {
        int answer = n;
        for (int i=0; i<control.length(); i++) {
        	System.out.println(i);
        }
        return answer;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 0;
		String control = "wsdawsdassw";
		Solution s = new Solution();
		System.out.println(s.solution(n, control));
	}

}
