package shinhan.string.q10;

public class Solution {
	public String solution(String new_id) {
        String answer = "";
//        1단계 조건
        answer = new_id.toLowerCase();
//        2단계 특수문자 제거
        String regex = "[^ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9._-]";
        answer = answer.replaceAll(regex,  "");
//        3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
        while (answer.contains("..")) {
        	answer = answer.replace("..", ".");
        };
//        4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
        if (answer.startsWith(".")) {
        	answer = answer.substring(1);
        }
        if (answer.endsWith(".")) {
        	answer = answer.substring(0, answer.length() - 1);
        }
//        5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
        if (answer.equals("")){
        	answer = "a";
        }
//        6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
//             만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if (answer.length() >= 16) {
        	answer = answer.substring(0, 15);
        	if (answer.endsWith(".")) {
        		answer = answer.substring(0, 14);
        	}
        }
//        7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
        while (answer.length() <= 2) {
        	answer = answer + answer.substring(answer.length() - 1);
        }
        
        return answer;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution ans = new Solution();
		String test =	"abcdefghijklmn.p";
		System.out.println(ans.solution(test));
	}

}
