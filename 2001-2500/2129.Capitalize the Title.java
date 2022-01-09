class Solution {
    public String capitalizeTitle(String title) {
        String[] arr = title.split(" ");
        for (int i = 0; i < arr.length; i++) {
            String str = arr[i];
            if (str.length() <= 2) {
                str = str.toLowerCase();
            } else {
                str = str.substring(0, 1).toUpperCase() + str.substring(1, str.length()).toLowerCase();
            }
            arr[i] = str;
        }
        return String.join(" ", arr);
    }
}

