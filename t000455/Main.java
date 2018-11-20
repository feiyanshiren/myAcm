import java.io.*;
import java.util.*;
public class Main{
	
	int ec(int a, int b, int[] xy)
	{
		if(b == 0)
		{
			xy[0] = 1;
			xy[1] = 0;
			return a;
		}
		int r = ec(b, a % b, xy);
		int t = xy[0];
		xy[0] = xy[1];
		xy[1] = t - a / b * xy[1];
		return r;
	}
	
    public static void main(String args[]) throws Exception{
        Scanner cin=new Scanner(System.in);
        int a=cin.nextInt(),b=cin.nextInt();
        int xy[] = {0, 0};
        ec(a, b, xy);
        System.out.println(String.);
    }
}