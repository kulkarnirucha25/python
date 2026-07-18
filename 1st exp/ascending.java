class ascending {
public static void main(String[] args) {
int[] a = {45, 12, 14, 35, 66, 22, 9, 5};
int temp;
for (int i = 0; i < 7; i++) {
for (int j = i + 1; j < 8; j++) {
if (a[i] > a[j]) {
temp = a[i];
a[i] = a[j];
a[j] = temp;
}
}
}
System.out.println("Sorted list in ascending order:");
for (int i = 0; i < 8; i++) {
System.out.print(a[i] + " ");
}
}
}
