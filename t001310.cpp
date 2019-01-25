#include <stdio.h>
int findPoint(int a[], int n) {
	int sum, min = 20000, i, j;
	for(i = 0; i < n; i++) {
		sum = 0;
		for(j = 0; j < n; j++) {
			if(a[j] > a[i]) sum += a[j]-a[i];
			else sum += a[i]-a[j];
		}
		if(sum < min) min = sum;
	}
	return min;
}
int main() {
	int t, n, a[20], b[20], i;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		for(i = 0; i < n; i++){
            scanf("%d%d", &a[i], &b[i]);
        } 
		printf("%d\n", findPoint(a, n)+findPoint(b, n));
	}
	return 0;
}