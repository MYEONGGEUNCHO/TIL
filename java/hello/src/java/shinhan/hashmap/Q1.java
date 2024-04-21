package java.shinhan.hashmap;

import java.util.HashMap;
import java.util.Map;

public class Q1 {
	public String solution(String[] participant, String[] completion) {
		String answer = "";
		HashMap<String, Integer> check = new HashMap<String, Integer>();
		
		for (String player: participant) {
			if (check.containsKey(player)) {
				check.put(player, check.get(player) + 1);
			} else {
				check.put(player, 1);
			}
		}
		
		for (String player: completion) {
			if (check.containsKey(player)) {
				check.put(player, check.get(player) - 1);
			}
		}
		
		for (Map.Entry<String, Integer> entry : check.entrySet()) {
			if (entry.getValue() != 0) {
				answer = entry.getKey();
			}
		}
		
		return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
