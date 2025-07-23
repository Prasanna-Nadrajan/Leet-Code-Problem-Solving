class Solution {
    private int gain(String s, String highPriorityPair, String lowPriorityPair, int highPriorityScore, int lowPriorityScore) {
        int totalScore = 0;
        Deque<Character> deck = new ArrayDeque<>();
        
        char highFirst = highPriorityPair.charAt(0);
        char highSecond = highPriorityPair.charAt(1);

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (currentChar == highSecond && !deck.isEmpty() && deck.peek() == highFirst) {
                deck.pop();
                totalScore += highPriorityScore;
            } else {
                deck.push(currentChar);
            }
        }

        StringBuilder remainingString = new StringBuilder();
        while (!deck.isEmpty()) {
            remainingString.append(deck.pollLast());
        }
        
        s = remainingString.toString();
        
        char lowFirst = lowPriorityPair.charAt(0);
        char lowSecond = lowPriorityPair.charAt(1);

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (currentChar == lowSecond && !deck.isEmpty() && deck.peek() == lowFirst) {
                deck.pop();
                totalScore += lowPriorityScore;
            } else {
                deck.push(currentChar);
            }
        }

        return totalScore;
    }


    public int maximumGain(String s, int x, int y) {
        if (x > y) {
        
            return gain(s, "ab", "ba", x, y);
        } else {
       
            return gain(s, "ba", "ab", y, x);
        }
    }
}
