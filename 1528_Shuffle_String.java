class Solution {
    public String restoreString(String s, int[] indices) {
        char[] t = new char[s.length()];
        for (int i = 0; i < indices.length; i++) {
            //tricky bit is below
            t[indices[i]] = s.charAt(i);
            
        }
        return new String(t);
    }
}