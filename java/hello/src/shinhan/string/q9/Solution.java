package shinhan.string.q9;

public class Solution {
	public boolean solution(String s) {
        boolean answer = false;
        String regex = "[0-9]+";
        if ((s.length() == 4 || s.length() == 6) && s.matches(regex) ){
        	return true;
        }
        return false;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
