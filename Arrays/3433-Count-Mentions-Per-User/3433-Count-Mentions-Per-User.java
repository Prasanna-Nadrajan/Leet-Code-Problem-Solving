class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        events.sort((a, b) -> {
            int t1 = Integer.parseInt(a.get(1));
            int t2 = Integer.parseInt(b.get(1));
            if (t1 != t2)
                return t1 - t2;
            return a.get(0).equals("OFFLINE") ? -1 : 1;
        });

        int[] mentions = new int[numberOfUsers];
        int[] offlineUntil = new int[numberOfUsers];

        for (List<String> e : events) {
            String type = e.get(0);
            int ts = Integer.parseInt(e.get(1));

            if (type.equals("OFFLINE")) {
                int id = Integer.parseInt(e.get(2));
                offlineUntil[id] = ts + 60;
            } else {
                String msg = e.get(2);
                if (msg.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (msg.equals("HERE")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        if (offlineUntil[i] <= ts) {
                            mentions[i]++;
                        }
                    }
                } else {
                    String[] ids = msg.split(" ");
                    for (String idStr : ids) {
                        int id = Integer.parseInt(idStr.substring(2));
                        mentions[id]++;
                    }
                }
            }
        }
        return mentions;
    }
}
