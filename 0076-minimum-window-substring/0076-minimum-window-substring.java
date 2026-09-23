class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }
        Map<Character, Integer> required = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        int left = 0;
        int formation = 0;

        for (char ch : t.toCharArray()) {
            required.put(ch, required.getOrDefault(ch, 0) + 1);
        }
        int distinct_required = required.keySet().size();

        int best_length = Integer.MAX_VALUE;
        int best_start = 0;

        for (int right = 0; right < s.length(); right++) {
            char curr = s.charAt(right);
            window.put(curr, window.getOrDefault(curr, 0) + 1);

            if (required.containsKey(curr) && window.get(curr).equals(required.get(curr))) {
                formation++;
            }

            while (formation == distinct_required)  {
                int curr_length = right - left + 1;
                if (curr_length < best_length) {
                    best_length = curr_length;
                    best_start = left;
                }

                char left_char = s.charAt(left);
                window.put(left_char, window.get(left_char) - 1);
                left++;

                if (required.containsKey(left_char) && window.get(left_char) < required.get(left_char)) {
                    formation--;
                }
            }
        }

        if (best_length == Integer.MAX_VALUE) {
            return "";
        }
        return s.substring(best_start, best_start + best_length);
    }
}